import csv

def load_data():
    X, y_crop, y_yield = [], [], []
    with open("agri_data.csv") as f:
        reader = csv.DictReader(f)
        for r in reader:
            X.append([float(r['N']), float(r['P']), float(r['K'])])
            y_crop.append(r['crop'])
            y_yield.append(float(r['yield']))
    return X, y_crop, y_yield