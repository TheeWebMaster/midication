from random import randint
import names
from .create_ord import create_ord


def get_rand_med():

  medicines = []

  for _ in range(1, randint(2, 6)):
    medicines.append({
        'title': names.get_last_name().upper(),
        'quantity': randint(1, 3),
        'duration': f'{randint(1, 10)}day(s)'
    })

  return medicines


def generate_rand_ords():
  rdv_file = open('files/rendezvous.txt', 'r')
  prev_patient_id = ''

  for rdv in rdv_file.readlines():
    rdv_details = rdv.split(';')
    current_patient_id = rdv_details[0]

    if(prev_patient_id != current_patient_id):
      index = 1

    create_ord(current_patient_id, rdv_details[1], rdv_details[2], get_rand_med(), index)

    prev_patient_id = current_patient_id
    index += 1
