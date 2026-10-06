# Initial status and transportation availability variables
distance_mi = 5
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = True

# Step 1: Check if the distance is zero (Falsy)
if not distance_mi:
    print(False)

# Step 2: Short distance logic (Less than or equal to 1 mile)
elif distance_mi <= 1:
    if not is_raining:
        print(True)  # Can walk if it's not raining
    else:
        print(False) # Cannot walk in the rain

# Step 3: Medium distance logic (Between 1 and 6 miles)
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)  # Can bike if a bicycle is available and it's dry
    else:
        print(False) # Cannot bike in the rain or without a bicycle

# Step 4: Long distance logic (Greater than 6 miles)
else:
    if has_car or has_ride_share_app:
        print(True)  # Can commute via car or ride-share app
    else:
        print(False) # No suitable transportation available
