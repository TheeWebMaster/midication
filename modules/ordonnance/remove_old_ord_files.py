import os


def remove_old_ord_files():
  for ordo in os.listdir('files/ordonnance'):
    if (ordo != '.gitignore'):
      os.remove(os.path.join('files/ordonnance', ordo))