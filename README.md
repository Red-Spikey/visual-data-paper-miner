# Figure-Centered Literature Mining Pipeline

This repository contains the code and manuscript for a figure-centered approach to scientific literature mining. Traditional search methods rely primarily on keyword matching within abstracts or body text, which often retrieves articles that merely mention target keywords without presenting actual data. 

This pipeline addresses that limitation by aggressively filtering bibliographic datasets based on the information conveyed through figures and their associated captions. By utilizing Optical Character Recognition (OCR) to validate the presence of terminology within the visual content itself, the pipeline ensures that retained articles contain substantive results relevant to the user's domain.

## Methodology

The filtering framework processes a corpus of scientific articles through three sequential stages:

1. **Article Corpus Construction:** Reads a list of DOIs from an initial broad search (e.g., Scopus) and retrieves full-text articles in XML format using the Elsevier API.
2. **Figure Extraction and Caption-Based Filtering:** Parses the XML documents to extract embedded figures and cleans their associated captions. Applies a whole-word, case-insensitive keyword match to the captions, retaining only figures that describe relevant parameters.
3. **OCR-Based Validation:** Preprocesses the retained figure images (grayscale conversion and contrast enhancement) and extracts embedded text using Pytesseract. Figures are retained only if the OCR text independently confirms the presence of the target keywords (e.g., axis labels, plot legends).

## Domain Application

The current keyword vocabulary provided in this repository is configured for the **Aerodynamics and Computational Fluid Dynamics (CFD)** domain. It specifically filters for plots containing data such as `Mach number`, `lift coefficient`, `pressure field`, and `Reynolds number`.

The method requires only a domain-specific keyword set and can be applied across different research areas without modification to the underlying underlying pipeline.

## Repository Structure

* `main.py` / `pipeline.ipynb` - The primary extraction and filtering scripts.
* `scopus.csv` - Example input dataset containing initial DOIs.
* `keywords.py` - Configurable vocabulary list for the two-stage filter.
* `paper/` - Contains the LaTeX source code and compiled PDF of the accompanying manuscript ("What Figures Reveal: A More Reliable Way to Identify Relevant Scientific Papers").
