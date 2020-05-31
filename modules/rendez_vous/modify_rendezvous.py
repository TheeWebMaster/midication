def getIndex(rdvs, patient_id):
  for (index, rdv) in enumerate(rdvs):
    if (patient_id in rdv.split(';')):
      return index


def replace_rdv(rdvs, patient_id, timing):
  index = getIndex(rdvs, patient_id)
  rdvs[index] = '{};{};{};\n'.format(
      patient_id, timing['date'], timing['time'])


def modify_rendezvous(patient_id, timing):
  rdv_file = open('files/rendervous.txt', 'r+')
  rdvs = rdv_file.readlines()

  replace_rdv(rdvs, patient_id, timing)

  rdv_file.truncate(0)
  rdv_file.seek(0)

  rdv_file.writelines(rdvs)
  rdv_file.close()
