# 🧑‍💻 Real-Time Face Counter (OpenCV + Dlib)

A Python project that detects faces from a webcam feed and updates the **face count every 3 seconds** using OpenCV and Dlib.  
The system displays bounding boxes on detected faces and shows the total count both on the video window and in the console.

---

## 📌 Features
- Real-time face detection with **dlib**  
- Bounding boxes & labels on faces  
- Face count updates every **3 seconds**  
- Console + on-screen face count  
- Optimized with **threading** and **FPS control**

---

## 🛠️ Requirements
- Python **3.10 or 3.11** (⚠️ `dlib` doesn’t support 3.12+)  
- Install dependencies:

```bash
pip install opencv-python dlib numpy
