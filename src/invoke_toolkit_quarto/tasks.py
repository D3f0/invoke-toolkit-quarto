"""A set of invoke-toolkit tasks
It has support for direnv if available which can be used for uv python
environment activation with:

```python
source_env_if_exists ../.envrc
dotenv_if_exists .env

if [ -d .venv ]; then
    export VIRTUAL_ENV=$PWD/.venv
    export PATH=$PWD/.venv/bin:$PATH
fi
```

"""

from pathlib import Path

from invoke_toolkit import Context, task


def get_git_root(ctx: Context) -> Path:
    """Git repo path"""
    try:
        return Path(
            ctx.run(
                "git rev-parse --show-toplevel", hide=not ctx.config.run.echo
            ).stdout
        )
    except Exception as err:
        return Path(".")


def get_command_prefix(ctx: Context) -> str:
    root = get_git_root(ctx)
    envrc = root / ".envrc"
    if envrc.exists():
        return f"direnv exec {root}"
    else:
        return ""


@task(
    help={
        "file": "Path to the document or project to preview (default: current project)",
        "port": "Port to listen on (default: random value between 3000 and 8000)",
        "host": "Hostname to bind to (default: 127.0.0.1)",
        "render": "Render to the specified format(s) before previewing (e.g. 'all', 'html')",
        "no_serve": "Don't run a local preview web server (just monitor and re-render)",
        "no_navigate": "Don't navigate the browser automatically when outputs are updated",
        "no_browser": "Don't open a browser to preview the site",
        "no_watch_inputs": "Do not re-render input files when they change",
        "timeout": "Seconds after which to exit if there are no active clients",
        "log": "Path to log file",
        "log_level": "Log level (debug, info, warning, error, critical)",
        "log_format": "Log format (plain, json-stream)",
        "quiet": "Suppress console output",
        "profile": "Active project profile(s)",
    }
)
def preview(
    ctx: Context,
    file: str = "",
    port: int = 0,
    host: str = "",
    render: str = "revealjs",
    no_serve: bool = False,
    no_navigate: bool = False,
    no_browser: bool = False,
    no_watch_inputs: bool = False,
    timeout: int = 0,
    log: str = "",
    log_level: str = "",
    log_format: str = "",
    quiet: bool = False,
    profile: str = "",
):
    """Preview a Quarto document (renders as revealjs on $PORT by default)"""
    cmd = f"{get_command_prefix(ctx)} quarto preview"

    if file:
        cmd += f" {file}"

    if render:
        cmd += f" --render {render}"

    if port:
        cmd += f" --port {port}"
    else:
        cmd += " --port $PORT"

    if host:
        cmd += f" --host {host}"

    if no_serve:
        cmd += " --no-serve"

    if no_navigate:
        cmd += " --no-navigate"

    if no_browser:
        cmd += " --no-browser"

    if no_watch_inputs:
        cmd += " --no-watch-inputs"

    if timeout:
        cmd += f" --timeout {timeout}"

    if log:
        cmd += f" --log {log}"

    if log_level:
        cmd += f" --log-level {log_level}"

    if log_format:
        cmd += f" --log-format {log_format}"

    if quiet:
        cmd += " --quiet"

    if profile:
        cmd += f" --profile {profile}"

    ctx.run(cmd, pty=True)


@task(
    help={
        "provider": "Publishing provider: quarto-pub, gh-pages, connect, netlify, confluence, huggingface",
        "path": "Path to the document or project to publish",
        "id": "Identifier of content to publish",
        "server": "Server to publish to (for Posit Connect)",
        "token": "Access token for publishing provider",
        "no_render": "Do not render before publishing",
        "no_prompt": "Do not prompt to confirm publishing destination",
        "no_browser": "Do not open a browser to the site after publishing",
        "log": "Path to log file",
        "log_level": "Log level (debug, info, warning, error, critical)",
        "log_format": "Log format (plain, json-stream)",
        "quiet": "Suppress console output",
        "profile": "Active project profile(s)",
    }
)
def publish(
    ctx: Context,
    provider: str = "gh-pages",
    path: str = "",
    id: str = "",
    server: str = "",
    token: str = "",
    no_render: bool = False,
    no_prompt: bool = True,
    no_browser: bool = False,
    log: str = "",
    log_level: str = "",
    log_format: str = "",
    quiet: bool = False,
    profile: str = "",
):
    """Publish a Quarto document to a provider (default: GitHub Pages)"""
    cmd = f"{get_command_prefix(ctx)} quarto publish"

    if provider:
        cmd += f" {provider}"

    if path:
        cmd += f" {path}"

    if id:
        cmd += f" --id {id}"

    if server:
        cmd += f" --server {server}"

    if token:
        cmd += f" --token {token}"

    if no_render:
        cmd += " --no-render"

    if no_prompt:
        cmd += " --no-prompt"

    if no_browser:
        cmd += " --no-browser"

    if log:
        cmd += f" --log {log}"

    if log_level:
        cmd += f" --log-level {log_level}"

    if log_format:
        cmd += f" --log-format {log_format}"

    if quiet:
        cmd += " --quiet"

    if profile:
        cmd += f" --profile {profile}"

    ctx.run(cmd, pty=True)
