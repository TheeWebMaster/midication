def is_valid_gender(gender):
  return gender.lower() == 'homme' or gender.lower() == 'femme'


def get_patient_gender():
  gender = ''

  while not is_valid_gender(gender):
    print('le sexe doit être homme/femme. (donner 0 pour quitter)')
    gender = input('sexe: ')

    if gender == '0':
      break

  return gender
