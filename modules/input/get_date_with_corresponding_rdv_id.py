from colorama import Fore
from modules.rendez_vous import is_matched_rdvid_date, print_rdvs
from .get_date import is_valid_date


def get_date_with_corresponding_rdv_id(rdv_id):
  while True:
    print(f'{Fore.YELLOW}la date doit correspondre avec le CIN {rdv_id}')
    print(F'La date doit être sous la forme suivante: jour/mois/année {Fore.MAGENTA}', end='')
    print(f'(donner 0 pour quitter){Fore.RESET}\n')

    date = input('date: ')

    if date == '0':
      break
    else:
      if not is_valid_date(date):
        print(f'{Fore.RED}DATE INVALIDE ✗{Fore.RESET}\n')
      elif not is_matched_rdvid_date(rdv_id, date):
        print_rdvs()
        print(f'{Fore.RED}il nya aucune correspondance avec CIN {rdv_id} et date {date}{Fore.RESET}\n')
      else:
        print(f'{Fore.GREEN}Valide  ✓{Fore.RESET}\n')
        break

  return date
