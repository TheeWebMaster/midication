from matplotlib import pyplot as plt
from .get_all_dates import get_all_dates


def get_months(dates):
  months = []

  for date in dates:
    months.append(date.split('/')[1])

  return months


def draw(month_nbr):
  x_values = [i for i in range(1, 13)]

  plt.plot(x_values, month_nbr, label='consultations/mois')

  plt.title('nombre des consultations pour chaque mois')

  plt.xlabel('mois')
  plt.ylabel('nombre des consultations')

  plt.legend()

  plt.show()


def per_month():
  dates = get_all_dates()
  months = get_months(dates)

  month_nbr = [i for i in range(12)]

  for i in range(12):
    month_nbr[i] = 0
    for month in months:
      if int(month) == i + 1:
        month_nbr[i] += 1

  draw(month_nbr)
