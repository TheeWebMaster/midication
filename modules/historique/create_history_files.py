import os 

def create_history_files():
  ord_files = os.listdir('files/ordonnance')

  for ord_file in ord_files:
    # file_content = open(os.path.join('files/ordonnance',ord_file))
    print(ord_file)