import modules.patient as patient
import modules.rendez_vous as rendezvous
import modules.ordonnance as ordo
import modules.historique as historique
import modules.graph as graph
import modules.menu as menu

patient.create_patient_file()
patient.generate_rand_patients()

rendezvous.create_rendezvous_file()
rendezvous.generate_rand_rdvs()

ordo.remove_old_ord_files()
ordo.generate_rand_ords()

historique.clear_prev_history_files()
historique.create_history_files()

print('\033[92mpatients, rendervous, ordonnances, historique data has been generated automatically for testing\033[0m')
print('\033[92myou can graph data directly or add, remove, update disired data\033[0m')
print('\033[94mplease check the files/ folder\033[0m')

while(True):
  menu.show()
  choice = input('\033[93mplease, choose an option: \033[0m')
  if (choice == '0'):
    break
  menu.handle_user_choice(choice)
