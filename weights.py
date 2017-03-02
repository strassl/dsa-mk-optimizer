def get_weight_for_skill(skill):
    taw = skill['taw']
    # x^2/(40+x^2)
    # http://www.wolframalpha.com/input/?i=x%5E2%2F(40%2Bx%5E2)+from+0+to+20
    tawsq = taw * taw
    w = tawsq / (40 + tawsq)
    return w