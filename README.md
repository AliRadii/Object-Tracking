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

You said:
Uploaded image
listen i now have a project like this how can i publish it to github 

ChatGPT said:
Great Aly — perfect step 👌
Publishing your project to GitHub is very important for your AI portfolio.

I’ll give you a clean, professional workflow (the way real developers do it).

✅ What You Have
Your project folder:

Object Tracking/
│── app.py
│── object_tracking.ipynb
│── vtest.avi
│── background video.mp4
│── image-1.png
🚨 Step 0 — IMPORTANT (Before Uploading)
You should NOT upload large video files to GitHub.

Why?

GitHub is for code.

Large media files make the repo heavy.

It looks unprofessional.

So:

❌ Don’t upload .avi or .mp4

❌ Don’t upload random images unless needed

✅ Upload code only

🧠 Step 1 — Prepare Your Project (Professional Structure)
Inside Object Tracking, create:

Object-Tracking/
│── app.py
│── object_tracking.ipynb
│── requirements.txt
│── README.md
│── .gitignore
│── sample_output.png (optional)
1️⃣ Create requirements.txt
If you're using:

OpenCV

NumPy

etc.

Create file:

requirements.txt
Example content:

opencv-python
numpy
matplotlib
If you want auto-generate:

pip freeze > requirements.txt
2️⃣ Create .gitignore
Create file:

.gitignore
Add:

__pycache__/
*.pyc
*.avi
*.mp4
.env
This prevents large videos from uploading.

3️⃣ Create a Strong README.md
Very important for portfolio.

Example:

# 🎯 Object Tracking using OpenCV

This project implements object tracking using computer vision techniques in Python.

## 🚀 Features
- Real-time object tracking
- Background subtraction
- Bounding box detection

## 🛠 Technologies Used
- Python
- OpenCV
- NumPy

## ▶️ How to Run

1. Install dependencies:
pip install -r requirements.txt


2. Run:
python app.py


## 📷 Sample Output
(Add screenshot here)

---

## 📌 Author
Aly Rady
🔥 Step 2 — Create GitHub Repository
Go to:
👉 https://github.com

Click:
➜ New Repository

Fill:

Name: Object-Tracking

Description: Real-time object tracking using OpenCV

Public ✅

DO NOT initialize with README (you already have one)

Click Create

💻 Step 3 — Upload Using Git (Best Method)
Open terminal inside your project folder.

If Git is not installed:
👉 Download Git first.

First Time Setup (Only once ever)
git config --global user.name "Aly Rady"
git config --global user.email "r2dy2005@gmail.com"
Initialize Project
Inside Object Tracking folder:

git init
git add .
git commit -m "Initial commit - Object Tracking Project"
Connect to GitHub
GitHub will show something like:

git remote add origin https://github.com/YOUR_USERNAME/Object-Tracking.git
git branch -M main
git push -u origin main
Paste and run.

🎉 Done!
Your project is now online.

🏆 Bonus (Make It Portfolio-Level)
To make it look professional:

✔ Add demo GIF
Record 5 sec and convert to GIF.
Upload small GIF.

✔ Add:
Problem statement

Method explanation

Algorithm explanation

Performance discussion

✔ Add project structure explanation
🚀 Next Level (Very Important for AI Engineer)
Later you should:

Convert notebook → clean modular Python project

Create src/ folder

Add argument parsing

Add config file

That makes you look like a real engineer, not just student.

If you want, I can:

Review your project structure

Help you write a strong README

Help you restructure it professionally

Help you deploy a live demo

What level do you want this project to reach? 🔥


You said:
Uploaded image
ok step by step i made this

ChatGPT said:
Perfect Aly ✅ You’re doing it right — I can see you already added requirements.txt.
Now let’s publish it to GitHub step by step, exactly what to do + what to type.

0) Quick fix before pushing (IMPORTANT)
You still have:

vtest.avi

background video....mp4

These should NOT go to GitHub.

✅ Create .gitignore
Inside your folder Object Tracking:

Right click → New → Text Document

Name it exactly:
.gitignore
(Make sure it’s not .gitignore.txt)

If Windows hides extensions:

File Explorer → View → Show → ✅ File name extensions

Now open .gitignore and paste:

__pycache__/
*.pyc
*.avi
*.mp4
*.png
.ipynb_checkpoints/
.env
If you WANT to upload the png screenshot, remove *.png from ignore.

1) Create the repo on GitHub
Go to GitHub → New repository

Name: Object-Tracking

Public ✅

Don’t add README (we’ll push your local one later)

Click Create repository

Leave that page open.

2) Open Terminal inside the project folder
Go to your folder:
D:\Route course\Projects\Object Tracking

Then:

Click on the address bar (top path)

Type cmd

Press Enter

A terminal opens already in the folder ✅

3) Run these commands (copy/paste exactly)
A) Initialize git
git init
B) Add files
git add .
C) Commit
git commit -m "Initial commit"
4) Connect to GitHub and push
On the GitHub repo page you created, you’ll see a URL like:

https://github.com/YOUR_USERNAME/Object-Tracking.git

Copy it, then run:

git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Object-Tracking.git
git push -u origin main
5) Verify
Refresh your GitHub repo page → your files should appear 🎉

✅ If you get a common error
“git is not recognized…”
→ You need to install Git:

Install “Git for Windows”

Then reopen CMD and retry

“Authentication failed”
→ GitHub now requires login via:

Browser login popup OR

Personal Access Token (PAT)

If that happens, tell me the exact error line and I’ll guide you in 2 minutes.

One check for you now:
After you run git add . type this command:

git status
If you paste me the output of git status, I’ll confirm you’re not accidentally uploading the mp4/avi before you push.


You said:
Uploaded image

ChatGPT said:
Good catch Aly 👌 I can see the problem immediately.

Your file name is:

.gitignore.txt
🚨 That is WRONG.

Git will NOT recognize it.

✅ Fix It Properly
Step 1 — Enable file extensions (VERY IMPORTANT)
In File Explorer:

Click View

Click Show

Enable ✅ File name extensions

Now you will see full names.

Step 2 — Rename the file
Change:

.gitignore.txt
To exactly:

.gitignore
No .txt
No extra spaces
Nothing after it.

It should look like this:

.gitignore   (Type: File)
Step 3 — Confirm it's correct
After renaming:

Open CMD in that folder and run:

git init
git add .
git status
Now you should NOT see:

vtest.avi

background video.mp4

image-1.png

in the staged files.

⚠ Why this matters
If .gitignore is wrong:

Git will upload:

All your videos

All images

Everything

Which:

Makes repo heavy

Looks unprofessional

Sometimes fails push

🔥 After You Fix It
Paste me the output of:

git status
And I’ll confirm you're 100% safe before pushing.

You're doing this correctly — just one small Windows trap 😄


You said:
Uploaded image

ChatGPT said:
Perfect Aly 👌🔥

Now it’s correct:

.gitignore   (Type: Git Ignore Source)
That means Git will now ignore:

.avi

.mp4

.png

cache files

You’re safe ✅

🚀 Now Let’s Push It (Carefully)
Open CMD inside this folder and run step by step:

1️⃣ Initialize Git
git init
2️⃣ Add files
git add .
3️⃣ IMPORTANT — Check before commit
git status
You should see something like:

new file: app.py
new file: object_tracking.ipynb
new file: requirements.txt
new file: .gitignore
You should NOT see:

vtest.avi

background video.mp4

image-1.png

If they don’t appear → perfect.

4️⃣ Commit
git commit -m "Initial commit - Object Tracking project"
5️⃣ Connect to GitHub
After creating the repo online, copy the repo URL and run:

git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Object-Tracking.git
git push -u origin main
Replace YOUR_USERNAME.

🧠 Important Note
If videos still show in git status:

That means you ran git add . before fixing .gitignore.

In that case run:

git rm --cached *.avi
git rm --cached *.mp4
git rm --cached *.png
Then:

git add .
git commit -m "Clean commit"
🎯 After Push
Refresh GitHub page → your repo should appear clean with only code.

Send me the output of:

git status
and I’ll confirm you’re 100% good before pushing 🔥


You said:
Uploaded image

ChatGPT said:
Perfect Aly — this is normal 👌
The error means:

Git is NOT installed on your machine.

✅ Step 1 — Install Git (Very Easy)
Go to:
👉 

Download and install.

During installation:

Just keep clicking Next
BUT make sure this option is selected:

✅ “Git from the command line and also from 3rd-party software”

(VERY IMPORTANT — this adds Git to PATH)

Finish installation.

✅ Step 2 — Restart CMD
Close the current CMD window completely.

Open it again:

Go to your project folder

Click address bar

Type cmd

Press Enter

✅ Step 3 — Test Git
Type:

git --version
You should see something like:

git version 2.44.0.windows.1
If you see that → Git is installed correctly 🎉

✅ Step 4 — Now Run Again
git init
🧠 Why This Happened
Windows does NOT come with Git by default.

Git is:

The tool that connects your computer to GitHub.

Used by ALL developers.

This is your first real developer setup moment 🔥

After you install, tell me what git --version prints.

We continue immediately.


You said:
Uploaded image

ChatGPT said:
YESSS 🔥🔥🔥

This line:

Initialized empty Git repository in D:/Route course/Projects/Object Tracking/.git/
means:

👉 Git is installed correctly
👉 Repository initialized successfully
👉 You are now officially using version control like a real developer 😎

🚀 Next Step
Now type:

git add .
Then immediately:

git status
🔎 What I Want To Check
We need to confirm that:

❌ .avi is NOT included
❌ .mp4 is NOT included
❌ .png is NOT included

Because .gitignore should block them.

Paste me the output of:

git status
before we commit.

We’re doing this the clean professional way 💪


You said:
Uploaded image

ChatGPT said:
Perfect Aly 👌🔥

This is exactly what we want.

From your git status:

new file:  .gitignore
new file:  app.py
new file:  object_tracking.ipynb
new file:  requirements.txt
✅ No .avi
✅ No .mp4
✅ No .png

Your .gitignore is working perfectly.

The LF/CRLF warning is normal on Windows — ignore it.

🚀 Now Commit
Run:

git commit -m "Initial commit - Object Tracking project"
🌍 Now Connect to GitHub
Go to GitHub:

Create new repository

Name: Object-Tracking

Public

Do NOT initialize with README

After creation, copy the repository URL.

It will look like:

https://github.com/YOUR_USERNAME/Object-Tracking.git
🔗 Connect Local Repo to GitHub
Back in CMD, run:

git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Object-Tracking.git
git push -u origin main
Replace YOUR_USERNAME.

🔐 If GitHub Asks for Login
A browser window will open.
Just login and authorize.

If it asks for password directly:
→ You’ll need a Personal Access Token (I’ll guide you if that happens).

After you push, refresh your GitHub page.

Tell me what happens when you run:

git push -u origin main
We’re almost done 🔥


You said:
Uploaded image

ChatGPT said:
Perfect Aly 👌🔥
This is normal — Git just needs to know who you are.

Right now Git says:

Author identity unknown

So we just need to configure your name and email once.

✅ Step 1 — Set Your Git Identity
Run these commands exactly:

git config --global user.name "Aly Rady"
git config --global user.email "r2dy2005@gmail.com"
⚠ Use the same email you use on GitHub.

✅ Step 2 — Try Commit Again
Now run:

git commit -m "Initial commit - Object Tracking project"
It should succeed now.

🧠 Why This Happens
Git tracks:

Who made the commit

When

What changed

Every commit in the world has an author attached.

You only need to configure this once on your machine.

🚀 After It Works
Then continue with:

git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Object-Tracking.git
git push -u origin main
(Replace YOUR_USERNAME)

Run the config commands now and tell me what the commit output says 🔥


You said:
Uploaded image

ChatGPT said:
YESSSS 🔥🔥🔥

This line:

[master (root-commit) a5585dd] Initial commit - Object Tracking project
4 files changed, 518 insertions(+)
means:

✅ Commit successful
✅ Files saved in Git history
✅ You are officially version-controlling your project

You just made your first real Git commit 😎

🚀 FINAL STEP — Push to GitHub
Now let’s connect it to GitHub.

1️⃣ Create Repo on GitHub (if not yet)
Go to GitHub → New repository

Name:

Object-Tracking
Public
DO NOT initialize with README

Click Create.

2️⃣ Copy Repo URL
It will look like:

https://github.com/YOUR_USERNAME/Object-Tracking.git
3️⃣ Back to CMD — Run These
Replace YOUR_USERNAME:

git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Object-Tracking.git
git push -u origin main
🔐 If Login Appears
A browser popup will appear → login → authorize.

If it asks for password in terminal:
You need a Personal Access Token (tell me if that happens).

🧠 Small Note
You are currently on branch:

master
But we renamed it to:

main
That’s modern standard.

After you run git push -u origin main, tell me what output you see 🔥


You said:
Uploaded image

ChatGPT said:
Perfect Aly 👌🔥 you’re on the right screen.

But I see one important thing:

Your repository is set to:

🔒 Private

⚠️ For Portfolio → Make It Public
Since this is a portfolio project, change:

👉 Private → Public

Because:

Recruiters can’t see private repos

Your GitHub profile won’t showcase it

⚠️ VERY IMPORTANT
I also see:

✅ Add README → ON

You should turn this OFF.

Because:

You already have a local repo

If GitHub creates a README online,
you’ll get a merge conflict when pushing.

So:

👉 Turn OFF "Add README"

✅ Correct Settings Should Be:
Public ✅

Add README ❌ OFF

Add .gitignore ❌ No

Add license ❌ No

Then click:

👉 Create repository

🚀 After You Click Create
GitHub will show you a page with commands.

Now go back to CMD and run:

git branch -M main
git remote add origin https://github.com/AliRadii/Object-Tracking.git
git push -u origin main
(Use exactly the URL GitHub gives you.)

🔥 Before You Click Create:
Tell me:

Did you switch to Public?

Did you turn off README?

Confirm and then create it 👌


You said:
Uploaded image

ChatGPT said:
Perfect Aly 👌🔥

Now everything is correct:

✅ Public
✅ README OFF
✅ No .gitignore
✅ No license

You’re ready.

🚀 Click Create repository
After it creates the repo, GitHub will show a page with some commands.

🖥️ Then Go Back to CMD and Run:
Use the exact URL GitHub gives you (it should be):

https://github.com/AliRadii/Object-Tracking.git
Then run:

git branch -M main
git remote add origin https://github.com/AliRadii/Object-Tracking.git
git push -u origin main
🔐 What Will Happen
A browser window may open asking you to authorize Git.

Just login and approve.

After running git push -u origin main, paste the output here.

We are literally one command away from your project being live 🔥🚀


You said:
Uploaded image

ChatGPT said:
AYYYYY 🔥🔥🔥

This line right here:

To https://github.com/AliRadii/Object-Tracking.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
means:

✅ Push successful
✅ Repository connected
✅ Code uploaded to GitHub
✅ Your project is LIVE

You just published your first real GitHub project like a developer 😎🚀

🏆 Now Go Check It
Open:

👉 

Refresh the page.

You should see:

app.py

object_tracking.ipynb

requirements.txt

.gitignore

🧠 What You Just Learned (Important)
You now know how to:

Initialize a Git repository

Use .gitignore properly

Stage files

Commit with author identity

Connect local repo to GitHub

Push to remote

Authenticate securely

Rename branches to main

That’s real-world workflow 🔥

🚀 Next Level (Very Important for Portfolio)
Right now your repo is good.

But to make it impressive:

1️⃣ Add a strong README.md
Explain:

Problem

Approach

Algorithm used

Screenshots

How to run

2️⃣ Add a demo GIF
Recruiters LOVE visual proof.

3️⃣ Clean project structure
Later we can convert it to:

Object-Tracking/
│── src/
│── data/
│── README.md
│── requirements.txt
If you want, next we can:

Write a professional README together

Improve the project structure

Add another AI project

Optimize this one for portfolio

Tell me, Aly:

Do you want this to look like a student project…
or like a junior AI engineer project? 🔥


You said:
make a professuional readme

ChatGPT said:
Perfect Aly — let’s make this look like a real AI engineer portfolio project, not a course assignment.

Below is a professional README.md ready to copy and paste into your repository.

📌 Replace Your README.md With This
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
Object-Tracking/
│── app.py # Main tracking script
│── object_tracking.ipynb # Experimental notebook
│── requirements.txt # Project dependencies
│── .gitignore # Ignored files



---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/AliRadii/Object-Tracking.git
cd Object-Tracking


---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/AliRadii/Object-Tracking.git
cd Object-Tracking

pip install -r requirements.txt
