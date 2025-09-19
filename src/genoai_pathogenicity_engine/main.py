import click
import logging

@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
def cli():
    """A command-line interface for the GenoAI Pathogenicity Engine."""
    pass

@cli.command("run", help="Run the GenoAI server.")
@click.option("-t", "--transport", type=click.Choice(["http", "stdio"]), default="http", help="Server transport protocol.")
@click.option("-p", "--port", type=int, default=8001, help="Port for HTTP transport.")
@click.option("-h", "--host", type=str, default="127.0.0.1", help="Hostname for HTTP transport.")
def run_command(transport: str, port: int, host: str):
    """Handles running the server in different modes."""
    logger = logging.getLogger(__name__)

    if transport == "http":
        import uvicorn
        from .app import app
        logger.info(f"Starting FastAPI server on http://{host}:{port}")
        uvicorn.run(app, host=host, port=port)
    elif transport == "stdio":
        logger.info("Starting MCP server in stdio mode.")
        from .mcp import mcp
        mcp.run(transport="stdio")
    else:
        logger.error(f"Transport '{transport}' is not supported.")

if __name__ == "__main__":
    cli()