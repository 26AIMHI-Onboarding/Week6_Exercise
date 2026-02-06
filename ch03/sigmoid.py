# coding: utf-8
import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    """
    시그모이드 함수 구현 (교재 p.72)
    수식: 1 / (1 + exp(-x))
    """
    # 넘파이의 지수 함수(np.exp)를 사용하여 수식을 완성하세요.
    return ### 빈칸  ###

# -5.0부터 5.0까지 0.1 간격의 넘파이 배열 생성
X = np.arange(-5.0, 5.0, 0.1)

# 위에서 정의한 sigmoid 함수를 호출하여 Y값을 계산하세요.
Y = ### 빈칸 ###

plt.plot(X, Y)
# y축의 범위를 0과 1 사이가 잘 보이도록 설정
plt.ylim(-0.1, 1.1) 
plt.show()