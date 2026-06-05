import random

def 사람(mine, yours):
    # 첫 번째 게임에서는 무조건 협력
    if not yours:
        return 'C'
    # 상대의 연속 배신 횟수를 계산
    consec_D = 0
    for move in reversed(yours):
        if move == 'D':
            consec_D += 1
        else:
            break
    # 기본 전략: 직전 협력일 때 협력, 직전 배신일 때 최대 2회까지 보복 후 용서
    if yours[-1] == 'C':
        decision = 'C'
    else:
        if consec_D < 2:
            decision = 'D'
        else:
            decision = 'C'
    # 인간적인 실수 효과: 5% 확률로 의사결정을 뒤집음
    if random.random() < 0.05:
        decision = 'D' if decision == 'C' else 'C'
    return decision
