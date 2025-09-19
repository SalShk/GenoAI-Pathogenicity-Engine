from fastmcp import Mcp

# Import your dedicated tool function
from .tools import run_genoai_analysis

# 1. Define a more detailed manifest
MANIFEST = {
    "mcp_version": "0.1.0",
    "title": "GenoAI Pathogenicity Engine",
    "description": "A clinical reasoning engine that produces a multi-dimensional evidence profile.",
    "tools": [
        {
            "name": "run_genoai_analysis",
            "description": "Executes the GenoAI engine on a list of variants to generate a clinically relevant pathogenicity score and category.",
            "inputs": {
                "type": "object",
                "properties": {
                    "variants": {
                        "type": "array",
                        "items": {"type": "object"},
                        "description": "A list of dictionaries, where each dictionary represents a pre-annotated variant."
                    }
                },
                "required": ["variants"]
            },
            "outputs": {
                "type": "array",
                "items": {"type": "object"},
                "description": "A list of the input variant dictionaries with added GenoAI scores and classifications."
            }
        }
    ]
}

# 2. Create the Mcp server instance using the manifest
mcp = Mcp(tools_manifest=MANIFEST)

# 3. Register your Python function as the tool named "run_genoai_analysis"
mcp.register_tool(run_genoai_analysis)

# 4. Create a helper function for the FastAPI app to get the manifest
def get_mcp_manifest():
    """Provides the manifest for the FastAPI web server endpoint."""
    return MANIFEST