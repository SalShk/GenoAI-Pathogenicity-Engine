# This file defines the manifest for the MCP server.

MANIFEST = {
    "mcp_version": "0.1.0",
    "title": "GenoAI Pathogenicity Engine",
    "description": "An advanced clinical reasoning engine designed to address the challenge of genomic variant interpretation.",
    "tools": [
        {
            "name": "run_genoai_analysis",
            "description": "Executes the GenoAI engine on a list of variants to generate a clinically relevant pathogenicity score and category.",
        }
    ]
}

def get_mcp_manifest():
    """Provides the manifest for the FastAPI web server endpoint."""
    return MANIFEST