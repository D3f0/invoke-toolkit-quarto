"""A set of invoke-toolkit tasks"""

from invoke_toolkit import Context, task


@task
def preview(ctx: Context):
    """Preview a Quarto document (renders as revealjs on $PORT)"""
    ctx.run("quarto preview --render revealjs --port $PORT")


@task
def publish(ctx: Context):
    """Publish a Quarto document to GitHub Pages"""
    ctx.run("quarto publish gh-pages --no-prompt")
