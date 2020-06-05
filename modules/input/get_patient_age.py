from colorama import Fore


def is_valid_age(age):
  return age.isdigit() and int(age) > 0


def get_patient_age():
  age = ''

  while True:
    print(f'{Fore.LIGHTYELLOW_EX}l\'âge doit être un entier positive. (donner 0 pour quitter){Fore.RESET}\n')
    age = input('âge: ')
    print('\n')

    if age == '0' or is_valid_age(age):
      break

    print(f'{Fore.RED}AGE INVALIDE!{Fore.RESET}\n')

  return age
