class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # gain = [-5,1,5,0,-7]
        # gain[i] means the gain in altitude compared to the previous altitude
        # he begins at altitude at 0
        # then he goes down -5 so his altitude is at -5
        # then he gains 1meter which makes is altitude -4 
        # then he gains 5 meter which makes his altitude 1
        # so we will use prefix sum to calculate the altitudes
        # altitudes = [0] * (len(gain) + 1)
        # for i in range(len(gain)):
        #     altitudes[i + 1] = altitudes[i] + gain[i] 
        # return max(altitudes)

        highest_altitude = 0
        current_altitude = 0
        for i in range(len(gain)):
            current_altitude += gain[i]
            highest_altitude = max(current_altitude, highest_altitude)
        return highest_altitude

