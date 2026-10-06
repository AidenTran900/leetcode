class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merged = []

        intervals.sort(key = lambda interval : interval[0])

        for i, interval in enumerate(intervals):
            # if merged is empty OR last_interval's end is < interval start (no overlap)
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # set last pt to highest end
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged