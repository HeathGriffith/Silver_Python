'''
(city_from, city_to, travel time)
loop to check how many lead to Rome; calculate average flight time:
output form: "{} connections lead to Rome with an average flight time of {} minutes"
'''

connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
'''
Rome_flight =[]
length =[]
for data in connections:
    if data[1] == "Rome":
            Rome_flight.append(data)
Rome_quantity = len(Rome_flight)
for min in Rome_flight:
    length.append(min[2])
avg_length = sum(length)/len(length)
print(f"{Rome_quantity} connections lead to Rome with an average flight time of {avg_length} minutes")


# Efficient solution
counter = 0
sum = 0.0
 
for con in connections:
    if con[1] == 'Rome':
        counter += 1
        sum += con[2]
 
print(counter, 'connections lead to Rome with an average flight time of', sum/counter, 'minutes')
'''