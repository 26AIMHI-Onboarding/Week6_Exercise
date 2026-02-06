import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    
    # 1. 적절한 가중치(w)와 편향(b)을 설정하세요 (교재 p.53)
    w = np.array([### 빈칸 1 ###]) 
    b = ### 빈칸 2 ###
    
    # 퍼셉트론의 연산 식을 완성하세요 (입력값과 가중치의 곱의 합 + 편향)
    tmp = ### 빈칸 ###
    
    # 활성화 함수(임계값을 넘으면 1, 아니면 0)를 구현하세요
    if tmp ## 빈칸 ### :
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = AND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))