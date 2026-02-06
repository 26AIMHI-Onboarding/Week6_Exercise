import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    # 넘파이 배열 x의 원소 중 0보다 큰 것만 1로 변환 
    return np.array(x > 0, dtype=np.int)

def sigmoid(x):
    # 시그모이드 수식 구현 
    return ### 빈칸: 1 / (1 + np.exp(-x)) ###

x = np.arange(-5.0, 5.0, 0.1)
y_step = step_function(x)
y_sig = sigmoid(x)

plt.plot(x, y_step, linestyle="--", label="step")
plt.plot(x, y_sig, label="sigmoid")
plt.ylim(-0.1, 1.1)
plt.legend()
plt.show()