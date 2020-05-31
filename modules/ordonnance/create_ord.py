from random import randint


def write(string, ord_file):
  ord_file.write(string + '\n')


def create_ord(id, firstname, lastname, date, time, medecines, i):
  with open(f'files/ordonnance/{firstname}_{lastname}--{i}.txt', 'w') as ord_file:
    headline = f'{id} {firstname} {lastname} {date} {time}'
    write(headline, ord_file)

    for medicine in medecines:
      med = '{} {} {}'.format(medicine['title'], medicine['quantity'], medicine['duration'])
      write(med, ord_file)
