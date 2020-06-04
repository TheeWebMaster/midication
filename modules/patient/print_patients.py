from tabulate import tabulate
from modules.helper.construct_table import construct_table


def print_patients():
  patient_file = open('files/patient.txt', 'r')
  patients = patient_file.readlines()

  headers = ['N°', 'CIN', 'nom', 'prenom', 'sexe', 'age']

  table = construct_table(patients)
  print('\n---------------tables des patients----------------')
  print(tabulate(table, headers=headers, showindex="always"), '\n')

  patient_file.close()
