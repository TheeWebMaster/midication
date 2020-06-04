def is_registred_rdv(rdv_id, date, time):
  template_rdv = f'{rdv_id};{date};{time};\n'

  rdv_file = open('files/rendezvous.txt', 'r')
  rdvs = rdv_file.readlines()
  rdv_file.close()

  for rdv in rdvs:
    if template_rdv == rdv:
      return True

  return False
