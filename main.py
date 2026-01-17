from src.data_loader import load_data
from src.preprocessing import preprocess
from src.train import train_model
from src.evaluate import evaluate

DATA_PATH = "data/raw/loan_approval_dataset.csv"
TARGET_COL = "loan_status"  

def main():
    df = load_data("~/Downloads/loan_approval_dataset.csv")
    X_train, X_test, y_train, y_test = preprocess(df, TARGET_COL)
    model = train_model(X_train, y_train)
    acc, report = evaluate(model, X_test, y_test)

    print("Accuracy:", acc)
    print(report)

if __name__ == "__main__":
    main()

