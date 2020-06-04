import os
from modules.patient.get_patient_fullname import get_patient_fullname


def get_ords_no_num(ords):
  ord_no_num = []

  for ordonnance in ords:
    ord_no_num.append(ordonnance[:ordonnance.rindex('_')])

  return ord_no_num


def get_ord_num(patient_id):
  patient_fullname = get_patient_fullname(patient_id)

  ords = os.listdir('files/ordonnance')
  ords_no_num = get_ords_no_num(ords)
  underscore_name = f'{patient_fullname[0]}_{patient_fullname[1]}'

  return ords_no_num.count(underscore_name) + 1
