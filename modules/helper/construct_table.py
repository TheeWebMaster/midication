def construct_table(patients):
  table = []

  for patient in patients:
    patient = patient.strip()
    patient = patient.split(';')
    patient.pop(-1)

    table.append(patient)

  return table
