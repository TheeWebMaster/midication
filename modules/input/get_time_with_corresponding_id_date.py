from colorama import Fore
from modules.rendez_vous import is_registred_rdv, print_rdvs
from .get_time import is_valid_time


def get_time_with_corresponding_id_date(rdv_id, date):
  while True:
    print(f'{Fore.YELLOW}le temp doit correspondre avec le CIN {rdv_id} et la date {date}')
    print(f'{Fore.YELLOW}le temp doit être sur la forme suivate:', end='')
    print(f' heure:minute{Fore.MAGENTA} (donner 0 pour quitter){Fore.RESET}\n')
    time = input('temp: ')

    if time == '0':
      break
    else:
      if not is_valid_time(time):
        print(f'{Fore.RED}DATE INVALIDE ✗{Fore.RESET}\n')
      elif not is_registred_rdv(rdv_id, date, time):
        print_rdvs()
        print(f'{Fore.RED}il nya aucune correspondance avec CIN {rdv_id}, date {date} et temp {time}{Fore.RESET}\n')
      else:
        print(f'{Fore.GREEN}Valide ✓{Fore.RESET}\n')
        break

  return time
