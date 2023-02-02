import os
import time
import sys


total_points_left = int(sys.argv[1])

if total_points_left < 0:
    print('ERROR! Points to spend cannot be less than 0')
    sys.exit(1)

def parse_and_sort():

    csv_file_path = os.path.join(os.path.curdir, 'transactions.csv')

    data = []
    hashmap = {}
    header = True

    try:
        with open(csv_file_path) as f:
            while True:
                line = f.readline()
                if line == "":
                    break

                if header:
                    header = False
                    continue
                else:
                    payer, points, timestamp = line.strip().split(",")
                    if payer in hashmap:
                        hashmap[payer] += int(points)
                    else:
                        hashmap[payer] = int(points)

                    data.append([payer, int(points), timestamp])

            f.close()
    except FileNotFoundError as e:
        print("ERROR! Cannot find the file 'transactions.csv'. Make sure to keep this file in the current working directory")
        sys.exit(1)

    data = sorted(data, key = lambda x: time.mktime(time.strptime(x[2], "%Y-%m-%dT%H:%M:%SZ")))

    return (data, hashmap)



data, hashmap = parse_and_sort()

for payer, points, timestamp in data:

    if total_points_left == 0:
        break

    if hashmap[payer] - min(points, total_points_left) >= 0:
        hashmap[payer] -= min(points, total_points_left)
        total_points_left -= min(points, total_points_left)

print(hashmap)






    
