import csv
import io
from pathlib import Path

import srsly
import typer


def clean_csv(input_csv_path: Path):
    """Read the CSV content, remove NULL bytes and return a file-like object."""
    with input_csv_path.open("rb") as file:
        content = file.read().replace(b"\0", b"")
    return io.StringIO(content.decode("utf-8"))


def convert_csv_to_jsonl(input_csv_path: Path, output_jsonl_path: Path):
    """
    Convert a specified text column from a CSV file to a JSONL file suitable for spaCy pretraining.
    """
    texts = []
    cleaned_csv = clean_csv(input_csv_path)  # Clean the CSV to remove NULL bytes
    reader = csv.DictReader(cleaned_csv)
    for row in reader:
        text = row["description"].strip()
        if text:  # Ensure the text is not empty
            texts.append({"text": text})

    srsly.write_jsonl(output_jsonl_path, texts)
    print(f"Converted texts from {input_csv_path} to {output_jsonl_path}")


if __name__ == "__main__":
    typer.run(convert_csv_to_jsonl)
