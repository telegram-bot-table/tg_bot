import time


def date_valid(date):
    try:
      valid_date = time.strptime(date, '%Y-%m-%d')
      return True
    except ValueError:
      return False
      
      

