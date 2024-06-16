from datetime import datetime
import random

def simulate_health_data(patient_id):
    return {
            "patient_id": f"{patient_id}_0000{random.randint(1,5)}",
            "heart_rate": random.randint(60, 100),
            "blood_pressure": f"{random.randint(110, 130)}/{random.randint(70, 90)}",
            "body_temperature": round(random.uniform(36.0, 37.5), 1),
            "blood_SpO2": random.randint(95,99),
            "time": datetime.now().isoformat()
        }

