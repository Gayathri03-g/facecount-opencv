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

🚀 Usage
Run the script:
```bash
python face_counter.py
---------------------------------
Webcam will open and detect faces
Count updates every 3s (in console + video feed)
Press q to quit

⚙️ Config (inside code)
``python
FRAME_SCALE = 0.5     # Resize frame for speed
FPS_LIMIT = 10        # Max frames per second
UPDATE_INTERVAL = 3   # Update count every 3 sec


📊 Example Console Output

Updated Face Count: 2
Updated Face Count: 4
Updated Face Count: 3
