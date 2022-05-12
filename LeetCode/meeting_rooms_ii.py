def min_meeting_rooms(intervals):
    start = sorted([interval.start for interval in intervals])
    end = sorted([interval.end for interval in intervals])

    start_pointer, end_pointer = 0, 0
    actual_count, max_count = 0, 0

    while start_pointer < len(start):
        if start[start_pointer] < end[end_pointer]:
            start_pointer += 1
            actual_count += 1
        else:
            end_pointer += 1
            actual_count -= 1
        max_count = max(max_count, actual_count)

    return max_count
