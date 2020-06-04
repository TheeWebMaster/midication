def filter_patients(patient_id, patients):
  new_patients = []

  for patient in patients:
    if patient_id != patient.split(';')[0]:
      new_patients.append(patient)

  return new_patients


def remove_patient(patient_id):
  patient_file = open('./files/patient.txt', 'r+')
  patients = patient_file.readlines()

  filtered = filter_patients(patient_id, patients)

  if len(filtered) != len(patients):
    patient_file.truncate(0)
    patient_file.seek(0)

    patient_file.writelines(filtered)

  patient_file.close()
