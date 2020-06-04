from modules.patient import is_patient, print_patients


def is_valid_id(patient_id):
  return patient_id.isdigit() and len(patient_id) == 8


def get_patient_id_not_existing():
  print_patients()
  patient_id = ''

  while True:
    print('CIN doit être exactement 8 chiffre. (donner 0 pour quitter)')
    patient_id = input('CIN: ')

    if is_patient(patient_id):
      print(f'le CIN {patient_id} existe déjà, svp entrer an nouveau CIN')
    elif is_valid_id(patient_id) or patient_id == '0':
      break

  return patient_id
