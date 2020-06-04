def get_all_dates():
  rdv_file = open('files/rendezvous.txt', 'r')

  dates = []

  for rdv in rdv_file.readlines():
    dates.append(rdv.split(';')[1])

  rdv_file.close()

  return dates
