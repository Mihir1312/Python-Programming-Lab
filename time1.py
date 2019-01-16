s=int(input('time in seconds='))
day=s//(24*3600)
s=s%(24*3600)
hour=s//3600
s=s%3600
minute=s//60
sec=s%60
print('The converted time is ')
print('Days =', day,'Hours =', hour,'Minutes =', minute, 'Seconds =', sec)

