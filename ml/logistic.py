# ml/logistic.py

import math

# Logistic Regression using maths
# sigmoid(z) = 1 / (1 + e^-z)

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Assumed weights
w1 = 0.04
w2 = 0.03
w3 = 0.02
b = -4

def predict_crop(x):
    N, P, K = x
    z = w1*N + w2*P + w3*K + b
    prob = sigmoid(z)

    # Threshold 0.5
    if prob >= 0.5:
        return "Rice"
    else:
        return "Wheat"