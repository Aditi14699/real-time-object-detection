# Real-Time Object Detection 🎯

A computer vision project that uses a pre-trained **MobileNet SSD** model to detect objects from a webcam feed in real-time — all wrapped in an interactive **Streamlit** web app. 📹✨

---

## 🧠 Model Used

- **Model**: MobileNet SSD (Single Shot MultiBox Detector)
- **Framework**: OpenCV DNN module
- **Trained On**: Caffe framework
- **Classes**: 20 pre-defined classes (person, dog, car, bottle, etc.)

---

## ⚙️ Tech Stack

- **Python** 
- **OpenCV** – Image processing and model inference
- **Streamlit** – Web-based UI
- **Pre-trained MobileNet SSD** – Object detection
- **Virtualenv** – Environment management

---

## 📂 Project Structure

real-time-object-detection/ 
├── model/ 
│ ├── MobileNetSSD_deploy.caffemodel 
│ └── MobileNetSSD_deploy.prototxt 
├── app.py 
├── requirements.txt 
├── README.md 
└── venv/

---

## 💻 How to Run

1. **Clone this repository**
    ```bash
    git clone https://github.com/Aditi14699/real-time-object-detection.git
    cd real-time-object-detection

2. **Set up virtual environment**
    ```bash
    python -m venv venv
    venv\Scripts\activate        # On Windows
    source venv/bin/activate     # On Mac/Linux

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt

4. **Run the Streamlit app**
    ```bash
    streamlit run app.py

---

📸 Features
- Real-time webcam feed
- Object detection and bounding boxes
- Streamlit interface for easy interaction
- Detects common objects like:
    - Person
    - Dog
    - Cat
    - Car
    - Chair
    - Bottle
    - And more...

---

🔮 Future Improvements
- Add YOLOv8 or Faster R-CNN for improved accuracy
- Option to upload and analyze video/image files
- Display detection confidence scores
- Track objects across frames using object tracking
- Add option to select/deselect classes to detect
- Deploy app using Streamlit Cloud or Hugging Face Spaces

---

📝 Acknowledgements
- OpenCV
- Streamlit
- MobileNet SSD Model (Caffe)

---

🧑‍💻 Author
- Aditi
- LinkedIn: https://www.linkedin.com/in/aditi-patil-52992115b/