import modules.patient as patient
import modules.rendez_vous as rendezvous
import modules.ordonnance as ordo
import modules.historique as history
import modules.graph as graph
import modules.input as inp
from modules.helper.print_patients import print_patients


def done():
  print('\ndone.')


def wrong_inputs():
  print('\nwrong input(s).')


def patient_404(patient_id):
  print(f'\nthe patient with CIN {patient_id} does not exist in the patient registry')


def is_valid_date(date):
  parts = date.split('/')

  if len(parts) != 3:
    return False
  else:
    if (parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
      return True
    else:
      return False


def is_valid_time(time):
  parts = time.split(':')

  if len(parts) != 2:
    return False
  else:
    if (parts[0].isdigit() and parts[1].isdigit()):
      return True
    else:
      return False


def is_valid_gender(gender):
  return gender == 'homme' or gender == 'femme'


def get_medicines():
  med = []
  num = ''
  while not num.isdigit():
    num = input('enter le nombre des medicaments: ')

  for _ in range(0, int(num)):
    med.append({
        'title': input('nom du medicament: '),
        'quantity': input('quantite du medicament: '),
        'duration': input('duration du medicament: ')
    })

  return med


def add_new_patient():
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
            print_patients()
            done()


def delete_patient():
  patient_id = inp.get_patient_id_that_exists()

  if patient_id != '0':
    patient.remove_patient(patient_id)
    print_patients()
    print(f'le patient avec CIN {patient_id} est suprimer avec succès')


def add_rendezvous():
  patient_id = input('CIN: ')
  date = input('date jour/mois/annee: ')
  time = input('temp hh:min ')

  if(patient_id.isdigit() and is_valid_date(date) and is_valid_time(time)):
    new_rdv = {
        'id': patient_id,
        'date': date,
        'time': time
    }
    allgood = rendezvous.add_rendezvous(new_rdv)

    if allgood:
      done()
    else:
      patient_404(patient_id)
  else:
    wrong_inputs()


def cancel_rendezvous():
  patient_id = input('donner le CIN de rendezvous a annule: ')
  date = input('donner la date de rendezvous a annule: jour/mois/annee ')
  time = input('donner l\'heure de rendezvous a annule: hh:min ')

  if (patient_id.isdigit() and is_valid_date(date) and is_valid_time(time)):
    is_allgood = rendezvous.cancel_rendezvous(patient_id, date, time)

    if is_allgood:
      done()
    else:
      print(f'\nrendezvous with ID {patient_id} date {date} time {time} already not registered')

  else:
    print('wrong CIN')


def modify_rendezvoud():
  patient_id = input('donner le CIN de rendezvous a modifier: ')
  prev_date = input('donner la date de rendezvous a annule: jour/mois/annee ')
  prev_time = input('donner l\'heure de rendezvous a annule: hh:min ')

  date = input('donner le nouveau date jour/mois/annee: ')
  time = input('donner le nouveau temp hh:min ')

  if patient_id.isdigit() and is_valid_date(date) and is_valid_time(time) and is_valid_date(prev_date) and is_valid_time(prev_time):
    is_allgood = rendezvous.modify_rendezvous(
        patient_id,
        {'date': date, 'time': time},
        {'date': prev_date, 'time': prev_time}
    )

    if is_allgood:
      done()
    else:
      print('\ndesired rendezvous to update not found.')
  else:
    wrong_inputs()


def create_ord():
  patient_id = input('CIN: ')
  date = input('date jour/mois/annee: ')
  time = input('temp hh:min ')

  medicines = get_medicines()

  if patient_id.isdigit() and is_valid_date(date) and is_valid_time(time):
    is_allgood = ordo.create_ord(patient_id, date, time, medicines, 1)

    if is_allgood:
      done()
    else:
      print(f'\nno corresponding patient with CIN {patient_id}')
  else:
    wrong_inputs()


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
      done()
    elif choice == '8':
      graph.per_month()
    elif choice == '9':
      graph.per_year()
    else:
      print('choix invalide.')
  else:
    print('choix invalid.')
