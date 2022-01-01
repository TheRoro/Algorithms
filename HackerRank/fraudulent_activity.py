def get_median(arr):
    arr.sort()
    median = 0
    if len(arr) % 2 == 0:
        median = (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
    else:
        median = arr[(len(arr) - 1) // 2]
    return median


def activity_notifications(expenditure, d):
    trailing = []
    notifications = 0

    for i in range(len(expenditure)):
        print(trailing)
        if i < d:
            trailing.append(expenditure[i])
        else:
            trailing.append(expenditure[i])
            if expenditure[i] >= get_median(trailing) * 2:
                notifications += 1
            trailing.pop()

    return notifications


print(activity_notifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
# print(activity_notifications([1,2,3,4,4], 4))
# print(activity_notifications([10,20,30,40,50], 3))
