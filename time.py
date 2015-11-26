import datetime

def getFiletime(dtms):
  seconds, micros = divmod(dtms, 1000000)
  days, seconds = divmod(seconds, 86400)

  return datetime.datetime(1601, 1, 1) + datetime.timedelta(days, seconds, micros)

print( getFiletime(12989401597150095).strftime( '%a, %d %B %Y %H:%M:%S %Z' ) )
