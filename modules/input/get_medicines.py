from colorama import Fore


def error_message(message):
  print(f'{Fore.RED}{message}{Fore.RESET}\n')


def get_med_num(title):
  while True:
    num = input(f'{Fore.MAGENTA}donner le {title} des medicaments: {Fore.RESET}')

    if num.isdigit() and int(num) > 0:
      break
    else:
      error_message(f'le {title} des médicaments doit être un entier positive')

  return int(num)


def get_med_title():
  while True:
    title = input(f'{Fore.MAGENTA}donner le nom du médicament: {Fore.RESET}')

    if title.isalpha():
      break
    else:
      error_message('le nom doit contenir des charactere alphabetique seulement')

  return title


def get_medicines():
  med = []
  num = get_med_num('nombre')
  print('\n')

  for i in range(0, num):
    print(f'{Fore.BLUE}médicament N°{i + 1}{Fore.RESET}')

    med.append({
        'title': get_med_title(),
        'quantity': get_med_num('quantite'),
        'duration': get_med_num('durée')
    })

    print('\n')

  return med
