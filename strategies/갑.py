def 팃포탯(mine, yours):
    if len(yours) == 0:
        return 'C' # 첫 게임은 무조건 협력
    return yours[-1]
