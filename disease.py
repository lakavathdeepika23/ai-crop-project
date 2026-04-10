import numpy as np
import cv2

def predict_frame(frame):
    # Simple AI logic (simulated)
    mean_color = np.mean(frame)

    if mean_color < 85:
        label = "Healthy Crop 🌱"
        confidence = 92
        prevention = "Maintain current care; ensure regular watering."
    elif mean_color < 170:
        label = "Mild Disease ⚠️"
        confidence = 75
        prevention = "Apply mild pesticide; increase sunlight exposure."
    else:
        label = "Severe Disease ❌"
        confidence = 88
        prevention = "Use strong pesticide; remove affected leaves immediately."

    return label, confidence, prevention