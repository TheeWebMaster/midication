def add_patient(patient):
  patient_file = open('./files/patient.txt', 'a')
  patient_str_info = ''

  for value in patient.values():
    patient_str_info += str(value) + ';'

  patient_file.write(patient_str_info + '\n')
  patient_file.close()
