from Bio import SeqIO, Entrez
from Bio.SeqUtils import gc_fraction
from openai import OpenAI


# ==========================================
# SETUP
# ==========================================

with open("api_key.txt", "r") as f:
    my_key = f.read().strip()

client = OpenAI(api_key=my_key)

Entrez.email = "saniaramphal79@gmail.com"


# ==========================================
# Helper 1: Sliding Window GC
# ==========================================

def sliding_window_gc(sequence, window=100):

    gc_values = []
    positions = []

    for i in range(0, len(sequence) - window, 50):

        fragment = sequence[i:i + window]
        gc = gc_fraction(fragment) * 100

        gc_values.append(gc)
        positions.append(i)

    return (gc_values, positions)


# ==========================================
# Helper 2: ORF finder
# ==========================================

def find_orfs(sequence):

    orfs = []
    start = "ATG"
    stops = ["TAA", "TAG", "TGA"]

    for frame in range(3):

        i = frame

        while i < len(sequence) - 3:

            codon = str(sequence[i:i + 3])

            if codon == start:

                j = i + 3

                while j < len(sequence) - 3:

                    stop = str(sequence[j:j + 3])

                    if stop in stops:

                        length = j + 3 - i
                        orfs.append((i, j + 3, length))
                        break

                    j += 3

            i += 3

    return orfs


# ==========================================
# Helper 3: PubMed fetch
# ==========================================

def fetch_pubmed_abstracts(gene_name):

    handle = Entrez.esearch(
        db="pubmed",
        term=gene_name,
        retmax=5
    )
    record = Entrez.read(handle)
    ids = record["IdList"]

    print("PubMed IDs:", ids)

    fetch_handle = Entrez.efetch(
        db="pubmed",
        id=ids,
        rettype="abstract",
        retmode="text"
    )
    abstracts = fetch_handle.read()

    return abstracts


# ==========================================
# Helper 4: AI summary (real OpenAI call)
# ==========================================

def ai_summarize(abstracts):

    prompt = f"""
You are a bioinformatics assistant.

Summarize into:
1. Biological Function
2. Disease Relevance
3. Research Applications

{abstracts}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    summary_text = response.choices[0].message.content

    interpretation = {
        "AI Summary": [summary_text]
    }

    return interpretation


# ==========================================
# Module 1: Load sequence
# ==========================================

def load_sequence(filepath):
    record = SeqIO.read(filepath, "fasta")
    return record


# ==========================================
# Module 2: Extract features
# ==========================================

def extract_features(record):

    gc_values, positions = sliding_window_gc(record.seq)
    orfs = find_orfs(record.seq)

    return (gc_values, positions, orfs)


# ==========================================
# Module 3: Get interpretation
# ==========================================

def get_interpretation(gene_name):

    abstracts = fetch_pubmed_abstracts(gene_name)
    interpretation = ai_summarize(abstracts)

    return interpretation


# ==========================================
# Report Generator
# ==========================================

def generate_report(record, orfs, interpretation):

    filepath = r"C:\Users\prene\OneDrive\Desktop\Bioinformatics\tp53_report.txt"

    with open(filepath, "w") as f:

        f.write("=" * 50 + "\n")
        f.write("BIOINFORMATICS PIPELINE REPORT\n")
        f.write("=" * 50 + "\n\n")

        # Section 1: Sequence Summary
        f.write("SEQUENCE SUMMARY\n")
        f.write(f"Gene ID: {record.id}\n")
        f.write(f"Length: {len(record.seq)} bp\n")
        f.write(f"GC Content: {gc_fraction(record.seq) * 100:.2f}%\n\n")

        # Section 2: ORF Annotations
        f.write("ORF ANNOTATIONS\n")
        for i, (start, stop, length) in enumerate(orfs):
            f.write(f"ORF {i + 1}: {start}-{stop} | {length} bp\n")

        # Section 3: Biological Interpretation
        f.write("\nBIOLOGICAL INTERPRETATION\n")
        for category, points in interpretation.items():
            f.write(f"\n{category}:\n")
            for point in points:
                f.write(f" - {point}\n")


# ==========================================
# Main Pipeline
# ==========================================

def run_pipeline(fasta_file, gene_name):

    print("=" * 50)
    print(f"Running pipeline for: {gene_name}")
    print("=" * 50)

    # Step 1
    print("\n[1/3] Loading sequence...")
    record = load_sequence(fasta_file)
    print(f"ID: {record.id} | Length: {len(record.seq)} bp")

    # Step 2
    print("\n[2/3] Extracting features...")
    gc_values, positions, orfs = extract_features(record)
    print(f"ORFs found: {len(orfs)}")
    if orfs:
        print(f"Longest ORF: {max(orfs, key=lambda x: x[2])}")

    # Step 3
    print("\n[3/3] Fetching AI interpretation...")
    interpretation = get_interpretation(gene_name)

    generate_report(record, orfs, interpretation)

    print("\nPipeline complete. Report saved.")


# ==========================================
# Run
# ==========================================


run_pipeline(
    r"C:\Users\prene\OneDrive\Desktop\Bioinformatics\sequence.fasta",
    "TP53"
)