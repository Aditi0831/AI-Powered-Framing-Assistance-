from flask import Flask, render_template, request
import csv

# ---- Import ML maths modules ----
from ml.linear_regression import predict_yield
from ml.logistic import predict_crop
from ml.naive_bayes import predict_disease
from ml.decision_tree import recommend_fertilizer
from ml.svm import train_svm, predict_svm
from ml.random_forest import random_forest_predict

app = Flask(__name__)

# -------------------------------------------------
# 🔹 LOAD DATASET (agri_data.csv in same folder)
# -------------------------------------------------

X = []
y_crop = []

with open('agri_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        N = float(row['N'])
        P = float(row['P'])
        K = float(row['K'])
        crop = row['crop']

        X.append([N, P, K])
        y_crop.append(crop)

# -------------------------------------------------
# 🔹 TRAIN SVM ONCE
# -------------------------------------------------

y_svm = [1 if c == "Rice" else -1 for c in y_crop]
w_svm, b_svm = train_svm(X, y_svm)

# -------------------------------------------------
# 🔹 ROUTE
# -------------------------------------------------

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])

        x = [N, P, K]

        # Existing algorithms
        fert = recommend_fertilizer(N, P, K)
        crop = predict_crop(x)
        yld = predict_yield(x)
        disease = predict_disease(N, P, K)

        # New algorithms
        svm_crop = "Rice" if predict_svm(x, w_svm, b_svm) == 1 else "Wheat"
        rf_crop = random_forest_predict(N, P, K)

        return render_template('result.html',
                               fertilizer=fert,
                               crop=crop,
                               yield_pred=yld,
                               disease=disease,
                               svm_crop=svm_crop,
                               rf_crop=rf_crop)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)