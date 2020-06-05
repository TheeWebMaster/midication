from colorama import Fore


def is_valid_time_structure(time):
  parts = time.split(':')

  if len(parts) != 2:
    return False
  else:
    if (parts[0].isdigit() and parts[1].isdigit()):
      return True
    else:
      return False


def is_in_range(time):
  hours, minutes = time.split(':')

  return 0 <= int(hours) <= 23 and 0 <= int(minutes) <= 59


def is_valid_time(time):
  return is_valid_time_structure(time) and is_in_range(time)


def get_time():
  while True:
    print(f'{Fore.YELLOW}le temp doit être sur la forme suivate:', end='')
    print(f' heure:minute{Fore.MAGENTA} (donner 0 pour quitter){Fore.RESET}\n')
    time = input('temp: ')

    if time == '0':
      break
    elif is_valid_time(time):
      print(f'{Fore.GREEN}Valide ✓{Fore.RESET}\n')
      break

    print(f'{Fore.RED}TEMP INVALIDE ✗{Fore.RESET}\n')

  return time
