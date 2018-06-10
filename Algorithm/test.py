def Solution (S):
    """
    type S:  "HH:MM" format string
    type h1: string
    type h2: string
    type m1: string
    type m2: string
    return closest_time: "HH:MM" format string
    """
    (hh, mm) = S.split(":")
    h1 = hh[0]
    h2 = hh[1]
    m1 = mm[0]
    m2 = mm[1]
    list = [h1,h2,m1,m2]

    list2 = list[:]
    closest_time = ""
    closest_val = float('inf')
    val = 0
    for h11 in list:
        print "h11 is ", h11
        list2 = list[:]
        print "first list2 is ", list2
        if int(h11) >= 3:
            continue
        list2.remove(h11)
        print "current list2 is ", list2
        for h22 in list2:
            print "h22 is ", h22
            HH = h11 + h22
            if int(HH) >= 24:
                continue
            list2.remove(h22)
            print "current list2 is ", list2
            for m11 in list2:
                if int(m11) >= 6:
                    continue
                list2.remove(m11)
                print "current list2 is ", list2
                for m22 in list2:
                    MM = m11+m22
                    print HH + ":" + MM
                    if int(HH) == 0:
                        HH = 24
                    if int(HH) > int(hh):
                        val = int(HH) * 60 + int(MM) - int(hh) * 60 - int(mm)
                    elif int(HH) == int(hh) and int(MM) == int(mm):
                        val = 24 * 60
                    elif int(HH) < int(hh):
                        val = 24 * 60 - (int(hh) * 60 + int(mm) - int(HH) * 60 - int(MM))
                    if val < closest_val:
                        closest_val = val
                        closest_time = HH+":"+MM
    return closest_time


print Solution("11:00")



