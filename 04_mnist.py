import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
import pickle

def get_data():
    # normalize=True로 설정하여 픽셀 값을 0.0~1.0 사이로 정규화 
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True)
    return x_test, t_test

def predict(network, x):
    # network 딕셔너리에 담긴 가중치로 추론 수행
    ### 3단계의 forward 로직 활용 ###
    pass

x, t = get_data()
# 미리 학습된 가중치 로드 (교재 제공 파일)
with open("sample_weight.pkl", 'rb') as f:
    network = pickle.load(f) 

accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y) # 가장 높은 확률의 인덱스 
    if p == t[i]:
        accuracy_cnt += 1

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))