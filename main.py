import os
import time
import sys

# Get total points to spend from command line argument
total_points_left = int(sys.argv[1])

# Throw error if total points to spend is < 0
if total_points_left < 0:
    print('ERROR! Points to spend cannot be less than 0')
    sys.exit(1)

# Read data from csv file, sort the data and prepare the initial state of total points
def parse_and_sort():

    # Path to CSV file
    csv_file_path = os.path.join(os.path.curdir, 'transactions.csv')

    data = []
    hashmap = {}
    header = True

    try:
        # Start reading csv file
        with open(csv_file_path) as f:
            while True:

                line = f.readline()
                if line == "":
                    break

                # Skip header row
                if header:
                    header = False
                    continue
                else:
                    # Clean the data
                    payer, points, timestamp = line.replace("\"", "").strip().split(",")

                    # Prepare initial state of total points for each payer
                    if payer in hashmap:
                        hashmap[payer] += int(points)
                    else:
                        hashmap[payer] = int(points)

                    data.append([payer, int(points), timestamp])

            f.close()
    except FileNotFoundError as e:
        print("ERROR! Cannot find the file 'transactions.csv'. Make sure to keep this file in the current working directory")
        sys.exit(1)

    # Sort the data based on timestamp value
    data = sorted(data, key = lambda x: time.mktime(time.strptime(x[2], "%Y-%m-%dT%H:%M:%SZ")))

    return (data, hashmap)


# Get sorted data and initial state
data, hashmap = parse_and_sort()

for payer, points, timestamp in data:

    # Exit if total points to spend become 0
    if total_points_left == 0:
        break
    
    # Check for preventing payer points to go to negative
    if hashmap[payer] - min(points, total_points_left) >= 0:
        hashmap[payer] -= min(points, total_points_left)
        total_points_left -= min(points, total_points_left)

print(hashmap)






    
