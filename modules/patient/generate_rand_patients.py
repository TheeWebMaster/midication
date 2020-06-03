from .add_patient import add_patient
from random import randint
import names

sexes = ['male', 'female']


def get_rand_sexe():
  return sexes[randint(0, 1)]


def generate_rand_patients():
  for _ in range(10):
    sexe = get_rand_sexe()
    patient = {
        'id': randint(10000000, 99999999),
        'name': names.get_first_name(gender=sexe),
        'surname': names.get_last_name(),
        'sexe': sexe,
        'age': randint(9, 99)
    }
    add_patient(patient)
