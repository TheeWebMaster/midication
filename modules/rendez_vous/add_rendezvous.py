from modules.helper.is_patient import is_patient


def get_rdv_str(rendezvous_infos):
  rdv_details = ''

  for info in rendezvous_infos.values():
    rdv_details += f'{info};'

  return rdv_details


def add_rendezvous(rendezvous_infos):
  patient_id = rendezvous_infos['id']

  if is_patient(patient_id):
    rendervous_file = open('./files/rendezvous.txt', 'a')
    rdv_str = get_rdv_str(rendezvous_infos)

    rendervous_file.write(rdv_str + '\n')
    rendervous_file.close()
