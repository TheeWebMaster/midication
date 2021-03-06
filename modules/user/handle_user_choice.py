from colorama import Fore
import modules.patient as patient
import modules.rendez_vous as rendezvous
import modules.ordonnance as ordo
import modules.historique as history
import modules.graph as graph
import modules.input as inp


def its_enough(message):
  enough = ''

  while enough.lower() != 'o' and enough.lower() != 'n':
    enough = input(f'\n{Fore.BLUE}{message}{Fore.RESET}')

  return enough.lower() == 'n'


def there_is_zero(*args):
  for arg in args:
    if arg == '0':
      return True

  return False


def add_new_patient():
  patient_id, firstname, lastname, sexe, age = ('', '', '', '', '')

  while True:
    patient_id = inp.get_patient_id_not_existing()

    if patient_id != '0':
      firstname = inp.get_patient_name('nom')

      if firstname != '0':
        lastname = inp.get_patient_name('prenom')

        if lastname != '0':
          sexe = inp.get_patient_gender()

          if sexe != '0':
            age = inp.get_patient_age()

            if age != '0':
              new_patient = {
                  'id': patient_id,
                  'firstname': firstname,
                  'lastname': lastname,
                  'sexe': sexe,
                  'age': age
              }
              patient.add_patient(new_patient)
              patient.print_patients()

              print(f'{Fore.GREEN}le patient "{lastname} {firstname}" ', end='')
              print(f'avec le CIN "{patient_id}" est ajouté avec succès.{Fore.RESET}')

    zero = there_is_zero(patient_id, firstname, lastname, sexe, age)

    if zero or its_enough('tu veux ajouter un autre patient? o/n '):
      break


def delete_patient():
  while True:
    patient_id = inp.get_patient_id_that_exists()

    if patient_id != '0':
      patient.remove_patient(patient_id)
      patient.print_patients()
      print(f'{Fore.GREEN}le patient avec CIN {patient_id} est suprimer avec succès.{Fore.RESET}')

    if there_is_zero(patient_id) or its_enough('supprimer un autre patient? o/n '):
      break


def add_rendezvous():
  patient_id, date, time = '', '', ''

  while True:
    patient_id = inp.get_patient_id_that_exists()

    if patient_id != '0':
      date = inp.get_date()

      if date != '0':
        time = inp.get_time()

        if time != '0':
          new_rdv = {
              'id': patient_id,
              'date': date,
              'time': time
          }

          rendezvous.add_rendezvous(new_rdv)

          rendezvous.print_rdvs()
          print(f'{Fore.GREEN}le renedezous avec les informations suivante {patient_id}, {date}, {time}')
          print('est ajoute avec succès dans la table des rendezvous')
          print(f'voir le dernier ligne de la table{Fore.RESET}')

    if there_is_zero(patient_id, date, time) or its_enough('ajouter un autre rendezvous? o/n '):
      break


def cancel_rendezvous():
  rdv_id, date, time = '', '', ''

  while True:
    rdv_id = inp.get_rdv_id_that_exist()

    if rdv_id != '0':
      date = inp.get_date_with_corresponding_rdv_id(rdv_id)

      if date != '0':
        time = inp.get_time_with_corresponding_rdvid_date(rdv_id, date)

        if time != '0':
          rendezvous.cancel_rendezvous(rdv_id, date, time)
          rendezvous.print_rdvs()

          print(f'{Fore.GREEN}le renedezous avec les informations suivante {rdv_id}, {date}, {time}')
          print(f'est annulé avec succès dans la table des rendezvous{Fore.RESET}')

    if there_is_zero(rdv_id, date, time) or its_enough('annuler un autre rendezvous? o/n '):
      break


def modify_rendezvoud():
  rdv_id, prev_date, prev_time, date, time = '', '', '', '', ''

  while True:
    rendezvous.print_rdvs()
    rdv_id = inp.get_rdv_id_that_exist()

    if rdv_id != '0':
      prev_date = inp.get_date_with_corresponding_rdv_id(rdv_id)

      if prev_date != '0':
        prev_time = inp.get_time_with_corresponding_rdvid_date(rdv_id, prev_date)

        if prev_time != '0':
          print(f'{Fore.YELLOW}donner le nouveau date: {Fore.RESET}')
          date = inp.get_date()

          if date != '0':
            print(f'{Fore.YELLOW}donner le nouveau temp: {Fore.RESET}')
            time = inp.get_time()

            if time != '0':
              rendezvous.modify_rendezvous(
                  rdv_id,
                  {'date': date, 'time': time},
                  {'date': prev_date, 'time': prev_time}
              )

              rendezvous.print_rdvs()
              print(f'{Fore.GREEN}le rendezous avec CIN {rdv_id} est modifier ', end='')
              print(f'par la date {date} et temp {time}.{Fore.RESET}')

    if there_is_zero(rdv_id, prev_date, prev_time, date, time) or its_enough('modifier un autre rendezvous? o/n '):
      break


def create_ord():
  rdv_id, date, time = '', '', ''

  while True:
    rendezvous.print_rdvs()
    rdv_id = inp.get_rdv_id_that_exist()

    if rdv_id != '0':
      date = inp.get_date_with_corresponding_rdv_id(rdv_id)

      if date != '0':
        time = inp.get_time_with_corresponding_rdvid_date(rdv_id, date)

        if time != '0':
          medicines = inp.get_medicines()
          patient_fullname = patient.get_patient_fullname(rdv_id)
          ord_num = ordo.get_ord_num(patient_fullname)

          ordo.create_ord(rdv_id, date, time, medicines, ord_num)

          print(f'{Fore.GREEN}ordonnance crée avec succès.\nconsulter file/ordonnance/', end='')
          print(f'{patient_fullname[0]}_{patient_fullname[1]}_{ord_num}.txt{Fore.RESET}')

          keep_rdv = its_enough('est ce que tu veux supprimer le rendez vous déjà fait? o/n: ')

          if not keep_rdv:
            rendezvous.cancel_rendezvous(rdv_id, date, time)
            rendezvous.print_rdvs()

            print(f'{Fore.MAGENTA}le rendezvous avec les information suivante')
            print(f'{rdv_id}, {date}, {time}')
            print(f'est supprimer dans la table de rendezvous.{Fore.RESET}')

    if there_is_zero(rdv_id, date, time) or its_enough('crée une autre ordonnance? o/n: '):
      break


def handle_user_choice(choice):
  if choice.isdigit():
    if choice == '1':
      add_new_patient()
    elif choice == '2':
      delete_patient()
    elif choice == '3':
      add_rendezvous()
    elif choice == '4':
      cancel_rendezvous()
    elif choice == '5':
      modify_rendezvoud()
    elif choice == '6':
      create_ord()
    elif choice == '7':
      history.create_history_files()
      print('les historique des patients sont crée avec succès.')
      print('cosulter le dossier files/historique/')
    elif choice == '8':
      graph.per_month()
    elif choice == '9':
      graph.per_year()
    else:
      print('choix invalide.')
  else:
    print('choix invalid.')
