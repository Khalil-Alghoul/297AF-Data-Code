from Bio import SeqIO
import re

INPUT_FILE = "blast_raw_sequences.fasta"
OUTPUT_FILE = "ampC_filtered.fasta"

MIN_LEN = 250
MAX_LEN = 500
MAX_SEQUENCES = 25

def is_bad_annotation(header):
    bad_keywords = ["fragment", "partial"]
    header_lower = header.lower()
    return any(word in header_lower for word in bad_keywords)

def main():
    valid_sequences = []

    # Step 1: Collect ALL reasonable sequences
    for record in SeqIO.parse(INPUT_FILE, "fasta"):
        header = record.description
        seq_len = len(record.seq)

        if seq_len < MIN_LEN or seq_len > MAX_LEN:
            continue

        if is_bad_annotation(header):
            continue

        valid_sequences.append(record)

    print(f"Total valid sequences found: {len(valid_sequences)}")

    # Step 2: Just take the first N
    selected = valid_sequences[:MAX_SEQUENCES]

    # Save output
    SeqIO.write(selected, OUTPUT_FILE, "fasta")

    print(f"Selected {len(selected)} sequences")
    print(f"Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()