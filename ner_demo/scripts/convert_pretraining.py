import csv
import srsly
from pathlib import Path
import typer


def convert_csv_to_jsonl(
    input_csv_path: Path,
    output_jsonl_path: Path,
):
    """
    Convert a specified text column from a CSV file to a JSONL file suitable for spaCy pretraining.

    Args:
    input_csv_path (Path): The path to the input CSV file.
    output_jsonl_path (Path): The path where the output JSONL file should be saved.
    """
    texts = []
    with input_csv_path.open("r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            text = row["description"].strip()
            if text:  # Ensure the text is not empty
                texts.append({"text": text})

    srsly.write_jsonl(output_jsonl_path, texts)
    print(f"Converted texts from {input_csv_path} to {output_jsonl_path}")


if __name__ == "__main__":
    typer.run(convert_csv_to_jsonl)
