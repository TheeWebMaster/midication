from modules.helper.is_patient import is_patient
from modules.patient.print_patients import print_patients


def is_valid_id(patient_id):
  return patient_id.isdigit() and len(patient_id) == 8


def get_patient_id_that_exists():
  print_patients()
  patient_id = ''

  while True:
    print('Le CIN doit être exactement 8 chiffre. (donner 0 pour quitter)')
    patient_id = input('CIN: ')

    if patient_id == '0':
      break
    else:
      if not is_patient(patient_id):
        print(f'le CIN {patient_id} n\'existe pas dans la table des patients. entrer un nouveau CIN')
      elif is_valid_id(patient_id):
        break

  return patient_id
