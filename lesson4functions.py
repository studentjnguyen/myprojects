def line():
    print("------------------------------------------")
    return


line()


def readable_timedelta(days):
    days1 = days % 7
    weeks1 = days // 7
    print("{} week(s) and {} day(s).".format(weeks1, days1))
    return


readable_timedelta(10)

line()


def max_numbers(first, second, third):
    if first > second and first > third:
        print(first)
    elif second > first and second > third:
        print(second)
    elif third > first and third > second:
        print(third)
    return


max_numbers(1, 2, 3)

line()


def sum_all(sample_list):
    print(sum(sample_list))
    return


sum_all([8, 2, 3, 0, 7])

line()


def lower_upper(upper_lower):
    count1 = 0
    count2 = 0
    for a in upper_lower:
        if (a.isupper()) == True:
            count1 += 1
        elif (a.islower()) == True:
            count2 += 1
    print("Uppercase letters count: " + str(count1))
    print("Lowercase letters count: " + str(count2))
    return


lower_upper("The Quick Brown Fox")

line()
