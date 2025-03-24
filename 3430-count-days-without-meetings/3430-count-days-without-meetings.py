from collections import defaultdict
from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        dayMap = defaultdict(int)

        # Mark the start and end of meetings in the map
        for start, end in meetings:
            dayMap[start] += 1
            dayMap[end + 1] -= 1

        prefixSum = 0
        freeDays = 0
        previousDay = 1  # Start checking from day 1

        # Process sorted keys of the dayMap
        for currentDay in sorted(dayMap.keys()):
            if prefixSum == 0:  
                freeDays += currentDay - previousDay  # Add free days

            prefixSum += dayMap[currentDay]  # Update prefix sum
            previousDay = currentDay

        # Add remaining free days after last meeting
        freeDays += days - previousDay + 1

        return freeDays
