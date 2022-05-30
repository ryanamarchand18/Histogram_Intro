def histogram(data, n, b, h):
    # data is a list
    # n is an integer
    # b and h are floats
    # Write your code here

    #Step 1
    if n <= 0 or h < b:
        hist = []
        return hist

    #Step 2
    if abs(b) > h:
        h = abs(b)

    #Step 3
    i = 0
    if b < 0:
        while len(data) > i:
            data[i] = abs(data[i])
            i += 1

    #Step 4
    if b < 0:
        b = 0

    #Step 5
    hist = [0] * n

    #Step 6
    w = float(float(h - b) / n)


    #Step 7
    p = 0
    while p < len(data):
        if data[p] >= h or data[p] <= b:
            del data[p]
            p -= 1
        p += 1

    #Step 8
    k = 0
    j = 0
    while k < len(data):
        j = 0
        while j < len(data):
            if data[j] >= (b + (w * k)) and data[j] < (b + (w * (k + 1))):
                    hist[k] += 1
            j += 1
        k += 1

    #Step 9
    # return the variable storing the histogram
    return hist
    # Output should be a list
    pass

def birthdaycake(name_to_day, name_to_month, name_to_year):
    #name_to_day, name_to_month and name_to_year are dictionaries
    
    # Write your code here

    #Step 2
    name_to_all = {}

    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    #Step 3
    for calc in name_to_year:
        d = name_to_day[calc]
        m = name_to_month[calc]
        y = name_to_year[calc]

        if m == 10 or m == 11 or m == 12:
            y += 5
        date = m, d, y
        if m <= 2:
            m += 12
            y -= 1
        wd = (d + int((13 * (m + 1)) / 5) + y + int(y / 4) - int(y / 100) + int(y / 400)) % 7

        name_to_all[calc] = date, days[wd]
        
    #Step 4
    return name_to_all
    # return the variable storing name_to_all
    # Output should be a dictionary
    
    pass
