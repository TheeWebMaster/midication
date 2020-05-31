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


def extract_fullname(patient):
  patient_detail = patient.split(';')

  return patient_detail[1], patient_detail[2]


def get_corresponding_patient_fullname(patient_id):
  patient_file = open('files/patient.txt', 'r')

  for patient in patient_file.readlines():
    if (patient_id in patient):
      return extract_fullname(patient)


def generate_rand_ords():
  rdv_file = open('files/rendervous.txt', 'r')
  prev_latname = ''

  for rdv in rdv_file.readlines():
    rdv_details = rdv.split(';')
    firstname, lastname = get_corresponding_patient_fullname(rdv_details[0])

    if(prev_latname != lastname):
      index = 1

    create_ord(rdv_details[0], firstname, lastname, rdv_details[1], rdv_details[2], get_rand_med(), index)

    prev_latname = lastname
    index += 1
