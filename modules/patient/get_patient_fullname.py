def get_patient_fullname(rdv_id):
  patient_file = open('files/patient.txt', 'r')
  patients = patient_file.readlines()
  patient_file.close()

  for patient_str in patients:
    patient_details = patient_str.split(';')
    if rdv_id == patient_details[0]:
      return patient_details[1], patient_details[2]
