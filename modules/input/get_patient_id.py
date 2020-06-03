def is_valid_id(patient_id):
  return patient_id.isdigit() and len(patient_id) == 8

def get_patient_id():
  patient_id = ''

  while not is_valid_id(patient_id):
    print('CIN doit être exactement 8 chiffre. (donner 0 pour quitter)')
    patient_id = input('CIN: ')

    if patient_id == '0':
      break
  
  return patient_id