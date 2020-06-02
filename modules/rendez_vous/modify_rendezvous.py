def get_index(rdvs, patient_id):
  for (index, rdv) in enumerate(rdvs):
    if (patient_id == rdv.split(';')[0]):
      return index

  return -1


def replace_rdv(rdvs, patient_id, index, timing):
  rdvs[index] = '{};{};{};\n'.format(patient_id, timing['date'], timing['time'])




def modify_rendezvous(patient_id, timing):
  rdv_file = open('files/rendezvous.txt', 'r+')
  rdvs = rdv_file.readlines()

  index_to_replace = get_index(rdvs, patient_id)

  if (index_to_replace >= 0):
    replace_rdv(rdvs, patient_id, index_to_replace, timing)
    rdv_file.truncate(0)
    rdv_file.seek(0)

    rdv_file.writelines(rdvs)
    print('done.')
  else:
    print('desired rendezvous to update not found.')

  rdv_file.close()
