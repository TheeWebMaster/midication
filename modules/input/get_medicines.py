def get_medicines():
  med = []
  num = ''
  while not num.isdigit():
    num = input('enter le nombre des medicaments: ')

  for _ in range(0, int(num)):
    med.append({
        'title': input('nom du medicament: '),
        'quantity': input('quantite du medicament: '),
        'duration': input('duration du medicament: ')
    })

  return med
