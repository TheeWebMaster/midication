def filter_patients(patient_id, patients):
  return [patient for patient in patients if patient_id not in patient]


def remove_patient(patient_id):
  patient_file = open('./files/patient.txt', 'r+')
  patients = patient_file.readlines()

  filtered = filter_patients(patient_id, patients)

  patient_file.truncate(0)
  patient_file.seek(0)

  patient_file.writelines(filtered)
  patient_file.close()
