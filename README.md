# TP53 Bioinformatics Pipeline

A Python pipeline that downloads, analyzes, and interprets the TP53 tumor suppressor gene using BioPython and AI tools.

## Objective

To build an end-to-end bioinformatics workflow that converts a raw FASTA sequence into a structured biological report — covering sequence metrics, feature extraction (GC content, ORFs), and AI-assisted literature interpretation via PubMed.

## Tools Used

- Python 3.x
- BioPython (SeqIO, SeqUtils, Entrez)
- NCBI Entrez API (PubMed search + abstract fetching)
- OpenAI API (gpt-4o-mini) for literature summarization

## How to Run

1. Install dependencies:
   ```
   pip install biopython openai
   ```
2. Place your FASTA file (e.g. `sequence.fasta`) in the same folder as the script.
3. Create a file called `api_key.txt` in the same folder containing only your OpenAI API key.
4. Run:
   ```
   python day4_pipeline.py
   ```
5. Output saved to: `tp53_report.txt`

## Results

<!-- TODO: replace with YOUR actual numbers from tp53_report.txt -->
- Sequence Length: ___ bp
- GC Content: ___%
- ORFs Found: ___
- Longest ORF: ___ bp (position ___–___)
- Key Finding: <!-- one sentence on what stood out -->

## Author

Sania Ramphal
