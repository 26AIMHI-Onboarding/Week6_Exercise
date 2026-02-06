# Week 6 Onboarding 실습 가이드

6주차 신경망 기초 실습에 오신 것을 환영합니다! 

이 실습은 논리 게이트 구현부터 시작하여 MNIST 손글씨 인식까지 단계적으로 진행됩니다.

## 📋 실습 순서

### 1단계: 논리 게이트 구현 (ch02)
기본적인 논리 게이트를 파이썬으로 구현하며 신경망의 기초를 학습합니다.

```
ch02/
├── and_gate.py        # AND 게이트 구현
├── nand_gate.py       # NAND 게이트 구현
├── or_gate.py         # OR 게이트 구현
└── xor_gate.py        # XOR 게이트 구현 (퍼셉트론의 한계)
```

**실습 순서:**
1. `and_gate.py` - AND 게이트로 퍼셉트론 기본 개념 이해
2. `nand_gate.py` - NAND 게이트 구현
3. `or_gate.py` - OR 게이트 구현
4. `xor_gate.py` - 다층 퍼셉트론의 필요성 이해

### 2단계: 활성화 함수 구현 (ch03)
신경망의 핵심인 다양한 활성화 함수를 직접 구현하며 특성을 이해합니다.

```
ch03/
├── step_function.py          # Step 함수 구현
├── sigmoid.py                # Sigmoid 함수 구현
├── relu.py                   # ReLU 함수 구현
└── sig_step_compare.py       # 활성화 함수 비교
```

**실습 순서:**
1. `step_function.py` - 계단 함수 구현
2. `sigmoid.py` - 시그모이드 함수 구현
3. `relu.py` - ReLU 함수 구현
4. `sig_step_compare.py` - 활성화 함수 비교 및 특성 이해

### 3단계: 공통 함수 정리 (common)
앞서 구현한 활성화 함수들을 재사용 가능한 모듈로 정리합니다.

```
common/
└── functions.py       # 활성화 함수 및 유틸리티 함수 모음
```

**구현 내용:**
- Step 함수
- Sigmoid 함수
- ReLU 함수
- Softmax 함수
- 기타 유틸리티 함수

**⚠️ 중요:** ch03에서 구현한 함수들을 여기에 모아서 정리하고, MNIST 실습에서 import하여 사용합니다!

### 4단계: MNIST 신경망 구현 (ch03)
손글씨 숫자 인식을 위한 신경망을 구현하고 실행합니다.

```
ch03/
├── mnist_show.py             # MNIST 데이터 시각화
├── neuralnet_mnist.py        # 기본 신경망 구현
├── neuralnet_mnist_batch.py  # 배치 처리 구현
└── sample_weight.pkl         # 학습된 가중치 파일
```

**실습 순서:**
1. `mnist_show.py` - MNIST 데이터셋 확인 및 시각화
2. `neuralnet_mnist.py` - 신경망 기본 구현 및 추론 (common/functions.py 사용)
3. `neuralnet_mnist_batch.py` - 배치 처리로 성능 향상

## 🚀 시작하기

### 환경 설정
```bash
# 필요한 패키지 설치
pip install -r requirements.txt
```

### 실습 진행
```bash
# 1단계: 논리 게이트
cd ch02
python and_gate.py
python nand_gate.py
python or_gate.py
python xor_gate.py

# 2단계: 활성화 함수 구현
cd ../ch03
python step_function.py
python sigmoid.py
python relu.py
python sig_step_compare.py

# 3단계: 공통 함수 정리 (MNIST 전에 필수!)
cd ../common
# functions.py에 앞서 구현한 함수들을 정리

# 4단계: MNIST 신경망
cd ../ch03
python mnist_show.py
python neuralnet_mnist.py
python neuralnet_mnist_batch.py
```

## 📚 학습 목표

### ch02: 퍼셉트론
- 퍼셉트론의 동작 원리 이해
- 선형 분류기의 한계 인식
- 다층 퍼셉트론의 필요성 이해

### ch03: 활성화 함수
- 다양한 활성화 함수 직접 구현
- 각 활성화 함수의 특성과 차이점 이해
- 신경망에서 활성화 함수의 역할 파악

### common: 코드 재사용
- 구현한 함수들을 모듈화하여 정리
- import를 통한 코드 재사용 학습
- 깔끔한 코드 구조 만들기

### ch03: MNIST 신경망
- 순방향 전파(forward propagation) 구현
- MNIST 데이터셋 다루기
- common 모듈 활용하기
- 배치 처리를 통한 효율성 향상

## 💡 Tips

1. **각 단계를 순서대로 진행하세요** - 이전 단계의 개념이 다음 단계의 기초가 됩니다.
2. **코드를 직접 수정하며 실험하세요** - 파라미터를 변경하고 결과를 관찰하세요.
3. **활성화 함수를 먼저 이해하세요** - ch03에서 각 함수를 구현한 후 common에 정리합니다.
4. **common/functions.py 완성 필수** - MNIST 실습에서 이 모듈을 import하여 사용합니다.
5. **시각화를 활용하세요** - `mnist_show.py`로 데이터를 확인하면 이해가 쉽습니다.

## 📁 프로젝트 구조

```
WEEK6_EXERCISE/
├── ch02/              # 논리 게이트 실습
│   ├── and_gate.py
│   ├── nand_gate.py
│   ├── or_gate.py
│   ├── xor_gate.py
│   └── readme.md
├── ch03/              # MNIST 신경망 실습
│   ├── step_function.py
│   ├── sigmoid.py
│   ├── relu.py
│   ├── sig_step_compare.py
│   ├── mnist_show.py
│   ├── neuralnet_mnist.py
│   ├── neuralnet_mnist_batch.py
│   ├── sample_weight.pkl
│   └── readme.md
├── common/            # 공통 함수
│   └── functions.py
├── dataset/           # 데이터셋 (자동 다운로드)
├── requirements.txt   # 필요 패키지
└── README.md         # 이 파일

```

## ⚙️ 요구사항

- Python 3.7+
- NumPy
- Matplotlib
- PIL (Pillow)

## 🎯 체크리스트

- [ ] ch02: 모든 논리 게이트 구현 완료
- [ ] ch03: 활성화 함수들(step, sigmoid, relu) 구현 완료
- [ ] ch03: 활성화 함수 비교 완료
- [ ] common: functions.py에 활성화 함수 정리 완료
- [ ] ch03: MNIST 데이터 시각화 확인
- [ ] ch03: 기본 신경망 추론 성공
- [ ] ch03: 배치 처리 구현 완료

---

**Happy Learning! 🚀**

질문이 있다면 언제든지 문의하세요!