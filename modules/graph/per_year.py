from .get_all_dates import get_all_dates
from matplotlib import pyplot as plt


def get_years(dates):
  years = []

  for date in dates:
    years.append(date.split('/')[2])

  return years

def draw(year_mapping):

  years = list(year_mapping.keys())
  int_years = [int(year) for year in years]
  int_years.sort()
  
  times = [year_mapping[str(year)] for year in int_years]

  plt.plot(int_years, times, label='consultations/année')



  plt.title('nombre des consultations pour chaque année')
  plt.legend()

  plt.xlabel('années')
  plt.ylabel('nombre des consultations')

  plt.legend()

  plt.show()

def per_year():
  dates = get_all_dates()
  years = get_years(dates)

  year_mapping = {}
  for year in years:
    if( year not in year_mapping.keys()):
      year_mapping[year] = 1
    else:
     year_mapping[year] += 1

  draw(year_mapping)