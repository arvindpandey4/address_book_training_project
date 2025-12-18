class Ride:
    def __init__(self, distance, start_time):
        self.distance = distance
        self.start_time = start_time
    
    def calculate_fare(self):
        base_fare = 50
        per_km_fare = 12
        final_fare = base_fare + (self.distance * per_km_fare)

        hr = int(self.start_time.split(":")[0])

        if (8 <= hr < 10) or (18 <= hr < 21):
            final_fare = final_fare*1.5
        
        if (hr >= 23) or (hr < 5):
            final_fare = final_fare + 100
        
        if final_fare > 1000:
            final_fare = 1000
        
        return final_fare

user_distance = float(input("Enter the distance travelled by you: "))
user_start_time = input("Enter your start time: ")
ride = Ride(user_distance, user_start_time)
total_fare = ride.calculate_fare()
print(f"Your total fare is: {total_fare}")