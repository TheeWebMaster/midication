from colorama import Fore
from modules.rendez_vous import is_existing_rdv, print_rdvs


def is_valid_id(rdv_id):
  return rdv_id.isdigit() and len(rdv_id) == 8


def get_rdv_id_that_exist():
  print_rdvs()
  rdv_id = ''

  while True:
    print(f'{Fore.YELLOW}le CIN doit être existant dans la table des rendezous.')
    print(F'de plus doit être exactement 8 chiffre.{Fore.MAGENTA} (donner 0 pour quitter){Fore.RESET}\n')
    rdv_id = input('CIN: ')

    if rdv_id == '0':
      break
    else:
      if not is_valid_id(rdv_id):
        print_rdvs()
        print(f'{Fore.RED}CIN INVALIDE ✗{Fore.RESET}\n')
      elif not is_existing_rdv(rdv_id):
        print_rdvs()
        print(f'{Fore.RED}le CIN {rdv_id} n\'existe pas dans la table des rendezvous. Entrer un nouveau CIN\n{Fore.RESET}')
      else:
        print(f'{Fore.GREEN}Valide ✓{Fore.RESET}\n')
        break

  return rdv_id
