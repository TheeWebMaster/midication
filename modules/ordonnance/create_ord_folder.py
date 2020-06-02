import os 

def create_ord_folder():
  if ('ordonnance' not in os.listdir('files/')):
    os.mkdir('files/ordonnance')  