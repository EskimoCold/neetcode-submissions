class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)

        fleets = 0
        last_time = 0
        
        for p, s in pairs:
            time = (target - p) / s

            if time > last_time:
                fleets += 1
                last_time = time

        return fleets
