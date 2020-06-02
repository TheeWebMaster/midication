import modules.patient as patient
import modules.rendez_vous as rendezvous
import modules.ordonnance as ordo
import modules.historique as historique
import modules.menu as menu

patient.create_patient_file()
patient.generate_rand_patients()

rendezvous.create_rendezvous_file()
rendezvous.generate_rand_rdvs()

ordo.remove_old_ord_files()
ordo.generate_rand_ords()

historique.clear_prev_history_files()
historique.create_history_files()

print('\n\n')
print('patients, rendervous, ordonnances, historique data has been generated automatically for testing')
print('you can graph data directly or add, remove, update disired data')
print('please check the files/ folder')

while(True):
  menu.show()
  choice = input('please, choose an option: ')
  print('\n')
  if (choice == '0'):
    break
  menu.handle_user_choice(choice)
