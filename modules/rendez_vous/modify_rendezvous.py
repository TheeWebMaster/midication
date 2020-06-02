def get_index(rdvs, patient_id, prev_timing):
  target = '{};{};{};\n'.format(patient_id, prev_timing['date'], prev_timing['time'])

  for (index, rdv) in enumerate(rdvs):
    if (target == rdv):
      return index

  return -1


def replace_rdv(rdvs, patient_id, index, new_timing):
  rdvs[index] = '{};{};{};\n'.format(patient_id, new_timing['date'], new_timing['time'])


def modify_rendezvous(patient_id, new_timing, prev_timing):
  rdv_file = open('files/rendezvous.txt', 'r+')
  rdvs = rdv_file.readlines()

  index_to_replace = get_index(rdvs, patient_id, prev_timing)

  if (index_to_replace >= 0):
    replace_rdv(rdvs, patient_id, index_to_replace, new_timing)
    rdv_file.truncate(0)
    rdv_file.seek(0)

    rdv_file.writelines(rdvs)
    print('\ndone.')
  else:
    print('\ndesired rendezvous to update not found.')

  rdv_file.close()
