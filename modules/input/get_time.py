def is_valid_time_structure(time):
  parts = time.split(':')

  if len(parts) != 2:
    return False
  else:
    if (parts[0].isdigit() and parts[1].isdigit()):
      return True
    else:
      return False


def is_in_range(time):
  hours, minutes = time.split(':')

  return 0 <= int(hours) <= 23 and 0 <= int(minutes) <= 59


def get_time():
  while True:
    time = input('temp hh:min (donner 0 pour quitter) ')

    if time == '0' or is_valid_time_structure(time) and is_in_range(time):
      break

  return time
