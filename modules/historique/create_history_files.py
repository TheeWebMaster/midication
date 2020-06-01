import os 

def add_one_history(history_file, current_ord_file):
  history_file.writelines(current_ord_file.readlines())
  history_file.write(f'------------------------------\n')

def create_history_files():
  ord_files = os.listdir('files/ordonnance')
  prev_patient_fullname = ''

  for ord_file in ord_files:
    current_patient_fullname = ord_file[:-6]
    current_ord_file = open(os.path.join('files/ordonnance', ord_file), 'r')
   
    if (prev_patient_fullname != current_patient_fullname):
      history_file = open(f'files/historique/{current_patient_fullname}.txt', 'w')
 
    add_one_history(history_file, current_ord_file)

    prev_patient_fullname = current_patient_fullname