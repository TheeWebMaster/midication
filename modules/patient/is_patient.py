def is_patient(patient_id):
  patient_file = open('files/patient.txt', 'r')
  patients = patient_file.readlines()
  patient_file.close()

  for patient in patients:
    if patient_id == patient.split(';')[0]:
      return True

  return False
