# Mortgage Disclosure Explorer

A small command-line tool for exploring the sample mortgage disclosure dataset.

## Project structure

```text
mortgage-disclosure-explorer/
├── data/
│   └── sample.csv
├── src/
│   └── explore.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Getting started

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the explorer against the sample data:

```bash
python src/explore.py
```

To inspect another pipe-delimited dataset:

```bash
python src/explore.py path/to/data.csv
```
