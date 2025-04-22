import cv2
import streamlit as st
import numpy as np
from PIL import Image

# Load class labels
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant",
           "sheep", "sofa", "train", "tvmonitor"]

# Load pre-trained model
prototxt_path = "model/MobileNetSSD_deploy.prototxt"
model_path = "model/MobileNetSSD_deploy.caffemodel"

net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

st.title("🔍 Real-time Object Detection with Streamlit")
st.markdown("Using MobileNet SSD and OpenCV")

# Start webcam
cap = cv2.VideoCapture(0)

FRAME_WINDOW = st.image([])

st.markdown("Press `Stop` button to end.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        st.warning("Failed to grab frame.")
        break

    # Resize and prepare input
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
                                 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    # Loop over detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])
            label = CLASSES[idx]
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            cv2.rectangle(frame, (startX, startY), (endX, endY),
                          (0, 255, 0), 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(frame, f"{label}: {confidence:.2f}", (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Convert frame to RGB and show in Streamlit
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)

# Cleanup
cap.release()
