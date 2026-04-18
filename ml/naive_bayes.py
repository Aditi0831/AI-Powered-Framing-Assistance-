# ml/naive_bayes.py

# Simple Naive Bayes using probability rules (no library)

def predict_disease(N, P, K):
    # Prior probabilities (assumed)
    p_disease = 0.4
    p_no_disease = 0.6

    # Likelihood (assumed from observation)
    if N > 80:
        pN_d = 0.7
        pN_nd = 0.3
    else:
        pN_d = 0.3
        pN_nd = 0.7

    if P < 40:
        pP_d = 0.6
        pP_nd = 0.4
    else:
        pP_d = 0.4
        pP_nd = 0.6

    if K < 30:
        pK_d = 0.8
        pK_nd = 0.2
    else:
        pK_d = 0.2
        pK_nd = 0.8

    # Naive Bayes formula
    prob_disease = p_disease * pN_d * pP_d * pK_d
    prob_no_disease = p_no_disease * pN_nd * pP_nd * pK_nd

    if prob_disease > prob_no_disease:
        return "Disease Risk"
    else:
        return "Healthy Crop"