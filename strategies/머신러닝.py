import math

def 머신러닝(mine, yours):
    # 과거 2턴의 기록을 피처(Feature)로 사용하므로, 기록이 부족할 땐 협력(C) 반환
    if len(mine) < 2:
        return 'C'
        
    # 머신러닝: 로지스틱 회귀(Logistic Regression) 모델 가중치 초기화
    # 입력 특성(Features) 구성: [바이어스(Bias), t-1 내 행동, t-1 상대 행동, t-2 내 행동, t-2 상대 행동]
    weights = [0.0, 0.0, 0.0, 0.0, 0.0]
    learning_rate = 0.1

    encode = lambda move: 1.0 if move == 'C' else 0.0
    sigmoid = lambda x: 1.0 / (1.0 + math.exp(-max(min(x, 20), -20)))
    
    # 과거의 누적 기록(mine, yours)을 처음부터 순회하며 모델 학습 (온라인 학습 시뮬레이션)
    # 이전 2턴의 정보를 기반으로 현재 턴의 상대방 행동을 예측하도록 가중치 최적화
    for i in range(2, len(mine)):
        # 입력 데이터 x 구성 (t-2와 t-1 시점의 데이터)
        x = [
            1.0, # 바이어스 항
            encode(mine[i-1]),
            encode(yours[i-1]),
            encode(mine[i-2]),
            encode(yours[i-2])
        ]
        
        # 정답 레이블 (t 시점에서의 상대방 실제 행동)
        target = encode(yours[i])
        
        # 순전파(Forward propagation): 선형 결합 계산
        linear_sum = sum(w * f for w, f in zip(weights, x))
        
        # 시그모이드(Sigmoid) 활성화 함수 적용 (지수 함수 오버플로우 방지용 클리핑 포함)
        prediction = sigmoid(linear_sum)
        
        # 역전파(Backpropagation): 오차 계산 및 경사 하강법(Gradient Descent) 가중치 업데이트
        error = target - prediction
        for j in range(len(weights)):
            weights[j] += learning_rate * error * x[j]

    # 학습이 완료된 모델에 현재 상태(가장 최근 2턴)를 입력하여 상대의 다음 행동 예측
    current_x = [
        1.0,
        encode(mine[-1]),
        encode(yours[-1]),
        encode(mine[-2]),
        encode(yours[-2])
    ]
    
    current_linear_sum = sum(w * f for w, f in zip(weights, current_x))
    prob_c = sigmoid(current_linear_sum) # 상대가 다음 턴에 'C'를 낼 예측 확률
    
    # 예측된 결과를 바탕으로 나의 행동을 결정 (최적화)
    # 상대가 협력할 것으로 예상(확률 0.5 이상)되면, 상호 협력의 이득을 챙기기 위해 협력(C)
    # 상대가 배신할 것으로 예상되면, 혼자 배신당해 최악의 점수를 받는 것을 막기 위해 방어적 배신(D)
    return 'C' if prob_c >= 0.5 else 'D'