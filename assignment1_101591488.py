"""
Author: Deniz Can
Assignment1
"""

# step b: create 4 variables
gym_member = "Alex Alliton" # str
preferred_weight_kg = 20.5 # float
highest_reps = 25 # int
membership_active = True # bool

# step c: create a dictionary named workout_stats
# dictionary with string keys and tuple of ints as values
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 50, 30),
    "Taylor": (20, 30, 40)
}

# step d: calculate total workout minutes using a loop and add to dictionary
for friend in list(workout_stats.keys()):
    total = sum(workout_stats[friend])
    workout_stats[f"{friend}_Total"] = total

# step e: create a 2D nested list called workout_list
# 2-dimensional list of integers
workout_list = []
for key, val in workout_stats.items():
    if not key.endswith("_Total"):
        workout_list.append(list(val))

# step f: slice the workout_list
for row in workout_list:
    print(row[0:2])
for row in workout_list[-2:]:
    print(row[2:])

# step g: check if any friend's total >= 120
for key, val in workout_stats.items():
    if key.endswith("_Total") and val >= 120:
        friend_name = key.replace("_Total", "")
        print(f"Great job staying active, {friend_name}!")

# step h: user input to look up a friend
name = input("Enter a friend's name: ")
if name in workout_stats and not name.endswith("_Total"):
    print(f"Workout minutes: {workout_stats[name]}")
    print(f"Total workout minutes: {workout_stats[f'{name}_Total']}")
else:
    print(f"Friend {name} not found in the records.")

# step i: friend with highest and lowest total workout minutes
highest_name = ""
highest_min = 0
lowest_name = ""
lowest_min = 9999
for key, val in workout_stats.items():
    if key.endswith("_Total"):
        if val > highest_min:
            highest_min = val
            highest_name = key.replace("_Total", "")
        if val < lowest_min:
            lowest_min = val
            lowest_name = key.replace("_Total", "")
print(f"Highest total workout minutes: {highest_name}")
print(f"Lowest total workout minutes: {lowest_name}")

#end of my code
