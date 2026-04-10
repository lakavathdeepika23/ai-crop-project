import streamlit as st
import numpy as np
import cv2
from disease import predict_frame
from soil import get_soil_data, analyze_soil

st.set_page_config(page_title="AI Crop System", layout="centered")
st.title("🌱 AI Crop Disease & Soil Purity Generator")

# Upload Crop Image
uploaded_file = st.file_uploader("Upload Crop Image", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, 1)
    st.image(frame, caption="Uploaded Image", use_column_width=True)

    label, confidence, prevention_crop = predict_frame(frame)
    st.subheader("🌿 Crop Disease Result")
    st.write(f"Prediction: {label}")
    st.write(f"Confidence: {confidence}%")
    st.info(f"Prevention: {prevention_crop}")

# Soil Analysis
st.subheader("🌾 Soil Analysis")
soil_data = get_soil_data()
soil_status, prevention_soil = analyze_soil(soil_data)

st.write(f"Moisture: {soil_data['moisture']}")
st.write(f"pH: {soil_data['ph']}")
st.write(f"Temperature: {soil_data['temperature']}°C")
st.success(soil_status)
st.info(f"Prevention: {prevention_soil}")