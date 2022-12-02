import math
import datetime

print('A sphere with a radius of 5 is', 4 / 3 * math.pi * 5 ** 3, 'cubed.\n')

print('The total wholesale cost for 60 copies is ' + '${:.2f}'.format(.40 * 24.95 + 3 + .75 * 59) + '.\n')

start_time = datetime.timedelta(hours=6, minutes=52)
time_change = datetime.timedelta(minutes=8*2+7*3, seconds=15*2+12*3)
end_time = start_time + time_change
print('You get home for breakfast at ' + str(end_time) + 'AM.')
