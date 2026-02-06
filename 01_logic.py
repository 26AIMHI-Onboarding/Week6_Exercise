import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) # 예시 가중치
    b = -0.7                 # 예시 편향
    tmp = np.sum(w*x) + b
    return 1 if tmp > 0 else 0

def NAND(x1, x2):
    # p.52 참고: AND의 가중치와 편향을 적절히 변경하여 구현하세요.
    x = np.array([x1, x2])
    w = ### 빈칸: np.array([-0.5, -0.5]) ###
    b = ### 빈칸: 0.7 ###
    tmp = np.sum(w*x) + b
    return 1 if tmp > 0 else 0

def XOR(x1, x2):
    # p.59 참고: 기존 게이트(AND, NAND, OR)를 조합하세요.
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2) # (OR 함수가 정의되어 있다고 가정)
    y = ### 빈칸: AND(s1, s2) ###
    return y