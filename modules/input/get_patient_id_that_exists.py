from colorama import Fore
from modules.patient import is_patient, print_patients


def is_valid_id(patient_id):
  return patient_id.isdigit() and len(patient_id) == 8


def get_patient_id_that_exists():
  print_patients()
  patient_id = ''

  while True:
    print(f'{Fore.YELLOW}le CIN doit être existant dans la table des patients.')
    print(F'de plus doit être exactement 8 chiffre.{Fore.MAGENTA} (donner 0 pour quitter){Fore.RESET}\n')
    patient_id = input('CIN: ')

    if patient_id == '0':
      break
    else:
      if not is_valid_id(patient_id):
        print_patients()
        print(f'{Fore.RED}CIN \'{patient_id}\' INVALIDE ✗{Fore.RESET}\n')
      elif not is_patient(patient_id):
        print_patients()
        print(f'{Fore.RED}le CIN {patient_id} n\'existe pas dans la table des patients. entrer un nouveau CIN{Fore.RESET}\n')
      else:
        print(f'{Fore.GREEN}Valide  ✓{Fore.RESET}\n')
        break

  return patient_id
