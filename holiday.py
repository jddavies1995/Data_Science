
# Inputs for the holiday - destination, number of nights staying and number of days to rent a car
city_flight = input("What city do you want to go to: Madrid, Lisbon or Paris? ")
num_nights = int(input("How many nights do you want to stay? "))
rental_days = int(input("How many days will you need to hire a car? "))

# function to calculate total hotel cost
def hotel_cost(num_nights):
    total_hotel = num_nights * 120
    return total_hotel

# function to calculate total flight cost
def plane_cost(city_flight):
    if city_flight == "Madrid":
        total_flight = 100
    elif city_flight == "Lisbon":
        total_flight = 120
    elif city_flight == "Paris":
        total_flight = 80
    else: 
        print("City is not in the list of destinations")
        total_flight = 0
    return total_flight

# function to calculate total car rental cost
def car_rental(rental_days):
    total_car = rental_days * 80
    return total_car

# function to calculate total holiday cost
def holiday_cost(num_nights, city_flight, rental_days):
    total_all = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_all

# Printing out the outputs of the holiday costs
print("The total cost of the hotel was: ", hotel_cost(num_nights))
print("The total cost of the plane was: ", plane_cost(city_flight))
print("The total cost of the car rental was: ", car_rental(rental_days))
print("The total cost of the holiday was: ", holiday_cost(num_nights, city_flight, rental_days))



