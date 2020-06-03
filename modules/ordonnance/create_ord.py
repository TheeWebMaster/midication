from random import randint
from modules.helper.is_patient import is_patient

def write_tofile(string, ord_file):
  ord_file.write(string + '\n')


def extract_fullname(patient):
  patient_detail = patient.split(';')

  return patient_detail[1], patient_detail[2]


def get_corresponding_patient_fullname(patient_id):
  patient_file = open('files/patient.txt', 'r')
  patients = patient_file.readlines()
  patient_file.close()

  for patient in patients:
    if (patient_id == patient.split(';')[0]):
      return extract_fullname(patient)


def create_ord(patient_id, date, time, medecines, i):

  if (is_patient(patient_id)):
    firstname, lastname = get_corresponding_patient_fullname(patient_id)
    ord_file = open(f'files/ordonnance/{firstname}_{lastname}_{i}.txt', 'w')
    headline = f'{patient_id} {firstname} {lastname} {date} {time}'

    write_tofile(headline, ord_file)

    for medicine in medecines:
      med = '{} {} {}'.format(medicine['title'], medicine['quantity'], medicine['duration'])
      write_tofile(med, ord_file)

    ord_file.close()
    return True
  else:
    return False
