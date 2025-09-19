# GenoAI Pathogenicity Engine

[![Tests](https://img.shields.io/github/actions/workflow/status/salshk/GenoAI-Pathogenicity-Engine/test.yaml?branch=main)](https://github.com/salshk/GenoAI-Pathogenicity-Engine/actions/workflows/test.yaml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![BioContextAI - Registry](https://img.shields.io/badge/Registry-package?style=flat&label=BioContextAI&labelColor=%23fff&color=%233555a1&link=https%3A%2F%2Fbiocontext.ai%2Fregistry)](https://biocontext.ai/registry)

**GenoAI Pathogenicity Engine** is an advanced clinical reasoning engine designed to address the core challenge in modern genomics: evidence synthesis under uncertainty. It functions as a semantic reasoning layer, transforming raw, heterogeneous variant data into a structured, multi-dimensional "Evidence Profile" ready for clinical review or consumption by higher-order AI agents.

## The Problem: The Synthesis Bottleneck

A clinical geneticist must act as a "committee of one," mentally integrating dozens of conflicting data points (molecular, population, clinical, etc.) for every variant. This qualitative process is a major bottleneck that is not scalable or easily reproducible. The current ecosystem of genomic tools excels at data aggregation but lacks a standardized framework for this crucial reasoning step.

## The Solution: A Structured Reasoning Engine

The GenoAI engine is architected to be this missing reasoning layer. It assesses each variant against five core evidence dimensions, inspired by ACMG/AMP guidelines:

1.  **Population Evidence:** How rare is the variant?
2.  **Molecular Impact:** What is the predicted functional consequence?
3.  **Clinical Precedent:** Has it been seen in patients before?
4.  **Evolutionary Constraint:** Is the position highly conserved?
5.  **Gene-level Intolerance:** Is the gene sensitive to variation?

The engine's output is a quantitative "Evidence Profile" containing a score for each dimension, a final pathogenicity score, and a clear classification (e.g., `Pathogenic`, `VUS_High_Risk`).

## Key Features

* **Multi-Dimensional Analysis:** Provides a transparent, five-component score that explains *why* a variant is classified a certain way.
* **Context-Aware Logic:** Applies different rules and weighting for different variant classes (e.g., Missense vs. Loss-of-Function).
* **Agent-Ready Output:** The "Evidence Profile" is specifically designed as a rich, structured input for agentic AI workflows and MCP servers.
* **Flexible & Robust API:** The server can handle variations in input column names and variant ID formats.

## Installation for Development

This project uses a `src` layout and is managed with modern Python tooling.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/salshk/GenoAI-Pathogenicity-Engine.git](https://github.com/salshk/GenoAI-Pathogenicity-Engine.git)
    cd GenoAI-Pathogenicity-Engine
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the project in editable mode:**
    ```bash
    pip install -e .
    ```

## Usage

To run the FastAPI web server:

1.  Ensure your virtual environment is active.
2.  Run the server from the root project directory:
    ```bash
    python -m genoai_pathogenicity_engine.main run --transport http --port 8001
    ```
3.  The API documentation will be available at **`http://127.0.0.1:8001/docs`**.

### API Example (using cURL)

```bash
curl -X POST "[http://127.0.0.1:8001/analyze/](http://127.0.0.1:8001/analyze/)" \
-H "Content-Type: application/json" \
-d '[
  {
    "variant_id": "chr7-140753336-A-T",
    "Consequence": "missense_variant",
    "ZYG": "Het",
    "IMPACT": "MODERATE",
    "genename": "BRAF",
    "REVEL": 0.964,
    "CADD_PHRED": 35.0,
    "MAX_AF": 0.00002,
    "CLIN_SIG": "Pathogenic",
    "clinvar_review": "criteria_provided,_multiple_submitters,_no_conflicts",
    "clinvar_clnsig": "Pathogenic",
    "clinvar_hgvs": "NC_000007.14:g.140753336A>T",
    "clinvar_id": "13961",
    "clinvar_trait": "Melanoma",
    "clinvar_var_source": "OMIM",
    "GENE_PHENO": "Cardiofaciocutaneous syndrome 1",
    "CADD_RAW": 6.1,
    "DANN_score": 0.998,
    "Eigen_phred_coding": 15.2,
    "GenoCanyon_score": 0.98,
    "PrimateAI_score": 0.92,
    "PrimateAI": 0.9,
    "am_pathogenicity": 0.95,
    "BayesDel_noAF_pred": 0.85,
    "ClinPred_pred": 0.99,
    "DEOGEN2_pred": 0.91,
    "SIFT": "deleterious(0)",
    "SIFT_pred": "D",
    "PolyPhen": "probably_damaging(1.0)",
    "Polyphen2_HVAR_pred": "D",
    "FATHMM_pred": "D",
    "fathmm_MKL_coding_pred": "D",
    "LRT_pred": "D",
    "M_CAP_pred": "D",
    "MetaLR_pred": "D",
    "MetaSVM_pred": "D",
    "MutationAssessor_pred": "high",
    "MutationTaster_pred": "disease_causing",
    "PROVEAN_pred": "Deleterious",
    "am_class": "pathogenic",
    "GERP_RS": 5.7,
    "phastCons100way_vertebrate": 1.0,
    "phyloP100way_vertebrate": 8.1,
    "SiPhy_29way_logOdds": 20.0,
    "MaxEntScan_diff": 0.1,
    "SpliceAI_pred": 0.02,
    "SpliceVault_SpliceAI_delta": 0.0,
    "SpliceVault_site_max_depth": 0.0,
    "SpliceVault_site_sample_count": 0.0,
    "SpliceVault_site_pos": 0.0,
    "SpliceVault_out_of_frame_events": "no",
    "SpliceVault_site_type": "-",
    "SpliceVault_top_events": "-",
    "LoF": "LC",
    "LoF_filter": "-",
    "LoF_flags": "-",
    "LoF_info": "-",
    "gnomADe_AF": 0.00001,
    "gnomADg_AF": 0.00002,
    "AF": 0.000015,
    "lof_pLI": 0.0,
    "lof_pNull": 1.0,
    "lof_obs": 28,
    "lof_exp": 30.5,
    "lof_oe": 0.91,
    "lof_z_score": -0.8,
    "lof_oe_ci_lower": 0.6,
    "lof_oe_ci_upper": 1.3,
    "mis_obs": 195,
    "mis_exp": 150.7,
    "mis_oe": 1.29,
    "mis_z_score": -4.2,
    "mis_oe_ci_lower": 1.1,
    "mis_oe_ci_upper": 1.5,
    "mis_pphen_obs": 120,
    "mis_pphen_exp": 100.0,
    "mis_pphen_oe": 1.2,
    "mis_pphen_z_score": -3.1,
    "DOMAINS": "Pkinase_Tyr:IPR020635"
  }
]'
```

## Contributing

We welcome contributions and collaborations. Please [open an issue](https://github.com/salshk/GenoAI-Pathogenicity-Engine/issues) to discuss your ideas.

## License

This project is licensed under the MIT License.