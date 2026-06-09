import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium", app_title="Thin Client CLI Examples")


@app.cell(hide_code=True)
def _():
    import os
    import shlex
    import subprocess
    import textwrap
    from pathlib import Path

    import marimo as mo
    from rich import print

    return Path, mo, os, print, shlex, subprocess, textwrap


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Thin Client CLI Examples

    **Install, configure, smoke-test, and run examples for the AGInt thin client from `AgintAI/agint-cli`.**

    Opening this notebook does **not** install anything or run live examples.
    Fill in the configuration below, then enable only the actions you want to run.
    """)
    return


@app.cell(hide_code=True)
def _(mo, os):
    api_base_url = mo.ui.text(
        label="API base URL",
        value=os.getenv("DOCKER_BUILDER_API_URL", ""),
        placeholder="https://your-private-api.example.com",
        full_width=True,
    )
    agint_api_key = mo.ui.text(
        label="AGInt API key",
        value=os.getenv("AGINT_APIKEY", ""),
        kind="password",
        full_width=True,
    )
    install_dir = mo.ui.text(
        label="Install directory",
        value=os.getenv("AGINT_INSTALL_DIR", ".agint-thin-client"),
        full_width=True,
    )
    install_client = mo.ui.checkbox(label="Install thin client")
    run_sanity_checks = mo.ui.checkbox(label="Run sanity checks")
    run_examples = mo.ui.checkbox(label="Run examples")

    mo.vstack(
        [
            mo.md("## Configuration"),
            api_base_url,
            agint_api_key,
            install_dir,
            mo.md("## Execution Guards"),
            install_client,
            run_sanity_checks,
            run_examples,
        ]
    )
    return (
        agint_api_key,
        api_base_url,
        install_client,
        install_dir,
        run_examples,
        run_sanity_checks,
    )


@app.cell(hide_code=True)
def _(
    Path,
    agint_api_key,
    api_base_url,
    install_client,
    install_dir,
    run_examples,
    run_sanity_checks,
):
    API_BASE_URL = api_base_url.value.strip()
    AGINT_API_KEY = agint_api_key.value.strip()
    INSTALL_DIR = Path(install_dir.value.strip() or ".agint-thin-client")
    INSTALL_CLIENT = install_client.value
    RUN_SANITY_CHECKS = run_sanity_checks.value
    RUN_EXAMPLES = run_examples.value
    INSTALL_ENV_PATH = INSTALL_DIR / ".env"
    INSTALL_VENV_ACTIVATE = INSTALL_DIR / ".venv" / "bin" / "activate"
    return (
        AGINT_API_KEY,
        API_BASE_URL,
        INSTALL_CLIENT,
        INSTALL_DIR,
        INSTALL_ENV_PATH,
        INSTALL_VENV_ACTIVATE,
        RUN_EXAMPLES,
        RUN_SANITY_CHECKS,
    )


@app.cell(hide_code=True)
def _(
    AGINT_API_KEY,
    API_BASE_URL,
    INSTALL_ENV_PATH,
    INSTALL_VENV_ACTIVATE,
    RUN_EXAMPLES,
    os,
    print,
    shlex,
    subprocess,
    textwrap,
):
    def shell(command: str, *, execute: bool | None = None):
        """Run a thin-client command, or silently no-op when guarded off.

        TODO: replace this wrapper with a first-party thin-client environment
        command if the CLI grows one.
        """
        should_execute = RUN_EXAMPLES if execute is None else execute
        if not should_execute:
            return None
        if not API_BASE_URL or not AGINT_API_KEY:
            print(
                "Set both API base URL and AGInt API key before running live "
                "thin-client commands."
            )
            return None

        normalized = textwrap.dedent(command).strip()
        activate = shlex.quote(str(INSTALL_VENV_ACTIVATE))
        env_file = shlex.quote(str(INSTALL_ENV_PATH))
        api_url = shlex.quote(API_BASE_URL)
        api_key = shlex.quote(AGINT_API_KEY)
        wrapped = f"""
        if [ -f {activate} ]; then
          . {activate}
        fi
        if [ -f {env_file} ]; then
          set -a
          . {env_file}
          set +a
        fi
        export DOCKER_BUILDER_API_URL={api_url}
        export AGINT_APIKEY={api_key}
        {normalized}
        """
        env = os.environ.copy()
        env["PYTHON_FORCE_COLOR"] = "1"
        completed = subprocess.run(
            textwrap.dedent(wrapped).strip(),
            shell=True,
            check=False,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if completed.stdout:
            print(completed.stdout)
        if completed.stderr:
            print(completed.stderr)
        if completed.returncode:
            print(f"exit status: {completed.returncode}")
        return completed.stdout, completed.stderr, completed.returncode

    return (shell,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Setup

    The thin-client README documents the interactive curl installer:

    ```bash
    curl -sSL https://raw.githubusercontent.com/AgintAI/agint-cli/main/install.sh | bash
    ```

    Inside marimo, use the hidden non-interactive install cell below. It creates
    the notebook-local virtual environment, installs from GitHub, writes the
    `.env` file from the configuration above, and smoke-tests the command entry
    points. Enable **Install thin client** only when you want that to run.
    """)
    return


@app.cell(hide_code=True)
def _(
    AGINT_API_KEY,
    API_BASE_URL,
    INSTALL_CLIENT,
    INSTALL_DIR,
    shell,
    shlex,
):
    install_thin_client = f"""
    python3 -m venv {shlex.quote(str(INSTALL_DIR / ".venv"))}
    . {shlex.quote(str(INSTALL_DIR / ".venv" / "bin" / "activate"))}
    python -m pip install --upgrade pip
    python -m pip install --upgrade "git+https://github.com/AgintAI/agint-cli.git"

    mkdir -p {shlex.quote(str(INSTALL_DIR))}
    umask 077
    printf '%s\\n' \\
      {shlex.quote(f"DOCKER_BUILDER_API_URL={API_BASE_URL}")} \\
      {shlex.quote(f"AGINT_APIKEY={AGINT_API_KEY}")} \\
      > {shlex.quote(str(INSTALL_DIR / ".env"))}

    dagify --help >/dev/null
    schemagin --help >/dev/null
    datagin --help >/dev/null
    dagent --help >/dev/null
    echo "thin client installed"
    """
    shell(install_thin_client, execute=INSTALL_CLIENT)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Sanity Checks

    Enable **Run sanity checks** to verify the configured environment and the
    installed CLI entry points before running examples.
    """)
    return


@app.cell(hide_code=True)
def _(RUN_SANITY_CHECKS, shell):
    sanity_check_commands = """
    python - <<'PY'
    import os

    print("DOCKER_BUILDER_API_URL=", os.environ.get("DOCKER_BUILDER_API_URL", "<unset>"))
    print("AGINT_APIKEY set=", bool(os.environ.get("AGINT_APIKEY")))
    PY
    command -v dagify
    command -v dagent
    command -v schemagin
    command -v datagin
    command -v agitransfer || true
    dagify --help >/dev/null
    schemagin --help >/dev/null
    datagin --help >/dev/null
    dagent --help >/dev/null
    """
    shell(sanity_check_commands, execute=RUN_SANITY_CHECKS)
    return


@app.cell(hide_code=True)
def _(RUN_SANITY_CHECKS, shell):
    sanity_check_openapi = """
    python - <<'PY'
    import json
    import os
    import urllib.request

    base_url = os.environ["DOCKER_BUILDER_API_URL"].rstrip("/")
    routes = [
        "/schemagin/compose",
        "/schemagin/refine",
        "/schemagin/visualize",
        "/datagin/ingest",
        "/datagin/synthesize",
        "/datagin/transform",
        "/dagify/compose",
        "/dagify/refine",
        "/dagify/resolve",
        "/dagify/compile",
        "/dagent/execute",
    ]
    with urllib.request.urlopen(f"{base_url}/openapi.json", timeout=30) as response:
        spec = json.load(response)

    schemas = spec.get("components", {}).get("schemas", {})
    for route in routes:
        operation = spec["paths"].get(route, {}).get("post")
        if not operation:
            print(f"missing route: {route}")
            continue
        ref = operation["requestBody"]["content"]["application/json"]["schema"]["$ref"]
        schema_name = ref.rsplit("/", 1)[-1]
        schema = schemas[schema_name]
        required = set(schema.get("required", []))
        print(f"\\n{route} -> {schema_name}")
        for name, detail in schema.get("properties", {}).items():
            metadata = {**detail.get("openapi_extra", {})}
            metadata.update({k: v for k, v in detail.items() if k.startswith("x-")})
            marker = "required" if name in required else "optional"
            cli_name = metadata.get("x-cli-name")
            argument = metadata.get("x-is-argument")
            print(f"  - {name}: {marker}; cli={cli_name}; argument={argument}")
    PY
    """
    shell(sanity_check_openapi, execute=RUN_SANITY_CHECKS)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # schemagin

    **Compose, refine, and visualize database schemas using intuitive natural-language prompts.**

    ---

    ## Sub-Commands

    | Command | Description |
    |:--|:--|
    | **`compose`** | Create a new database schema from a natural-language prompt. |
    | **`refine`** | Improve an existing schema using a required context file, stdin, or URI. |
    | **`visualize`** | Render schema diagrams and optionally export the schema in another format. |

    ---

    ## Usage Examples

    ### Compose a schema from a prompt

    ```bash
    schemagin compose "A schema representing a hedge fund" --ascii --intelligence 0 > schema.yaml
    ```
    """)
    return


@app.cell
def _(shell):
    shell(
        schema_compose
        := """schemagin compose "A schema representing a hedge fund" --ascii --intelligence 0 > schema.yaml"""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Generate schema diagram source artifacts

    ```bash
    schemagin compose "A schema representing a hedge fund" --visual dot --visual dbml --visual d2 --output-dir ./outputs/schemagin
    ```
    """)
    return


@app.cell
def _(shell):
    shell(
        schema_artifacts
        := """schemagin compose "A schema representing a hedge fund" --visual dot --visual dbml --visual d2 --output-dir ./outputs/schemagin"""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Refine an existing schema with context

    ```bash
    schemagin refine "Add soft-delete flags to all tables" --context schema.yaml --format=json > schema2.json
    ```
    """)
    return


@app.cell
def _(shell):
    shell(
        schema_refine
        := """schemagin refine "Add soft-delete flags to all tables" --context schema.yaml --format=json > schema2.json"""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Visualize a schema

    ```bash
    schemagin visualize schema.yaml --ascii
    ```
    """)
    return


@app.cell
def _(shell):
    shell(schema_visualize := """schemagin visualize schema.yaml --ascii""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Export visualizations from an existing schema

    ```bash
    schemagin visualize schema.yaml --visual dot --visual dbml --visual d2 --output-dir ./outputs/schema_docs
    ```
    """)
    return


@app.cell
def _(shell):
    shell(
        schema_visualize_artifacts
        := """schemagin visualize schema.yaml --visual dot --visual dbml --visual d2 --output-dir ./outputs/schema_docs"""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # datagin

    **Convert, transform, and synthesize structured data from unstructured inputs.**

    ---

    ## Sub-Commands

    | Command | Description |
    |:--|:--|
    | **`ingest`** | Extract structured data from text, files, or stdin. |
    | **`synthesize`** | Generate synthetic rows from a schema and prompt. |
    | **`transform`** | Transform structured data into a target output. |

    ---

    ## Usage Examples

    ### Generate synthetic data from a schema

    ```bash
    datagin synthesize "Financial data for these tables" schema.yaml --output-agilink syntheticFinancials.duckdb --rows 5
    ```
    """)
    return


@app.cell
def _(shell):
    shell(
        datagin_synthesize
        := """datagin synthesize "Financial data for these tables" schema.yaml --output-agilink syntheticFinancials.duckdb --rows 5"""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Ingest structured data from a file

    ```bash
    datagin ingest "Extract names and emails" messy_input_data.txt --output-agilink ./local.duckdb
    ```
    """)
    return


@app.cell
def _(shell):
    shell(
        datagin_ingest := """
        printf '%s\\n' "name,email\\nAda Lovelace,ada@example.com" > messy_input_data.txt
        datagin ingest "Extract names and emails" messy_input_data.txt --output-agilink ./local.duckdb
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Structure text from stdin

    ```bash
    echo "Eleanor Patel increased investment to $10,000." > fund-note.txt
    cat fund-note.txt | datagin ingest "Extract financial data" - --output-agilink ingestedFinancials.duckdb
    ```
    """)
    return


@app.cell
def _(shell):
    shell(
        datagin_stdin := """
        printf '%s\\n' "Eleanor Patel increased investment to $10,000." > fund-note.txt
        cat fund-note.txt | datagin ingest "Extract financial data" - --output-agilink ingestedFinancials.duckdb
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # agilink

    **Move schemas and table data between local files, DuckDB files, and Agilink-style workspaces.**

    The thin client exposes these commands as `agicat` and `agiwrite` when the
    server advertises those OpenAPI groups. Older installs can use the parent
    command form, such as `agi-tools agicat ...` or `agi-tools agiwrite ...`.

    ---

    ## Sub-Commands

    | Command | Description |
    |:--|:--|
    | **`agiwrite schema`** | Materialize a schema into a target database or workspace. |
    | **`agiwrite data`** | Write CSV directory data into a target database or workspace. |
    | **`agicat schema`** | Read a schema back out as YAML or JSON. |
    | **`agicat data`** | Export table data as CSV or a directory of CSV files. |

    ---

    ## Usage Examples

    ### Materialize a generated schema into DuckDB

    ```bash
    agiwrite schema schema.yaml --target-db ingestedFinancials.duckdb
    ```
    """)
    return


@app.cell
def _(shell):
    shell(
        agiwrite_schema
        := """agiwrite schema schema.yaml --target-db ingestedFinancials.duckdb"""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Read a schema back from DuckDB

    ```bash
    agicat schema ingestedFinancials.duckdb --output-format yaml > exported_schema.yaml
    ```
    """)
    return


@app.cell
def _(shell):
    shell(
        agicat_schema
        := """agicat schema ingestedFinancials.duckdb --output-format yaml > exported_schema.yaml"""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Export table data as CSV files

    ```bash
    agicat data ingestedFinancials.duckdb --output-format directory --output-dir ./exports/financials
    ```
    """)
    return


@app.cell
def _(shell):
    shell(
        agicat_data
        := """agicat data ingestedFinancials.duckdb --output-format directory --output-dir ./exports/financials"""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # dagify

    **Compose, refine, resolve, and compile workflow DAGs from natural-language instructions.**

    ---

    ## Sub-Commands

    | Command | Description |
    |:--|:--|
    | **`compose`** | Create a workflow DAG from a natural-language description. |
    | **`refine`** | Improve an existing workflow DAG using a prompt, optional context, and optional tool catalog. |
    | **`resolve`** | Upgrade a DAG to a more concrete type in the DAG hierarchy. Use `--tools` when the workflow already contains `selected_tools` so resolve can look up their signatures. |
    | **`compile`** | Compile a DAG into an executable target such as CrewAI. |

    ---

    ## Usage Examples

    ### Compose a workflow

    ```bash
    dagify compose "A workflow representing hedge fund due diligence" --ascii --intelligence 5 > hedgefund.flow
    ```
    """)
    return


@app.cell
def _(shell):
    shell(
        dagify_compose
        := """dagify compose "A workflow representing hedge fund due diligence" --ascii --intelligence 5 > hedgefund.flow"""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Refine a workflow

    ```bash
    dagify refine "Improve all nodes in this workflow" hedgefund.flow --ascii --intelligence 5 > improved.flow
    ```
    """)
    return


@app.cell
def _(shell):
    shell(
        dagify_refine
        := """dagify refine "Improve all nodes in this workflow" hedgefund.flow --ascii --intelligence 5 > improved.flow"""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Resolve a workflow

    ```bash
    dagify resolve improved.flow --ascii --intelligence 5
    ```

    For tool-aware workflows, pass the same tool catalog or allowlist used when the tools were selected:

    ```bash
    dagify resolve improved.flow context.md --tools tools.yaml --guidance "preserve existing tool choices" --ascii --intelligence 5
    ```
    """)
    return


@app.cell
def _(shell):
    shell(
        dagify_resolve := """dagify resolve improved.flow --ascii --intelligence 5"""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Compile a workflow

    ```bash
    dagify compile improved.flow --type-floor pure --build-target crewai --tools tools.yaml --intelligence 5
    ```
    """)
    return


@app.cell
def _(shell):
    shell(
        dagify_compile
        := """dagify compile improved.flow --type-floor pure --build-target crewai --tools tools.yaml --intelligence 5"""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # dagent

    **Validate, optimize, execute, interpret, and synthesize workflow DAGs.**

    ---

    ## Sub-Commands

    | Command | Description |
    |:--|:--|
    | **`validate`** | Check DAG structure, dependencies, and execution feasibility. |
    | **`optimize`** | Tune AI-driven DAG nodes against test data. |
    | **`execute`** | Execute a DAG plan with optional context, structured input args, and a tool allowlist/catalog. |
    | **`interpret`** | Generate and execute a DAG plan dynamically. |
    | **`synthesize`** | Generate, compile, and execute a DAG plan in one flow. |

    ---

    ## Usage Examples

    ### Execute from stdin

    ```bash
    cat hedgefund.flow | dagent execute - "Large cap stocks only" --intelligence 5
    ```

    Tool-aware workflows require the runtime tool allowlist/catalog:

    ```bash
    dagent execute hedgefund.flow context.md --input input_args.yaml --tools tools.yaml --intelligence 5
    ```
    """)
    return


@app.cell
def _(shell):
    shell(
        dagent_execute
        := """cat hedgefund.flow | dagent execute - "Large cap stocks only" --intelligence 5"""
    )
    return


if __name__ == "__main__":
    app.run()
