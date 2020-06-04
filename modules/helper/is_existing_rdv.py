def is_existing_rdv(rdv_id):
  rdv_file = open('files/rendezvous.txt', 'r')
  rdvs = rdv_file.readlines()

  for rdv in rdvs:
    if rdv_id == rdv.split(';')[0]:
      return True

  return False
