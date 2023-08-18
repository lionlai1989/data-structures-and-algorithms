from sys import stdin


def min_refills(distance, tank, stops):
    # print(distance, tank, stops)

    # The end line is the last stops.
    stops.append(distance)

    if distance < tank:
        return 0 # No need to refill
    
    num_refill = 0
    current_pos = 0
    tank_realtime = tank

    for idx in range(len(stops)):
        # Next stop is too far away.
        if stops[idx] - current_pos > tank:
            return -1 # It's impossible to reach the next stop.

        # Refill the tank to reach the next stop.
        if stops[idx] - current_pos > tank_realtime:
            # Refill the tank
            num_refill += 1
            tank_realtime = tank
        
        # Consume the tank and move to the next stop.
        tank_realtime = tank_realtime - (stops[idx] - current_pos)
        current_pos = stops[idx]

    return num_refill # Return number of refill


if __name__ == '__main__':
    # Use the following as input:
    # 950
    # 400
    # 4
    # 200 375 550 750
    # <ctrl-d> sends EOF
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
