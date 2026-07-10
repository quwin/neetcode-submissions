class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        slowest_eta_ahead = 0
        for pos, spd in cars:
            eta = (target - pos) / spd
            if eta > slowest_eta_ahead:
                fleets += 1
                slowest_eta_ahead = eta

        return fleets
                

