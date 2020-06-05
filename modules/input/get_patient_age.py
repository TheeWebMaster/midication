from colorama import Fore


def is_valid_age(age):
  return age.isdigit() and int(age) > 0


def get_patient_age():
  age = ''

  while True:
    print(f'{Fore.LIGHTYELLOW_EX}l\'âge doit être un entier positive.{Fore.MAGENTA} (donner 0 pour quitter){Fore.RESET}\n')
    age = input('âge: ')

    if age == '0':
      break
    elif is_valid_age(age):
      print(f'{Fore.GREEN}Valide ✓{Fore.RESET}\n')
      break

    print(f'{Fore.RED}AGE INVALIDE ✗{Fore.RESET}\n')

  return age
