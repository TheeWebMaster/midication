from colorama import Fore


def is_valid_gender(gender):
  return gender.lower() == 'homme' or gender.lower() == 'femme'


def get_patient_gender():
  gender = ''

  while True:
    print(f'{Fore.LIGHTYELLOW_EX}le sexe doit être homme/femme. (donner 0 pour quitter){Fore.RESET}\n')
    gender = input('sexe: ')
    print('\n')

    if gender == '0' or is_valid_gender(gender):
      break

    print(f'{Fore.RED}SEXE INVALID!{Fore.RESET}\n')

  return gender
