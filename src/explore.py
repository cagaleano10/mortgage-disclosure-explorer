"""Print a concise exploratory summary of a pipe-delimited mortgage dataset."""

import argparse
from pathlib import Path
import pandas as pd
import tkinter as tk
root = tk.Tk()
DEFAULT_DATA = Path(__file__).resolve().parents[1] / "data" / "sample.csv"

lb = tk.Listbox(root)
### button = tk.Button(root, text="Stop", width=25, command=)
lb.insert(1, "Average Loan Amount")
lb.insert(2, "Average Interest Rate")
lb.insert(3, "Average Loan-to-Value Ratio")
lb.insert(4, "Average Debt-to-Income Ratio")

lb.pack()
root.mainloop()

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Summarize a pipe-delimited mortgage disclosure dataset."
    )
    parser.add_argument(
        "data_path",
        nargs="?",
        type=Path,
        default=DEFAULT_DATA,
        help=f"input file (default: {DEFAULT_DATA})",
    )
    args = parser.parse_args()

    data = pd.read_csv(args.data_path, sep="|")
    print(f"Average Loan Amount: ${data['Mortgage Loan Amount'].mean():,.2f}")
    print(f"Average Interest Rate: {data['Current Interest Rate'].mean():.2f}%")
    print(f"Average Loan-to-Value Ratio: {data['Loan-To-Value (LTV)'].mean():.2f}%")
    print(f"Average Debt-to-Income Ratio: {data['Debt-To-Income (DTI)'].mean():.2f}%")
    print(f"Average Borrower Credit Score: {data['Classic FICO'].mean():.2f}")
    print(f"File: {args.data_path}")
    print(f"Rows: {len(data):,}")
    print(f"Columns: {len(data.columns):,}")

    missing = data.isna().sum()
    missing = missing[missing > 0].sort_values(ascending=False)
    if not missing.empty:
        print("\nMissing values:")
        print(missing.to_string())

    numeric = data.select_dtypes(include="number")
    if not numeric.empty:
        print("\nNumeric summary:")
        print(numeric.describe().to_string())


if __name__ == "__main__":
    main()
