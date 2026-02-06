import numpy as np

def step_function(x):
    """
    계단 함수 (p.69)
    x가 0을 넘으면 1을, 그렇지 않으면 0을 반환하도록 구현하세요.
    """
    # 힌트: np.array(x > 0, dtype=np.int) 활용
    return ### 빈칸: 여기에 코드를 작성하세요 ###

def sigmoid(x):
    """
    시그모이드 함수 (p.72)
    수식: 1 / (1 + exp(-x))
    """
    return ### 빈칸: 여기에 수식을 코드로 작성하세요 ###

def relu(x):
    """
    ReLU 함수 (p.76)
    0보다 크면 그대로, 0 이하면 0을 반환합니다.
    """
    return ### 빈칸: np.maximum(?, ?) 활용 ###

def identity_function(x):
    """항등 함수 (회귀용 출력층, p.91)"""
    return x

def softmax(x):
    """
    소프트맥스 함수 (분류용 출력층, p.94)
    지수 함수를 사용하며, 오버플로 대책을 위해 입력 중 최댓값을 빼주어야 합니다.
    """
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T 

    # 1. 입력값 중 최댓값 찾기
    c = ### 빈칸: np.max(x) ###
    
    # 2. 분자: exp(x - c) 계산
    exp_a = ### 빈칸: np.exp(x - c) ###
    
    # 3. 분모: 분자들의 합 계산
    sum_exp_a = ### 빈칸: np.sum(exp_a) ###
    
    y = exp_a / sum_exp_a
    return y