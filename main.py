import sys
import modules.patient as patient
import modules.rendez_vous as rendezvous
import modules.ordonnance as ordo
import modules.historique as historique

patient.create_patient_file()
patient.generate_rand_patients()

rendezvous.create_rendezvous_file()
rendezvous.generate_rand_rdvs()

ordo.remove_old_ord_files()
ordo.generate_rand_ords()

historique.create_history_files()