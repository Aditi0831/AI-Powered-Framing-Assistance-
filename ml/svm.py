def train_svm(X, y, lr=0.001, epochs=500):
    w = [0.0, 0.0, 0.0]
    b = 0.0

    for _ in range(epochs):
        for xi, yi in zip(X, y):
            condition = yi * (sum(w[j]*xi[j] for j in range(3)) + b)
            if condition >= 1:
                continue
            else:
                for j in range(3):
                    w[j] += lr * yi * xi[j]
                b += lr * yi
    return w, b

def predict_svm(x, w, b):
    val = sum(w[j]*x[j] for j in range(3)) + b
    return 1 if val >= 0 else -1