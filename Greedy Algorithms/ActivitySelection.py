

def activitySelectionSolution(activity):
    activity = sorted(activity, key = lambda item: item[2])
    # print(activity)

    names = []
    names.append(activity[0])

    for i in range(1,len(activity)):
        if activity[i][1] >= names[-1][2]:
            names.append(activity[i])

    return names


activities = [["A1", 0, 6],
             ["A2", 3, 4],
             ["A3", 1, 2],
             ["A4", 5, 8],
             ["A5", 5, 7],
             ["A6", 8, 9]
             ]

print([name[0] for name in activitySelectionSolution(activities)])