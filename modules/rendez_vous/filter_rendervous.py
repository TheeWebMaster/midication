def filter_rdvs(rdvs, patient_id, date, time):
  filtered = []
  target = f'{patient_id};{date};{time};'

  for rdv in rdvs:
    if (target not in rdv):
      filtered.append(rdv)

  return filtered