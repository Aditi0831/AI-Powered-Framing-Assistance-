import csv

def load_dataset():
    X, y_crop, y_yield = [], [], []
    with open("agri_data.csv") as f:
        reader = csv.DictReader(f)
        for r in reader:
            x = [float(r['N']), float(r['P']), float(r['K'])]
            X.append(x)
            y_crop.append(r['crop'])
            y_yield.append(float(r['yield']))
    return X, y_crop, y_yield