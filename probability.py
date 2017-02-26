MIN_D = 1
MAX_D = 20

PROB_SPACE_SIZE = 8000

def expected_tap(attrs, taw, handicap):
    space = event_space(attrs, taw, handicap)

    result_tap = 0
    for tap in range(0, max(taw, 1) + 1):
        result_tap += tap * space[tap]

    return result_tap / PROB_SPACE_SIZE
    
def probability(tap, attrs, taw, handicap):
    space = event_space(attrs, taw, handicap)
    if tap < len(space):
        tap_count = space[tap]
    else:
        tap_count = 0
    return tap_count / PROB_SPACE_SIZE

def event_space(attrs, taw, handicap):
    taps = []
    for i in range(0, max(taw, 1)+1):
        taps.append(0)

    lbound = MIN_D
    ubound = MAX_D+1

    for d1 in range(lbound, ubound):
        for d2 in range(lbound, ubound):
            for d3 in range(lbound, ubound):
                result_tap = roll_tap((d1,d2,d3), attrs, taw, handicap)

                count = taps[result_tap]
                count += 1
                taps[result_tap] = count
    return taps

def roll_tap(rolls, attrs, taw, handicap):
    (d1,d2,d3) = rolls
    (a1,a2,a3) = attrs

    dif1 = a1 - d1
    dif2 = a2 - d2
    dif3 = a3 - d3

    taw_with_hc = taw - handicap

    if double_one(rolls):
        return max(taw, 1)
    if double_twenty(rolls):
        return 0

    if taw_with_hc < 0:
        threshold = abs(taw_with_hc)
        if dif1 >= threshold and dif2 >= threshold and dif3 >= threshold:
            return 1
        else:
            return 0
    else:
        mtotal = min(dif1, 0) + min(dif2, 0) + min(dif3, 0)
        tap_after_rolls = taw_with_hc + mtotal

        if tap_after_rolls < 0:
            return 0
        else:
            return max(min(tap_after_rolls, taw), 1)

def double_one(rolls):
    return double_number(rolls, 1)

def double_twenty(rolls):
    return double_number(rolls, 20)

def double_number(rolls, n):
    (d1,d2,d3) = rolls

    is1 = d1 == n
    is2 = d2 == n
    is3 = d3 == n

    return (is1 and is2) or (is1 and is3) or (is2 and is3)
