def filter_rdvs(rdvs, patient_id):
  filtered = []

  for rdv in rdvs:
    if (patient_id != rdv.split(';')[0]):
      filtered.append(rdv)

  return filtered


def cancel_rendezvous(patient_id):
  rdv_file = open('files/rendezvous.txt', 'r+')
  rdvs = rdv_file.readlines()

  filterd_rdvs = filter_rdvs(rdvs, patient_id)

  if (len(filterd_rdvs) != len(rdvs)):
    rdv_file.truncate(0)
    rdv_file.seek(0)

    rdv_file.writelines(filterd_rdvs)
    print('\033[92mdone.\033[0m')
  else:
    print(f'rendezvous with ID {patient_id} already not registered')

  rdv_file.close()
