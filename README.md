# visual-data-paper-miner

A figure-centered literature mining pipeline that identifies truly relevant scientific papers by validating keyword presence not just in text, but directly within figure images using OCR.

---

## The Problem

Standard literature search returns papers that *mention* your keywords — not necessarily papers that *report results* for them. A paper can reference a term in its introduction or methodology without ever presenting empirical data for it. This tool fixes that.

---

## How It Works

The pipeline runs in two filtering stages after retrieving full-text XMLs from a bibliographic corpus (e.g. Scopus exports):

```
Initial DOI Pool
      │
      ▼
 XML Retrieval (via publisher API)
      │
      ▼
 Stage 1 — Caption Filter
 (keyword match in figure captions)
      │
      ▼
 Stage 2 — OCR Visual Validation
 (keyword match inside the figure image itself)
      │
      ▼
 Final Relevant Papers
```

1. **Corpus Construction** — Start from a `scopus.csv` export. DOIs are extracted and full-text XMLs are fetched via the publisher API.
2. **Figure Extraction** — Figures and their captions are parsed from each XML document.
3. **Stage 1: Caption Filter** — Figures are kept only if at least one target keyword appears in the caption text.
4. **Stage 2: OCR Validation** — Each shortlisted figure image is OCR-processed (Tesseract). The figure is retained only if the keyword also appears in the image itself (axis labels, legends, annotations).
5. **Output** — Papers that pass both stages are written to `relevant_papers.csv`.

---

## Repo Structure

```
visual-data-paper-miner/
│
├── Acoustics AND Ultrasonics/
│   ├── pipeline/
│   │   ├── csvs/                  # Intermediate CSV outputs per stage
│   │   ├── xmls/                  # Downloaded full-text XML files
│   │   ├── relevant_papers.csv    # Final filtered papers
│   │   └── tracker.csv            # Per-paper processing log
│   ├── Acoustics AND Ultrasonics.ipynb   # Domain-specific run notebook
│   └── scopus.csv                 # Raw Scopus export for this domain
│
├── Electrochemistry/              # Same structure (in progress)
│
├── Heat Transfer and Thermal Conductivity/
│   ├── pipeline/
│   ├── Heat Transfer and Thermal Conductivity.ipynb
│   └── scopus.csv
│
├── Next-Generation Batteries (Lithium-ion &...)/
│   └── ...                        # Same structure
│
├── general.ipynb                  # Shared utility functions and pipeline core
└── readme.md
```

---

## Results (from paper evaluation)

| Domain | Initial Pool | XML Errors | After Stage 1 | After Stage 2 | Final Relevant |
|---|---|---|---|---|---|
| Acoustics & Ultrasonics | 5000 | 4699 | 205 | 48 | **48** |
| Heat Transfer | 2429 | 2350 | 75 | 51 | **51** |
| Next-Gen Batteries | 5000 | 4129 | 566 | 314 | **314** |

The high XML error rate is expected — it reflects publisher paywalls and access restrictions on bulk Scopus exports.

---

## Requirements

- Python 3.x
- `pytesseract` + Tesseract OCR installed on system
- `Pillow` for image preprocessing
- `lxml` or `BeautifulSoup` for XML parsing
- Publisher API access (e.g. Elsevier API key for full-text retrieval)
- Scopus account for initial DOI export

---

## Usage

1. Export search results from Scopus as `scopus.csv` into the relevant domain folder.
2. Open the domain-specific `.ipynb` notebook.
3. Set your keyword vocabulary in the config cell.
4. Run all cells — the pipeline will populate `pipeline/xmls/`, `pipeline/csvs/`, and write `relevant_papers.csv`.

---

## Citation

> Tripathi, S., Dixit, A., Prathamesh, & Arvind. *What Figures Reveal: A More Reliable Way to Identify Relevant Scientific Papers.* IIT Kanpur.

---

## Contact

Aman Dixit — amandixit23@iitk.ac.in  
Material Science and Engineering, IIT Kanpur
