"""Print a concise exploratory summary of a pipe-delimited mortgage dataset."""

import argparse
from pathlib import Path

import pandas as pd


DEFAULT_DATA = Path(__file__).resolve().parents[1] / "data" / "sample.csv"


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
