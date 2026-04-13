import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score
import time

df = pd.read_csv("bank.csv")

target_name = 'deposit'
X = df.drop('deposit', axis=1)
y = df[target_name]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

num_cols = ["age", "balance", "day", "campaign", "pdays", "previous", "duration"]

cat_cols = ["job", "marital", "education", "default", "housing",
            "loan", "contact", "month", "poutcome"]

preprocess_pipeline = ColumnTransformer([
    ("num", Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ]), num_cols),

    ("cat", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ]), cat_cols)
])

X_train = preprocess_pipeline.fit_transform(X_train)
X_test = preprocess_pipeline.transform(X_test)

encode = LabelEncoder()
y_train = encode.fit_transform(y_train)
y_test = encode.fit_transform(y_test)

def batch_classify(X_train, y_train, X_test, y_test):

    models = [
        ("Logistic Regression", LogisticRegression()),
        ("Random Forest", RandomForestClassifier()),
        ("KNN", KNeighborsClassifier()),
        ("Naive Bayes", GaussianNB()),
        ("SVM", SVC())
    ]

    results = []

    for name, model in models:
        t_start = time.perf_counter()

        model.fit(X_train, y_train)

        t_end = time.perf_counter()

        train_score = model.score(X_train, y_train)
        test_score = model.score(X_test, y_test)

        results.append({
            "model": name,
            "train_score": train_score,
            "test_score": test_score,
            "training_time": t_end - t_start
        })

    return pd.DataFrame(results)


df_results = batch_classify(X_train, y_train, X_test, y_test)
print(df_results.sort_values(by='test_score', ascending=False))

def feature_importance_graph(indices, importances, feature_names):
    plt.figure(figsize=(10, 12))
    plt.title("Feature Importance")

    plt.barh(range(len(indices)), importances[indices], align="center")
    plt.yticks(range(len(indices)), feature_names[indices])
    plt.xlabel("Relative Importance")
    plt.show()

model = RandomForestClassifier()
model.fit(X_train, y_train)

importances = model.feature_importances_
indices = np.argsort(importances)

feature_names = np.array(preprocess_pipeline.get_feature_names_out())

feature_importance_graph(indices, importances, feature_names)

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
ConfusionMatrixDisplay(cm).plot()
plt.show()

from sklearn.metrics import roc_curve, roc_auc_score

y_prob = model.predict_proba(X_test)[:,1]

fpr, tpr, _ = roc_curve(y_test, y_prob)
auc = roc_auc_score(y_test, y_prob)

plt.plot(fpr, tpr, label="AUC=" + str(auc))
plt.plot([0,1], [0,1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.title("ROC Curve")
plt.show()

from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [5, 10, None],
    'min_samples_split': [2, 5]
}

grid = GridSearchCV(RandomForestClassifier(), param_grid, cv=5, scoring='accuracy')
grid.fit(X_train, y_train)

print("Best parameters:", grid.best_params_)
print("Best score:", grid.best_score_)

import pickle

with open("modelo_banco.pkl", "wb") as f:
    pickle.dump(model, f)
    
