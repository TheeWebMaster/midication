import os


def add_one_history(history_file, current_ord_file):
  history_file.writelines(current_ord_file.readlines())
  history_file.write('------------------------------\n')


def count(ord_files):
  temp = ord_files.copy()
  mapping = {}

  for i in range(len(temp)):
    temp[i] = temp[i][:-6]

  for patient in temp:
    if patient not in mapping.keys():
      mapping[patient] = temp.count(patient)

  return mapping


def create_history_files():
  ord_files = os.listdir('files/ordonnance')
  mapping = count(ord_files)

  prev_patient = ''

  for ord_file in ord_files:
    current_patient = ord_file[:-6]
    current_ord_file = open(f'files/ordonnance/{ord_file}', 'r')

    if current_patient != prev_patient:
      counter = 1
      current_patient_history_file = open(f'files/historique/{current_patient}.txt', 'w')

    add_one_history(current_patient_history_file, current_ord_file)

    if counter == mapping[current_patient]:
      current_patient_history_file.close()

    prev_patient = current_patient
    counter += 1
    current_ord_file.close()
