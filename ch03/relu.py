import numpy as np
import matplotlib.pylab as plt


def relu(x):
    """
    ReLU 함수 구현 (교재 p.76)
    입력이 0을 넘으면 그 입력을 그대로 출력하고, 0 이하면 0을 출력합니다.
    """
    # np.maximum 함수를 사용하여 ReLU를 한 줄로 구현하세요.
    return ### 빈칸 ###

x = np.arange(-5.0, 5.0, 0.1)

# 위에서 정의한 relu 함수를 호출하여 y값을 계산하세요.
y = ### 빈칸 ###

plt.plot(x, y)
plt.ylim(-1.0, 5.5)
plt.show()