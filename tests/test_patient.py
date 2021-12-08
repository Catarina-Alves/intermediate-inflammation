"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name


def test_create_doctor():
    from inflammation.models import Doctor

    name = 'Alice'
    doctor = Doctor(name=name)

    assert doctor.name == name


def test_add_patients():
    from inflammation.models import Doctor

    # Names of doctor and patients
    doctor_name = 'Alice'
    patient_1_name = 'Bob'
    patient_2_name = 'Carl'

    # Initialise doctor class and add patients
    doctor = Doctor(name=doctor_name)
    doctor.add_patient(patient_name=patient_1_name)
    doctor.add_patient(patient_name=patient_2_name)

    assert doctor.patients[0].name == 'Bob'
    assert doctor.patients[1].name == 'Carl'


def test_patient_names():
    from inflammation.models import Doctor

    # Names of doctor and patients
    doctor_name = 'Alice'
    patient_1_name = 'Bob'
    patient_2_name = 'Carl'

    # Initialise doctor class and add patients
    doctor = Doctor(name=doctor_name)
    doctor.add_patient(patient_name=patient_1_name)
    doctor.add_patient(patient_name=patient_2_name)

    assert doctor.patient_names == ['Bob', 'Carl']