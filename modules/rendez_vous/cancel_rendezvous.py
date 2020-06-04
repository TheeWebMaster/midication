from .filter_rendervous import filter_rdvs


def cancel_rendezvous(patient_id, date, time):
  rdv_file = open('files/rendezvous.txt', 'r+')
  rdvs = rdv_file.readlines()

  filterd_rdvs = filter_rdvs(rdvs, patient_id, date, time)

  if len(filterd_rdvs) != len(rdvs):
    rdv_file.truncate(0)
    rdv_file.seek(0)

    rdv_file.writelines(filterd_rdvs)

  rdv_file.close()
