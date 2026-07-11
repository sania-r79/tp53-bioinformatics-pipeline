# TP53 Bioinformatics Pipeline

A Python pipeline that downloads, analyzes, and interprets the TP53 tumor suppressor gene using BioPython and OpenAI tools.

## Objective

To build a complete bioinformatics pipeline that converts a raw FASTA sequence into a structured biological report which covers sequence description, feature extraction (GC content, ORFs), and AI-assisted literature interpretation via PubMed.

## Tools Used

- Python 3.14.5
- BioPython (SeqIO, SeqUtils, Entrez)
- NCBI Entrez API (PubMed search + abstract retrieval)
- OpenAI API (gpt-4o-mini) for literature summarization

## How to Run

1. Install dependencies:
   ```
   pip install biopython openai
   ```
2. Place your FASTA file (e.g. "sequence.fasta") in the same folder as the script.
3. Create a file called "api_key.txt" in the same folder containing only your OpenAI API key.
4. Run:
   ```
   python day4_pipeline.py
   ```
5. Output saved to: `tp53_report.txt`

## Results

- Sequence Length: 2512 bp
- GC Content: 53.38%
- ORFs Found: 36
- Longest ORF: 1182 bp (position 142-1324)
- Key Finding: The longest ORF covers almost 47% of the total sequence length. This indicates that a substantial coding region is consistent with the TP53 coding structure.

## Author

Sania Ramphal
