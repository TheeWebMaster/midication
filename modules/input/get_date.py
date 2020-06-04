def all_digits(*args):
  for arg in args:
    if not arg.isdigit():
      return False

  return True


def in_range(day, month, year):
  return 1 <= int(day) <= 31 and 1 <= int(month) <= 12 and int(year) >= 1400


def is_valid_date(date):
  parts = date.split('/')

  if len(parts) != 3:
    return False
  else:
    if all_digits(parts[0], parts[1], parts[2]) and in_range(parts[0], parts[1], parts[2]):
      return True
    else:
      return False


def get_date():
  while True:
    date = input('date jour/mois/année: (donner 0 pour quitter) ')

    if date == '0' or is_valid_date(date):
      break
    else:
      print('DATE INVALIDE')

  return date
