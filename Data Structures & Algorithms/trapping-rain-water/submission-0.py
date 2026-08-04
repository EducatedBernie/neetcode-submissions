class Solution:
    def trap(self, height: List[int]) -> int:
        

        l = 0
        r = len(height) - 1

        wallsToSeen = {}
        wallsToPotential = {}

        while l < r:
            # register what l is on, update seen list
            for h, count in wallsToSeen.items():
                if height[l] <= h:
                    count += height[l]
                if height[r] <= h:
                    count += height[r]

            # created potential if it didn't exist

            bottleNeckHeight = min(height[r], height[l])
            
            if bottleNeckHeight not in wallsToPotential:
                wallsToPotential[bottleNeckHeight] = height[r] * height[l]
                wallsToSeen[bottleNeckHeight] = 0 
                #make sure future we add walls that are at or below this height
            
            # register what r is on

            # now move
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        maxRain = 0
        # iterate through the wallsToPotential list
        for wallHeight, potential in wallsToPotential.items():
            maxRain = max(maxRain, potential - wallsToSeen[wallHeight])

        return maxRain