def filter_rdvs(rdvs, patient_id, date, time):
  filtered = []
  target = f'{patient_id};{date};{time};'

  for rdv in rdvs:
    if (target not in rdv):
      filtered.append(rdv)

  return filtered


def cancel_rendezvous(patient_id, date, time):
  rdv_file = open('files/rendezvous.txt', 'r+')
  rdvs = rdv_file.readlines()

  filterd_rdvs = filter_rdvs(rdvs, patient_id, date, time)

  if (len(filterd_rdvs) != len(rdvs)):
    rdv_file.truncate(0)
    rdv_file.seek(0)

    rdv_file.writelines(filterd_rdvs)
    print('\ndone.')
  else:
    print(f'\nrendezvous with ID {patient_id} date {date} time {time} already not registered')

  rdv_file.close()
