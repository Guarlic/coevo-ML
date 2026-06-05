def 확통(mine, yours):
    if len(mine) < 3:
        return ['C','D','C'][len(mine)]
    
    coop_after_C = 0
    defect_after_C = 0
    coop_after_D = 0
    defect_after_D = 0

    for m, y in zip(mine, yours):
        if m == 'C':
            if y == 'C': coop_after_C += 3
            else: defect_after_C += 1
        else:
            if y == 'C': coop_after_D += 1
            else: defect_after_D += 1
    
    if mine[-1] == 'C':
        if coop_after_C >= defect_after_C * 0.6: return 'C'
        return 'D'
    if coop_after_D >= defect_after_D * 0.3: return 'C'
    return 'D'