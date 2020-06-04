from random import randint
from .add_rendezvous import add_rendezvous


def get_rand_date():
  return f'{randint(1, 31)}/{randint(1, 12)}/{randint(2010, 2020)}'


def get_rand_time():
  return f'{randint(0, 2)}{randint(0, 3)}:{randint(0, 5)}{randint(0, 9)}'


def generate_rand_rdvs():
  patient_file = open('files/patient.txt', 'r')
  patients = patient_file.readlines()

  for patient in patients:
    patient_id = patient.split(';')[0]
    for _ in range(0, randint(1, 3)):
      add_rendezvous({
          'id': patient_id,
          'date': get_rand_date(),
          'time': get_rand_time()
      })
