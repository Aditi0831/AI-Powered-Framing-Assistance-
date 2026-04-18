# ml/linear_regression.py

# Simple Linear Regression using maths
# y = w1*N + w2*P + w3*K + b

# Pre-calculated weights (assumed from dataset observation)
w1 = 0.5
w2 = 0.3
w3 = 0.2
b = 5

def predict_yield(x):
    N, P, K = x
    y = w1*N + w2*P + w3*K + b
    return round(y, 2)