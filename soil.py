import random

def get_soil_data():
    soil_moisture = random.randint(30, 80)
    soil_ph = round(random.uniform(5.5, 7.5), 2)
    temperature = random.randint(20, 35)

    return {
        "moisture": soil_moisture,
        "ph": soil_ph,
        "temperature": temperature
    }

def analyze_soil(data):
    if data["moisture"] < 40:
        status = "Dry Soil ⚠️ - Needs Water"
        prevention = "Water the soil immediately; consider drip irrigation."
    elif data["moisture"] > 70:
        status = "Too Wet ❌"
        prevention = "Avoid overwatering; improve drainage."
    else:
        status = "Healthy Soil 🌱"
        prevention = "Maintain current soil care."

    return status, prevention