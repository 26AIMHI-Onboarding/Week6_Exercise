# coding: utf-8
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    """
    계단 함수 구현 (교재 p.71)
    입력이 0을 넘으면 1을 출력하고, 그 외에는 0을 출력합니다.
    """
    # 넘파이 배열의 부등호 연산을 이용해 구현하세요.
    # 힌트: x > 0 결과인 Boolean 배열을 int형으로 변환합니다.
    return ### 빈칸 ###

# -5.0부터 5.0까지 0.1 간격의 넘파이 배열 생성
X = np.arange(-5.0, 5.0, 0.1)

# 위에서 정의한 step_function을 호출하여 Y값을 계산하세요.
Y = ### 빈칸 ###

# 그래프를 그립니다.
plt.plot(X, Y)
# y축의 범위를 0과 1이 명확히 보이도록 설정
plt.ylim(-0.1, 1.1) 
plt.show()