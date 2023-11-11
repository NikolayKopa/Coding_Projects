flight_costs_city = {'Charlotte':183,'Tampa':220,'Pittsburgh':222,'Los Angeles':475}
def hotel_cost(no_of_nights):
   return no_of_nights*140
def flight_cost(city):
   if city in flight_costs_city:
       return flight_costs_city[city]
   else:
       return 250
def rental_car_cost(days):
   total_cost = days*40
   if days >= 7:
       total_cost -= 50
   elif days >= 3:
       total_cost -= 20
   return total_cost
def total_trip_cost(days, *cities):
   for i in cities:
       total_cost = 0
       total_cost += hotel_cost(days)
       total_cost += flight_cost(i)
       total_cost += rental_car_cost(days)
       print(i,':',total_cost)
user_cities_list = input('Enter the cities you want to visit for your trip(split with commas): ').split(',')
days = int(input('Enter the number of days you want for your trip: '))
total_trip_cost(days, *user_cities_list)
