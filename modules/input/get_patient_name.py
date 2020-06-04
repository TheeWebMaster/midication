def is_valid_name(name):
  return name.isalpha()


def get_patient_name(title):
  name = ''

  while not is_valid_name(name):
    print(f'le {title} doit être formé par des caractères alphabetique. (donner 0 pour quitter)')
    name = input(f'{title}: ')

    if name == '0':
      break

  return name
