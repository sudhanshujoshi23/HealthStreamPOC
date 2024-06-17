from utils.generate_health_data import simulate_health_data


def test_simulate_health_data():
    patient_id = "ch102"
    data = simulate_health_data(patient_id)
    assert type(data) == type(dict())
    assert data.get('patient_id')
    assert data.get('heart_rate')
    assert data.get('blood_pressure')
    assert data.get('body_temperature')
    assert data.get('blood_SpO2')
    assert data.get('time')