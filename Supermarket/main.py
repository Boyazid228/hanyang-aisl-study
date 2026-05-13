import sys


inventory = []

def get_inventory(current_timestamp):
	result = []
	for i in range(len(inventory)-1, -1, -1):
		if inventory[i][0]+inventory[i][2] > current_timestamp:
			result.append(inventory[i][1])
	return result


def sell_product(current_timestamp):
	while inventory:
	    tail = inventory.pop()

	    if tail[0]+tail[2] > current_timestamp:
	        return tail[1]

	return -1

	
def add_product(current_timestamp, id, expires_in):
	inventory.append([current_timestamp, id, expires_in])


def main():
	for line in sys.stdin:
	    parts = line.strip().split()

	    if not parts:
	        continue

	    cmd = parts[0]

	    if cmd == "add_product":
	        t, id, exp = map(int, parts[1:])
	        add_product(t, id, exp)

	    elif cmd == "sell_product":
	        t = int(parts[1])
	        print(sell_product(t))

	    elif cmd == "get_inventory":
	        t = int(parts[1])
	        print(get_inventory(t))

if __name__ == '__main__':
	main()