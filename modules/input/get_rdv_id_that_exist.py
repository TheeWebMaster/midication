from modules.rendez_vous import is_existing_rdv, print_rdvs


def is_valid_id(rdv_id):
  return rdv_id.isdigit() and len(rdv_id) == 8


def get_rdv_id_that_exist():
  print_rdvs()
  rdv_id = ''

  while True:
    print('Le CIN de rendezvous doit être exactement 8 chiffre. (donner 0 pour quitter)')
    rdv_id = input('CIN: ')

    if rdv_id == '0':
      break
    else:
      if not is_existing_rdv(rdv_id):
        print(f'le CIN {rdv_id} n\'existe pas dans la table des rendezvous. entrer un nouveau CIN')
      elif is_valid_id(rdv_id):
        break

  return rdv_id
