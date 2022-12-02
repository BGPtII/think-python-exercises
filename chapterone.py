time_to_seconds = 42 * 60 + 42
print('There are', time_to_seconds, 'seconds in 42 minutes and 42 seconds.\n')

dist_to_miles = 10 / 1.61
print('There are', dist_to_miles, 'miles in 10 kilometers.\n')

print('You ran a 10 kilometer race in 42 minutes and 42 seconds...')
print('Your average pace in minutes is:', time_to_seconds/dist_to_miles / 60, 'minutes per mile.')
print('Your average pace in seconds is:', time_to_seconds/dist_to_miles, 'seconds per mile.')
average_speed = dist_to_miles/(time_to_seconds/60/60)
print('Your average speed is:', average_speed, 'miles per hour.')
