def tree1(N,P,K):
    return "Rice" if N > 70 else "Wheat"

def tree2(N,P,K):
    return "Maize" if P > 50 else "Rice"

def tree3(N,P,K):
    return "Wheat" if K < 40 else "Maize"

def random_forest_predict(N,P,K):
    votes = [tree1(N,P,K), tree2(N,P,K), tree3(N,P,K)]
    return max(set(votes), key=votes.count)