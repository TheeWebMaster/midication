def get_ordlistname_without_underscore(ords):
  ord_no_num = []

  for ordonnance in ords:
    ord_no_num.append(ordonnance[:ordonnance.rindex('_')])

  return ord_no_num
