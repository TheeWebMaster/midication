from colorama import Fore


def is_valid_gender(gender):
  return gender.lower() == 'homme' or gender.lower() == 'femme'


def get_patient_gender():
  gender = ''

  while True:
    print(f'{Fore.LIGHTYELLOW_EX}le sexe doit être homme où femme.{Fore.MAGENTA} (donner 0 pour quitter){Fore.RESET}\n')
    gender = input('sexe: ')

    if gender == '0':
      break
    elif is_valid_gender(gender):
      print(f'{Fore.GREEN}Valide ✓{Fore.RESET}\n')
      break

    print(f'{Fore.RED}SEXE INVALID ✗{Fore.RESET}\n')

  return gender.lower()
