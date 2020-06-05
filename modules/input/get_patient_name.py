from colorama import Fore


def is_valid_name(name):
  return name.isalpha()


def get_patient_name(title):
  name = ''

  while True:
    print(f'{Fore.YELLOW}le {title} doit être formé par des caractères alphabetique.', end='')
    print(f'{Fore.MAGENTA} (donner 0 pour quitter){Fore.RESET}\n')

    name = input(f'{title}: ')
    print('\n')

    if name == '0' or is_valid_name(name):
      break

    print(f'{Fore.RED}{title.upper()} INVALIDE!{Fore.RESET}\n')

  return name
