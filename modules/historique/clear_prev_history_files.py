import os 

def clear_prev_history_files():
  history_files = os.listdir('files/historique')

  for history_file in history_files:
    if (history_file != '.gitignore'):
       os.remove(os.path.join('files/historique', history_file))