import streamlit as st
import cv2
import numpy as np
import tempfile
import time

# --- Page Config ---
st.set_page_config(
    page_title="Object Tracking App",
    layout="wide",
    page_icon=":guardsman:"
)

# --- Sidebar ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/security-checked.png", width=80)
    st.header("Object Tracking App")
    st.markdown(
        "Upload a video file to detect and track moving objects using background subtraction. "
        "Results are displayed side by side for easy comparison."
    )
    st.markdown("---")
    st.info("Supported formats: mp4, avi, mov")
    st.markdown("---")
    st.subheader("Detection Box Color")
    box_color = st.color_picker("Pick a color for the detection box", "#FF0000")
    st.subheader("Video Speed")
    speed = st.slider("Playback speed (frames/sec)", min_value=1, max_value=60, value=30)

# --- Main Title & Description ---
st.title("🎯 Object Tracking with Background Subtraction")
st.markdown(
    """
    <style>
    .big-font {font-size:18px !important;}
    </style>
    <div class="big-font">
    This application allows you to upload a video file and perform object tracking using background subtraction.<br>
    <b>Original</b> and <b>Processed</b> frames are displayed side by side.
    </div>
    """,
    unsafe_allow_html=True
)

def convert_img(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

uploaded_file = st.file_uploader("📤 Upload a Video", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    tfile.close()

    cap = cv2.VideoCapture(tfile.name)

    if not cap.isOpened():
        st.error("❌ Error opening video file.")
    else:
        st.success("✅ Video uploaded successfully! Processing...")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Original Frame")
            stframe = st.empty()
        with col2:
            st.subheader("Detected Objects")
            stframe2 = st.empty()

        back_subtractor = cv2.createBackgroundSubtractorMOG2()
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        progress = st.progress(0)

        # Convert hex color to BGR for OpenCV
        hex_color = box_color.lstrip('#')
        box_bgr = tuple(int(hex_color[i:i+2], 16) for i in (4, 2, 0))

        frame_idx = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            fg_mask = back_subtractor.apply(frame)
            contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                if cv2.contourArea(cnt) > 300:
                    x, y, w, h = cv2.boundingRect(cnt)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), box_bgr, 2)

            stframe.image(convert_img(frame), channels="RGB", use_container_width=True)
            stframe2.image(fg_mask, channels="GRAY", use_container_width=True)
            frame_idx += 1
            progress.progress(min(frame_idx / frame_count, 1.0))
            time.sleep(1.0 / speed)
        cap.release()
        st.success("🎉 Video processing completed!")

