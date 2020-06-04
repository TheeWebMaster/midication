from tabulate import tabulate
from modules.helper.construct_table import construct_table


def print_rdvs():
  rdv_file = open('files/rendezvous.txt', 'r')
  rdvs = rdv_file.readlines()

  headers = ['N°', 'CIN', 'date', 'heure']
  table = construct_table(rdvs)

  print('\n-------tables des rendezvous-------')
  print(tabulate(table, headers=headers, showindex="always"), '\n')

  rdv_file.close()
