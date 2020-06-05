import os
from .get_ordlistname_without_underscore import get_ordlistname_without_underscore


def get_ord_num(patient_fullname):
  ords = os.listdir('files/ordonnance')
  ords_no_num = get_ordlistname_without_underscore(ords)
  underscore_name = f'{patient_fullname[0]}_{patient_fullname[1]}'

  return ords_no_num.count(underscore_name) + 1
