# ml/decision_tree.py

# Decision Tree using rule-based splitting (no library)

def recommend_fertilizer(N, P, K):

    if N < 40:
        if P < 40:
            return "Urea"
        else:
            return "DAP"

    elif 40 <= N <= 80:
        if K < 40:
            return "NPK"
        else:
            return "Compost"

    else:  # N > 80
        return "Organic Fertilizer"