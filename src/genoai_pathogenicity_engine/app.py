from fastapi import FastAPI, Body
from typing import List

from .mcp import get_mcp_manifest
# Import your tool function from the 'tools' package
from .tools import run_genoai_analysis

# This is the main FastAPI application object
description = """
An advanced clinical reasoning engine designed to address the challenge of genomic variant interpretation.

This service synthesizes dozens of annotations according to ACMG/AMP-aligned guidelines,
transforming raw data into a structured, multi-dimensional 'Evidence Profile'. Each variant
is assessed across five key dimensions: Population, Molecular, Clinical, Evolutionary, and
Gene-level Constraint.

The resulting profile provides a robust, reproducible, and transparent basis for
clinical decision-making and for consumption by higher-order AI agents.
"""

app = FastAPI(
    title="GenoAI Pathogenicity Engine",
    description=description,
    version="1.2.0", 
)

@app.get("/mcp", summary="MCP Manifest")
async def mcp_endpoint():
    return get_mcp_manifest()

@app.post("/analyze/", summary="Run GenoAI Analysis")
async def analyze_variants_endpoint(variants: List[dict] = Body(...)):
    # The endpoint now simply calls your dedicated tool function
    return run_genoai_analysis(variants)