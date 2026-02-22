# 🎯 Real-Time Object Tracking using OpenCV

A computer vision project that implements real-time object tracking using OpenCV in Python.  
The system detects and tracks moving objects in video streams using background subtraction and contour-based detection techniques.

---

## 📖 Overview

Object tracking is a fundamental task in computer vision with applications in:

- Surveillance systems
- Autonomous vehicles
- Human motion analysis
- Smart traffic systems
- Industrial monitoring

This project demonstrates a classical computer vision approach to tracking moving objects in video frames.

---

## 🧠 Methodology

The tracking pipeline follows these steps:

1. **Video Capture**
   - Load video stream using OpenCV.

2. **Preprocessing**
   - Convert frames to grayscale
   - Apply Gaussian blur to reduce noise

3. **Background Subtraction**
   - Detect motion regions by separating foreground from background

4. **Thresholding & Morphological Operations**
   - Remove noise
   - Improve contour detection quality

5. **Contour Detection**
   - Identify moving objects
   - Draw bounding boxes around detected objects

---

## 🛠 Technologies Used

- Python 3.x
- OpenCV
- NumPy
- Jupyter Notebook (for experimentation)

---

## 📂 Project Structure
