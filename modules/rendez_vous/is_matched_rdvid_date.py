def is_matched_rdvid_date(rdv_id, date):
  rdv_file = open('files/rendezvous.txt', 'r')
  rdvs = rdv_file.readlines()

  for rdv in rdvs:
    rdv_details = rdv.split(';')

    if rdv_id == rdv_details[0] and date == rdv_details[1]:
      return True

  return False
