class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the position, go from closest from target to furthest from target, calculate the time to destination, if < curr_fleet, will become part of that fleet, else, will become the start of a new fleet

        desc_pos = sorted(enumerate(position), key = lambda x: x[1], reverse = True)
        curr_fleet_time = 0
        fleet_count = 0

        for i, pos in desc_pos:
            time_to_des = (target - pos)/speed[i]
            if time_to_des > curr_fleet_time:
                curr_fleet_time = time_to_des
                fleet_count += 1
        
        return fleet_count
