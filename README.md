* This change is to trigger the CI/CD pipeline.
# GenoAI Pathogenicity Engine

[![Tests](https://img-shields.io/github/actions/workflow/status/salshk/GenoAI-Pathogenicity-Engine/test.yaml?branch=main)](https://github.com/salshk/GenoAI-Pathogenicity-Engine/actions/workflows/test.yaml)
[![License: MIT](https://img-shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![BioContextAI - Registry](https://img-shields.io/badge/Registry-package?style=flat&label=BioContextAI&labelColor=%23fff&color=%233555a1&link=https%3A%2F%2Fbiocontext.ai%2Fregistry)](https://biocontext.ai/registry)

**GenoAI Pathogenicity Engine** is an advanced clinical reasoning engine designed to address the core challenge in modern genomics: evidence synthesis under uncertainty. It functions as a semantic reasoning layer, transforming raw, heterogeneous variant data into a structured, multi-dimensional "Evidence Profile" ready for clinical review or consumption by higher-order AI agents.

## Architecture & Usage Model

This project follows a professional **"Open Core"** model, separating the open-source framework from the proprietary core logic.

* **Public Repository (This one):** Contains the complete, open-source MCP server framework, API logic, and testing suite. It is designed to be transparent, extensible, and ready for collaboration.
* **Private Repository:** Contains the proprietary `genoai_engine_private` package, which includes the core scientific scoring algorithms that power this server.

## The Problem: The Synthesis Bottleneck

A clinical geneticist must act as a "committee of one," mentally integrating dozens of conflicting data points for every variant. This qualitative process is a major bottleneck that is not scalable or easily reproducible. The current ecosystem of genomic tools excels at data aggregation but lacks a standardized framework for this crucial reasoning step.

## The Solution: A Structured Reasoning Engine

The GenoAI engine is architected to be this missing reasoning layer. It assesses each variant against five core evidence dimensions, inspired by ACMG/AMP guidelines: Population, Molecular, Clinical, Evolutionary, and Gene-level Intolerance. The engine's output is a quantitative "Evidence Profile" containing a score for each dimension and a final classification.

## Access & Licensing

The open-source framework in this repository is licensed under the MIT License. Usage of the core **`genoai_engine_private`** requires a separate license and access token.

* **For Academic & Research Collaboration:** We are open to collaboration. Please contact us at **[salehshekari@gmail.com]** to discuss access for non-commercial research purposes.
* **For Commercial Use:** A commercial license is required. Please contact us at **[salehshekari@gmail.com]** for information on licensing and integration.

## Installation for Collaborators

**Prerequisite:** This server requires access to the `genoai_engine_private` package. Please see the 'Access & Licensing' section for details on obtaining an access token.

1.  **Configure `pip`** to access the private repository using the provided token.
2.  **Clone this public repository:**
    ```bash
    git clone [https://github.com/salshk/GenoAI-Pathogenicity-Engine.git](https://github.com/salshk/GenoAI-Pathogenicity-Engine.git)
    cd GenoAI-Pathogenicity-Engine
    ```
3.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
4.  **Install the project and all dependencies (including the private engine):**
    ```bash
    pip install -e .
    ```

## Usage

To run the FastAPI web server, ensure your virtual environment is active and run the following command from the root project directory:
```bash
python -m genoai_pathogenicity_engine.main run --transport http --port 8001
```
The API documentation will then be available at **`http://127.0.0.1:8001/docs`**.

### API Example (using cURL)

```bash
curl -X POST "[http://127.0.0.1:8001/analyze/](http://127.0.0.1:8001/analyze/)" \
-H "Content-Type: application/json" \
-d '[
  {
    "variant_id": "chr7-140753336-A-T",
    "Consequence": "missense_variant",
    "REVEL": 0.964,
    "CADD_PHRED": 35.0,
    "MAX_AF": 0.00002,
    "...": "..." 
  }
]'
```

## Contributing

We welcome contributions and collaborations on the open-source framework. Please [open an issue](https://github.com/salshk/GenoAI-Pathogenicity-Engine/issues) to discuss your ideas.
