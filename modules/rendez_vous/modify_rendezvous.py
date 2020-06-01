def getIndex(rdvs, patient_id):
  for (index, rdv) in enumerate(rdvs):
    if (patient_id == rdv.split(';')[0]):
      return index

  return False


def replace_rdv(rdvs, patient_id, timing):
  index = getIndex(rdvs, patient_id)

  if (index >= 0 and index != False) :
    rdvs[index] = '{};{};{};\n'.format(patient_id, timing['date'], timing['time'])
    return True
  else:
    print('desired rendezvous to update not found.')
    return False



def modify_rendezvous(patient_id, timing):
  rdv_file = open('files/rendezvous.txt', 'r+')
  rdvs = rdv_file.readlines()

  found = replace_rdv(rdvs, patient_id, timing)

  if (found):
    rdv_file.truncate(0)
    rdv_file.seek(0)

    rdv_file.writelines(rdvs)
    print('done.')
  else:
    print('not found')

  rdv_file.close()
