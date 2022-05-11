def can_attend_meetings(intervals) -> bool:
    intervals.sort(key=lambda x: x[0])

    for i in range(len(intervals) - 1):
        first, second = intervals[i], intervals[i + 1]

        if second.start < first.end:
            return False

    return True
