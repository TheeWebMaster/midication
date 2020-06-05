from colorama import Fore


def all_digits(*args):
  for arg in args:
    if not arg.isdigit():
      return False

  return True


def in_range(day, month, year):
  return 1 <= int(day) <= 31 and 1 <= int(month) <= 12 and 1800 <= int(year) <= 2020


def is_valid_date(date):
  parts = date.split('/')

  if len(parts) != 3:
    return False
  else:
    if all_digits(parts[0], parts[1], parts[2]) and in_range(parts[0], parts[1], parts[2]):
      return True
    else:
      return False


def get_date():
  while True:
    print(F'{Fore.YELLOW}La date doit être sur la forme suivante: jour/mois/année {Fore.MAGENTA}', end='')
    print(f'(donner 0 pour quitter){Fore.RESET}\n')

    date = input('date: ')

    if date == '0':
      break
    else:
      if is_valid_date(date):
        print(f'{Fore.GREEN}Valide  ✓{Fore.RESET}\n')
        break
      else:
        print(f'{Fore.RED}DATE INVALIDE ✗{Fore.RESET}\n')

  return date
