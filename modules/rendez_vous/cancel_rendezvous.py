def filter_rdvs(rdvs, patient_id):
  filtered = []

  for rdv in rdvs:
    if (patient_id not in rdv.split(';')):
      filtered.append(rdv)

  return filtered


def cancel_rendezvous(patient_id):
  rdv_file = open('files/rendervous.txt', 'r+')
  rdvs = rdv_file.readlines()

  filterd_rdvs = filter_rdvs(rdvs, patient_id)

  rdv_file.truncate(0)
  rdv_file.seek(0)

  rdv_file.writelines(filterd_rdvs)
  rdv_file.close()
