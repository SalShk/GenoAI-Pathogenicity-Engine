# GenoAI Pathogenicity Engine

[![Tests](https://img.shields.io/github/actions/workflow/status/salshk/GenoAI-Pathogenicity-Engine/test.yaml?branch=main)](https://github.com/salshk/GenoAI-Pathogenicity-Engine/actions/workflows/test.yaml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![BioContextAI - Registry](https://img.shields.io/badge/Registry-package?style=flat&label=BioContextAI&labelColor=%23fff&color=%233555a1&link=https%3A%2F%2Fbiocontext.ai%2Fregistry)](https://biocontext.ai/registry)

**GenoAI Pathogenicity Engine** is an advanced clinical reasoning engine designed to address the core challenge in modern genomics: evidence synthesis under uncertainty. It functions as a semantic reasoning layer, transforming raw, heterogeneous variant data into a structured, multi-dimensional "Evidence Profile" ready for clinical review or consumption by higher-order AI agents.

## Architecture & Usage Model

This project follows a professional **"Open Core"** model, separating the open-source framework from the proprietary core logic.

* **Public Repository (This one):** Contains the complete, open-source FastAPI server framework, API logic, and testing suite. It is designed to be transparent, extensible, and ready for collaboration.
* **Private Repository:** Contains the proprietary `genoai_engine_private` package, which includes the core scientific scoring algorithms that power this server.

## The Problem: The Synthesis Bottleneck

A clinical geneticist must act as a "committee of one," mentally integrating dozens of conflicting data points for every variant. This qualitative process is a major bottleneck that is not scalable or easily reproducible. The current ecosystem of genomic tools excels at data aggregation but lacks a standardized framework for this crucial reasoning step.

## The Solution: A Structured Reasoning Engine

The GenoAI engine is architected to be this missing reasoning layer. It assesses each variant against five core evidence dimensions, inspired by ACMG/AMP guidelines: Population, Molecular, Clinical, Evolutionary, and Gene-level Intolerance. The engine's output is a quantitative "Evidence Profile" containing a score for each dimension and a final classification.

## Access & Licensing

The open-source framework in this repository is licensed under the MIT License. The core **`genoai_engine_private`** package is proprietary.

* **For Academic & Research Collaboration:** We are open to collaboration. Please contact us at **[salehshekari@gmail.com]** to discuss access for non-commercial research purposes.
* **For Commercial Use:** A commercial license is required. Please contact us at **[salehshekari@gmail.com]** for information on licensing and integration.

## Installation (Open-Source Framework Only)

This guide is for contributors who want to work on the open-source server framework without the core private engine. The core analysis functionality will be non-operational, but you can still run and test the API endpoints.

1.  **Clone this public repository:**
    ```bash
    git clone [https://github.com/salshk/GenoAI-Pathogenicity-Engine.git](https://github.com/salshk/GenoAI-Pathogenicity-Engine.git)
    cd GenoAI-Pathogenicity-Engine
    ```
2.  **Install the public dependencies:**
    ```bash
    uv pip install -r requirements.txt
    ```
    *Note: The `uv pip install` command will skip the private `genoai-engine-private` package, as you do not have access to it.*

## Installation for Collaborators

This guide is for collaborators who have been granted a Personal Access Token (PAT) for the private repository.

1.  **Configure Git with your PAT:** Open your terminal and run this command with your token. This tells Git to use the token for authentication when it encounters a GitHub URL.
    ```bash
    git config --global url."https://genoai-api-user:<YOUR_PRIVATE_REPO_TOKEN>@github.com".insteadOf "[https://github.com](https://github.com)"
    ```
2.  **Clone this public repository:**
    ```bash
    git clone [https://github.com/salshk/GenoAI-Pathogenicity-Engine.git](https://github.com/salshk/GenoAI-Pathogenicity-Engine.git)
    cd GenoAI-Pathogenicity-Engine
    ```
3.  **Create a virtual environment and install all dependencies (including the private engine):**
    ```bash
    uv venv
    uv pip install -r requirements.txt
    pip install -e .
    ```

## Usage

To run the FastAPI web server, ensure your virtual environment is active and run the following command from the root project directory:
```bash
python -m genoai_pathogenicity_engine.main run --transport http --port 8001

## API Example (using cURL)
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
**We welcome contributions and collaborations on the open-source framework. Please [open an issue](https://github.com/salshk/GenoAI-Pathogenicity-Engine/issues) to discuss your ideas.**
