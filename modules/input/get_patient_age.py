def is_valid_age(age):
  return age.isdigit() and int(age) > 0

def get_patient_age():
  age = ''

  while not is_valid_age(age):
    print('l\'âge doit être un entier positive. (donner 0 pour quitter)')
    age = input('âge: ')

    if age == '0':
      break

  return age