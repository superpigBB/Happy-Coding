## Method 1: mathematical calculation of permutaion by Vicky Bao
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

    closest_time = ""
    closest_val = float('inf')
    val = 0
    for h11 in list:
        if int(h11) >= 3: continue
        h2_list = list[:]
        h2_list.remove(h11)
        # print "h11 is %s" % h11
        # print "h2_list is ", h2_list
        while len(h2_list) >0:
            h22 = h2_list.pop()
            # print "h22 is %s" % h22
            if int(h11+h22) >= 24: continue
            h3_list = list[:]
            h3_list.remove(h11)
            h3_list.remove(h22)
            # print "h3_list is ", h3_list
            for m11 in h3_list:
                h4_list = h3_list[:]
                if int(m11) >=6: continue
                h4_list.remove(m11)
                m22 = h4_list[0]
                # print "m11 is %s, m22 is %s" %(m11, m22)
                # print "Final time format is %s" % (h11+h22+":" + m11 + m22)

                HH = h11 + h22
                MM = m11 + m22

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
                    # print "Type of HH %s is %s, Type of MM %s is %s" % (HH, type(HH), MM, type(MM))
                    if HH == 24: HH = "00"
                    closest_time = HH + ":" + MM
    return closest_time


print Solution("23:59")
print Solution("11:00")


### Method 2 Permutations in Python by searching the algorithm online

def Solution (S):
    # """
    #     type S:  "HH:MM" format string
    #     type h1: string
    #     type h2: string
    #     type m1: string
    #     type m2: string
    #     return closest_time: "HH:MM" format string
    #     """
    (hh, mm) = S.split(":")
    h1 = hh[0]
    h2 = hh[1]
    m1 = mm[0]
    m2 = mm[1]
    l = [h1,h2,m1,m2]

    closest_time = ""
    closest_val = float('inf')
    val = 0
    for p in permutation(l):
        if int(p[0]) < 3 and int(p[0] + p[1]) < 24 and int(p[2]) < 6:
            # print p
            HH = p[0] + p[1]
            MM = p[2] + p[3]

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
                # print "Type of HH %s is %s, Type of MM %s is %s" % (HH, type(HH), MM, type(MM))
                if HH == 24: HH = "00"
                closest_time = HH + ":" + MM
    return closest_time


def permutation(lst):
    """

    :param lst:
    :return: l
    """
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l

print Solution("23:59")
print Solution("11:00")
# for p in permutation([1,2,3]):
#     print p