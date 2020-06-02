import os

def create_history_folder():
  if ('historique' not in os.listdir('files/')):
    os.mkdir('files/historique')
