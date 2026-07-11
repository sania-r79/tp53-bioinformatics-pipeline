# TP53 Bioinformatics Pipeline — Project Report

## Introduction

<!-- What TP53 is and why it matters -->
TP53 is the tumour suppressor gene, one of the most frequently studied genes in cancer biology. It encodes a transcription factor that regulates the cell cycle and triggers apoptosis in response to DNA damage, making it central to maintaining genomic stability. This project explores TP53's sequence characteristics and connects those findings to current research literature.

## Methods

<!-- Tools used, approach taken, pipeline overview -->
The pipeline was built in Python using BioPython for sequence handling and the NCBI Entrez API for literature retrieval. It runs in four stages:

1. **Load sequence** — reads the TP53 FASTA file
2. **Extract features** — calculates GC content across a sliding window and identifies Open Reading Frames (ORFs)
3. **Fetch interpretation** — searches PubMed for TP53-related abstracts and summarizes them using the OpenAI API (gpt-4o-mini)
4. **Generate report** — compiles sequence metrics, ORF annotations, and the AI-generated interpretation into a single output file

## Results

<!-- Actual outputs: numbers, figures, annotations. This is what the data SHOWS, not what it means. -->
- Sequence Length: ___ bp
- GC Content: ___%
- ORFs Found: ___
- Longest ORF: ___ bp (position ___–___)

| ORF # | Start | Stop | Length (bp) |
|-------|-------|------|--------------|
|       |       |      |              |

## Interpretation

<!-- What the AI summarized: function, disease, research -->
### Biological Function
<!-- summarize from your AI output -->

### Disease Relevance
<!-- summarize from your AI output -->

### Research Applications
<!-- summarize from your AI output -->

## Conclusions

<!-- What you found, what it MEANS, what comes next. Do not just repeat the Results section. -->


## What I Learned

<!-- Honest reflection — skills gained, challenges faced -->


## Appendix

<!-- Raw ORF table, full AI output, code snippet -->

### Full AI Output
```
<!-- paste full text output here -->
```

### Code
See `day4_pipeline.py` in this repository.
