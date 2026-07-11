# TP53 Bioinformatics Pipeline — Project Report

## Introduction

TP53 is the tumour suppressor gene, one of the most frequently studied genes in cancer biology. It encodes a transcription factor that regulates the cell cycle and triggers apoptosis in response to DNA damage, making it central to maintaining genomic stability. Mutations in TP53 are found across a wide range of human cancers, making it one of the most important genes in oncology research. This project explores TP53's sequence characteristics and connects those findings to current research literature via an automated pipeline.

## Methods

The pipeline was built in Python using BioPython for sequence handling and the NCBI Entrez API for literature retrieval. It runs in four stages:

1. **Load sequence** — reads the TP53 FASTA file (NM_000546.6)
2. **Extract features** — calculates GC content across a sliding window (window size 100 bp, step size 50 bp) and identifies all Open Reading Frames (ORFs) across three forward reading frames
3. **Fetch interpretation** — searches PubMed for TP53-related abstracts and summarizes them using the OpenAI API (gpt-4o-mini)
4. **Generate report** — compiles sequence metrics, ORF annotations, and the AI-generated interpretation into a single output file

**Tools used:** Python 3.x, BioPython, NCBI Entrez API, OpenAI API (gpt-4o-mini)

## Results

- **Gene ID:** lcl|NM_000546.6_gene_1
- **Sequence Length:** 2512 bp
- **GC Content:** 53.38%
- **Total ORFs Found:** 36
- **Longest ORF:** 1182 bp (position 142–1324)

### Top 5 ORFs by length

| ORF # | Start | Stop | Length (bp) |
|-------|-------|------|--------------|
| 9     | 142   | 1324 | 1182         |
| 10    | 259   | 1324 | 1065         |
| 11    | 271   | 1324 | 1053         |
| 12    | 337   | 1324 | 987          |
| 13    | 538   | 1324 | 786          |

The full list of all 36 detected ORFs is provided in the Appendix.

## Interpretation

The pipeline searched PubMed for "TP53" and retrieved the 5 most recent matching abstracts, which were summarized using AI into the following categories:

### Biological Function
The retrieved abstracts covered several distinct research areas connected to TP53 either directly or through related pathways: ERBB2 amplification as a biomarker in endometrial cancer, taurine metabolism genes (CCND1, LYN) in lupus nephritis, a compound (4-chloro-7-nitrobenzofurazan) that activates the p53 pathway to induce apoptosis in fibrosarcoma, tobacco-associated tumor mutational burden (including TP53 mutations) in lung adenocarcinoma, and population-specific somatic mutation patterns in colorectal cancer.

### Disease Relevance
Findings spanned endometrial cancer disparities linked to ERBB2 amplification, the role of taurine metabolism in lupus nephritis, fibrosarcoma treatment resistance, tobacco-linked lung adenocarcinoma risk, and population-level variation in colorectal cancer mutation profiles.

### Research Applications
Applications discussed included genomic profiling for personalized endometrial cancer treatment, biomarker development for lupus nephritis diagnosis, redox-targeting therapeutics for fibrosarcoma, tobacco-exposure biomarkers for lung cancer immunotherapy, and comparative genomic studies to guide inclusive colorectal cancer care.

## Conclusions

Structurally, TP53's longest identified ORF (1182 bp) accounts for nearly 47% of the total 2512 bp sequence, consistent with TP53 containing a substantial coding region relative to its overall gene length. The moderately high GC content (53.38%) falls within the expected range for human coding sequences.

On the literature side, only one of the five retrieved abstracts (the lung adenocarcinoma / tobacco exposure study) discussed TP53 directly as a subject of investigation — the remaining four were only tangentially connected, either through shared pathways (e.g. the p53 apoptosis pathway in the fibrosarcoma study) or unrelated diseases that happened to mention TP53 in passing. This suggests that a single-keyword PubMed search for "TP53" is broad enough to surface abstracts where the gene is mentioned but not the central focus, rather than literature specifically characterizing TP53's own biology.

## What I Learned

Working through this pipeline reinforced how the specificity of a search query directly affects the relevance of downstream AI interpretation — a broad search term can return abstracts that are only loosely related to the target gene, which then get summarized as though they were core findings. A more targeted search (for example, using PubMed field tags like `TP53[Title]` or adding qualifiers such as "TP53 AND (mutation OR tumor suppressor)") would likely produce abstracts more directly focused on TP53 itself.

I also worked through several environment and debugging challenges over the course of this project: installing packages correctly via pip versus mistakenly running commands inside the Python interactive shell, handling OpenAI API billing and rate limits, keeping API keys out of version control using a separate `api_key.txt` file and `.gitignore`, and structuring a multi-file script into a single runnable pipeline. These troubleshooting steps were as valuable to the learning process as the bioinformatics content itself.

## Appendix

### Full ORF Table

| ORF # | Start | Stop | Length (bp) |
|-------|-------|------|--------------|
| 1  | 207  | 225  | 18   |
| 2  | 297  | 309  | 12   |
| 3  | 1518 | 1551 | 33   |
| 4  | 1770 | 1788 | 18   |
| 5  | 2022 | 2499 | 477  |
| 6  | 2025 | 2499 | 474  |
| 7  | 2232 | 2499 | 267  |
| 8  | 2259 | 2499 | 240  |
| 9  | 142  | 1324 | 1182 |
| 10 | 259  | 1324 | 1065 |
| 11 | 271  | 1324 | 1053 |
| 12 | 337  | 1324 | 987  |
| 13 | 538  | 1324 | 786  |
| 14 | 619  | 1324 | 705  |
| 15 | 646  | 1324 | 678  |
| 16 | 850  | 1324 | 474  |
| 17 | 868  | 1324 | 456  |
| 18 | 877  | 1324 | 447  |
| 19 | 1159 | 1324 | 165  |
| 20 | 1291 | 1324 | 33   |
| 21 | 1579 | 1585 | 6    |
| 22 | 1588 | 1633 | 45   |
| 23 | 1717 | 1756 | 39   |
| 24 | 1762 | 1771 | 9    |
| 25 | 1804 | 1822 | 18   |
| 26 | 263  | 272  | 9    |
| 27 | 323  | 509  | 186  |
| 28 | 677  | 881  | 204  |
| 29 | 698  | 881  | 183  |
| 30 | 761  | 881  | 120  |
| 31 | 800  | 881  | 81   |
| 32 | 1112 | 1175 | 63   |
| 33 | 1175 | 1250 | 75   |
| 34 | 1196 | 1250 | 54   |
| 35 | 1568 | 1604 | 36   |
| 36 | 2240 | 2270 | 30   |

### Code

See `day4_pipeline.py` in this repository for the full pipeline implementation.
