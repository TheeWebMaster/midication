from modules.helper.is_patient import is_patient
from modules.helper.print_patients import print_patients


def is_valid_id(patient_id):
  return patient_id.isdigit() and len(patient_id) == 8


def get_patient_id():
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
