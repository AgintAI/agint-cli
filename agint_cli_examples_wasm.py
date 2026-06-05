import marimo

__generated_with = "0.23.9"
app = marimo.App(width="full", app_title="Thin Client CLI Examples - WASM")


@app.cell(hide_code=True)
def _():
    import base64
    import html
    import json
    import re
    import sys
    import urllib.error
    import urllib.request

    import marimo as mo

    IS_WASM = "pyodide" in sys.modules
    return IS_WASM, base64, html, json, mo, re, urllib


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Thin Client CLI Examples

    This browser notebook shows the same commands you can copy into a terminal,
    then runs their AGInt API equivalents directly from WebAssembly.

    No shell commands or local installs run in this browser version.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    api_base_url = mo.ui.text(
        label="API base URL",
        value="https://api.agintai.com",
        placeholder="https://your-agint-api.example.com",
        full_width=True,
    )
    agint_api_key = mo.ui.text(
        label="AGInt API key",
        kind="password",
        full_width=True,
    )
    check_api_connection = mo.ui.run_button(label="Check API connection")
    run_schema_compose = mo.ui.run_button(label="Run")
    run_schema_refine = mo.ui.run_button(label="Run")
    run_schema_visualize = mo.ui.run_button(label="Run")
    run_datagin_synthesize = mo.ui.run_button(label="Run")
    run_datagin_ingest = mo.ui.run_button(label="Run")
    run_datagin_stdin = mo.ui.run_button(label="Run")
    run_dagify_compose = mo.ui.run_button(label="Run")
    run_dagify_refine = mo.ui.run_button(label="Run")
    run_dagify_resolve = mo.ui.run_button(label="Run")
    run_dagify_compile = mo.ui.run_button(label="Run")
    run_dagent_execute = mo.ui.run_button(label="Run")

    mo.vstack(
        [
            mo.md("## Configuration"),
            api_base_url,
            agint_api_key,
            mo.md("## Examples"),
        ]
    )
    return (
        agint_api_key,
        api_base_url,
        check_api_connection,
        run_dagent_execute,
        run_dagify_compile,
        run_dagify_compose,
        run_dagify_refine,
        run_dagify_resolve,
        run_datagin_ingest,
        run_datagin_stdin,
        run_datagin_synthesize,
        run_schema_compose,
        run_schema_refine,
        run_schema_visualize,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Local install

    Copy this command when you want the real terminal CLI on your machine:

    ```bash
    curl -sSL https://raw.githubusercontent.com/AgintAI/agint-cli/main/install.sh | bash
    ```

    This WebAssembly notebook does not install the CLI. It keeps the command
    examples copyable while making equivalent browser API calls under the hood.
    """)
    return


@app.cell(hide_code=True)
def _(IS_WASM, agint_api_key, api_base_url, base64, html, json, mo, re, urllib):
    FILES = {}

    def command_block(command: str):
        return mo.md(f"""```bash
{command}
```""")

    def decode_stderr(value):
        if not value:
            return ""
        if not isinstance(value, str):
            return str(value)
        try:
            return base64.b64decode(value, validate=True).decode("utf-8")
        except Exception:
            return value

    def clean_terminal_output(text: str):
        if not text:
            return ""

        # Strip ANSI/VT100 terminal controls while preserving plain ASCII art.
        cleaned = text.replace("\r\n", "\n").replace("\r", "\n")
        cleaned = (
            cleaned.replace("\\x1b", "\x1b")
            .replace("\\u001b", "\x1b")
            .replace("\\033", "\x1b")
            .replace("\\e", "\x1b")
        )
        cleaned = re.sub(r"\x1b\][^\x07]*(?:\x07|\x1b\\)", "", cleaned)
        cleaned = re.sub(r"\x1b\[[0-?]*[ -/]*[@-~]", "", cleaned)
        cleaned = re.sub(r"\x9b[0-?]*[ -/]*[@-~]", "", cleaned)
        cleaned = re.sub(r"\x1b[@-Z\\-_]", "", cleaned)

        # Some browser rendering drops ESC but leaves fragments like [34m.
        cleaned = re.sub(r"\[\??[0-9;:]+[ -/]*[@-~]", "", cleaned)
        cleaned = re.sub(r"\[[0-9;:? ]{1,30}[A-Za-z]", "", cleaned)

        lines = []
        seen_progress = {}
        for line in cleaned.split("\n"):
            stripped = line.rstrip()
            progress_key = stripped.strip()
            if progress_key.endswith("..."):
                seen_progress[progress_key] = seen_progress.get(progress_key, 0) + 1
                if seen_progress[progress_key] > 2:
                    continue
            if lines and lines[-1] == stripped and progress_key.endswith("..."):
                continue
            lines.append(stripped)

        return "\n".join(lines).strip("\n")

    def example_panel(run_button, command: str, response, *, output_name=None):
        return mo.vstack(
            [
                run_button,
                render_response(command, response, output_name=output_name),
            ]
        )

    def preformatted(title: str, text: str, *, tone: str = "plain"):
        if not text:
            return None
        border = {
            "plain": "#d8dee9",
            "error": "#d73a49",
            "warning": "#b08800",
            "success": "#22863a",
        }.get(tone, "#d8dee9")
        return mo.Html(
            f"""
            <section style="margin: 0.75rem 0;">
              <div style="font-weight: 600; margin-bottom: 0.25rem;">{html.escape(title)}</div>
              <pre style="
                overflow-x: auto;
                white-space: pre;
                width: 100%;
                max-width: calc(100vw - 3rem);
                box-sizing: border-box;
                border: 1px solid {border};
                border-radius: 6px;
                padding: 0.75rem;
                background: #f6f8fa;
                color: #24292f;
                font-size: 0.875rem;
                line-height: 1.3;
              ">{html.escape(text)}</pre>
            </section>
            """
        )

    def render_response(command: str, response, *, output_name=None):
        pieces = [command_block(command)]
        if response is None:
            pieces.append(mo.md("_Click **Run** to execute this example._"))
            return mo.vstack(pieces)

        if response.get("http_error"):
            pieces.append(preformatted("HTTP error", response["http_error"], tone="error"))
            return mo.vstack([piece for piece in pieces if piece is not None])

        stdout = clean_terminal_output(response.get("stdout") or "")
        stderr = clean_terminal_output(decode_stderr(response.get("stderr")))
        exit_code = response.get("exit_code")

        if output_name and stdout:
            FILES[output_name] = stdout

        if exit_code not in (None, 0):
            pieces.append(mo.md(f"**Exit status:** `{exit_code}`"))
        elif response:
            pieces.append(mo.md("**Status:** success"))

        pieces.append(preformatted("stdout", stdout))
        stderr_tone = "error" if exit_code not in (None, 0) else "plain"
        pieces.append(preformatted("stderr / terminal output", stderr, tone=stderr_tone))

        if output_name and stdout:
            pieces.append(
                mo.download(
                    data=stdout.encode("utf-8"),
                    filename=output_name,
                    mimetype="text/plain",
                    label=f"Download {output_name}",
                )
            )

        if not stdout and not stderr:
            pieces.append(preformatted("response", json.dumps(response, indent=2)))

        return mo.vstack([piece for piece in pieces if piece is not None])

    async def agint_post(path: str, payload: dict):
        if not api_base_url.value.strip() or not agint_api_key.value.strip():
            return {
                "http_error": (
                    "Set both API base URL and AGInt API key before running "
                    "live examples."
                )
            }

        url = f"{api_base_url.value.rstrip('/')}{path}"
        body = {
            **payload,
            "agint_apikey": agint_api_key.value.strip(),
        }
        encoded = json.dumps(body)

        if IS_WASM:
            from pyodide.http import pyfetch

            try:
                response = await pyfetch(
                    url,
                    method="POST",
                    headers={"Content-Type": "application/json"},
                    body=encoded,
                )
                text = await response.string()
                if response.status >= 400:
                    return {"http_error": f"{response.status} {response.status_text}\n{text}"}
                return json.loads(text)
            except Exception as error:
                return {"http_error": str(error)}

        request = urllib.request.Request(
            url,
            data=encoded.encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as error:
            body_text = error.read().decode("utf-8", errors="replace")
            return {"http_error": f"{error.code} {error.reason}\n{body_text}"}
        except Exception as error:
            return {"http_error": str(error)}

    async def agint_get(path: str):
        if not api_base_url.value.strip():
            return {"http_error": "Set the API base URL before checking the API."}

        url = f"{api_base_url.value.rstrip('/')}{path}"

        if IS_WASM:
            from pyodide.http import pyfetch

            try:
                response = await pyfetch(url, method="GET")
                text = await response.string()
                if response.status >= 400:
                    return {"http_error": f"{response.status} {response.status_text}\n{text}"}
                try:
                    return json.loads(text)
                except json.JSONDecodeError:
                    return {"stdout": text}
            except Exception as error:
                return {
                    "http_error": (
                        f"{error}\n\n"
                        "If this works inside the VPN in a normal browser tab but "
                        "fails here, check that the API allows CORS requests from "
                        "https://molab.marimo.io and https://agintai.github.io."
                    )
                }

        request = urllib.request.Request(url, method="GET")
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                text = response.read().decode("utf-8")
                try:
                    return json.loads(text)
                except json.JSONDecodeError:
                    return {"stdout": text}
        except urllib.error.HTTPError as error:
            body_text = error.read().decode("utf-8", errors="replace")
            return {"http_error": f"{error.code} {error.reason}\n{body_text}"}
        except Exception as error:
            return {"http_error": str(error)}

    return FILES, agint_get, agint_post, example_panel, render_response


@app.cell(hide_code=True)
async def _(agint_get, api_base_url, check_api_connection, example_panel):
    connection_response = None
    if check_api_connection.value:
        connection_response = await agint_get("/openapi.json")
        if "paths" in connection_response:
            path_count = len(connection_response.get("paths", {}))
            connection_response = {
                "stdout": f"Connected. OpenAPI schema loaded with {path_count} paths."
            }
    example_panel(
        check_api_connection,
        f"curl {api_base_url.value.rstrip('/')}/openapi.json",
        connection_response,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # schemagin

    Compose, refine, and visualize database schemas using intuitive
    natural-language prompts.
    """)
    return


@app.cell(hide_code=True)
async def _(agint_post, example_panel, run_schema_compose):
    schema_compose_command = (
        'schemagin compose "A schema representing a hedge fund" '
        "--ascii --intelligence 5 > schema.yaml"
    )
    schema_compose_response = None
    if run_schema_compose.value:
        schema_compose_response = await agint_post(
            "/schemagin/compose",
            {
                "prompt": "A schema representing a hedge fund",
                "ascii": True,
                "intelligence": 5,
            },
        )
    example_panel(
        run_schema_compose,
        schema_compose_command,
        schema_compose_response,
        output_name="schema.yaml",
    )
    return (schema_compose_response,)


@app.cell(hide_code=True)
async def _(FILES, agint_post, example_panel, run_schema_refine):
    schema_refine_command = (
        'schemagin refine "Add soft-delete flags to all tables" '
        "--context schema.yaml --format=json > schema2.json"
    )
    schema_refine_response = None
    if run_schema_refine.value:
        schema_refine_response = await agint_post(
            "/schemagin/refine",
            {
                "prompt": "Add soft-delete flags to all tables",
                "context": FILES.get("schema.yaml", ""),
                "format": "json",
            },
        )
    example_panel(
        run_schema_refine,
        schema_refine_command,
        schema_refine_response,
        output_name="schema2.json",
    )
    return (schema_refine_response,)


@app.cell(hide_code=True)
async def _(FILES, agint_post, example_panel, run_schema_visualize):
    schema_visualize_command = "schemagin visualize schema.yaml --ascii"
    schema_visualize_response = None
    if run_schema_visualize.value:
        schema_visualize_response = await agint_post(
            "/schemagin/visualize",
            {
                "schema": FILES.get("schema.yaml", ""),
                "ascii": True,
            },
        )
    example_panel(run_schema_visualize, schema_visualize_command, schema_visualize_response)
    return (schema_visualize_response,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # datagin

    Convert, transform, and synthesize structured data from unstructured inputs.
    """)
    return


@app.cell(hide_code=True)
async def _(FILES, agint_post, example_panel, run_datagin_synthesize):
    datagin_synthesize_command = (
        'datagin synthesize "Financial data for these tables" schema.yaml '
        "--output-agilink syntheticFinancials.duckdb --rows 5"
    )
    datagin_synthesize_response = None
    if run_datagin_synthesize.value:
        datagin_synthesize_response = await agint_post(
            "/datagin/synthesize",
            {
                "prompt": "Financial data for these tables",
                "schema": FILES.get("schema.yaml", ""),
                "output_agilink": "syntheticFinancials.duckdb",
                "rows": 5,
            },
        )
    example_panel(
        run_datagin_synthesize,
        datagin_synthesize_command,
        datagin_synthesize_response,
    )
    return (datagin_synthesize_response,)


@app.cell(hide_code=True)
async def _(agint_post, example_panel, run_datagin_ingest):
    datagin_ingest_command = (
        'printf \'%s\\n\' "name,email\\nAda Lovelace,ada@example.com" '
        "> messy_input_data.txt\n"
        'datagin ingest "Extract names and emails" messy_input_data.txt '
        "--output-agilink ./local.duckdb"
    )
    datagin_ingest_response = None
    if run_datagin_ingest.value:
        datagin_ingest_response = await agint_post(
            "/datagin/ingest",
            {
                "prompt": "Extract names and emails",
                "input": "name,email\nAda Lovelace,ada@example.com",
                "output_agilink": "./local.duckdb",
            },
        )
    example_panel(run_datagin_ingest, datagin_ingest_command, datagin_ingest_response)
    return (datagin_ingest_response,)


@app.cell(hide_code=True)
async def _(agint_post, example_panel, run_datagin_stdin):
    datagin_stdin_command = (
        'echo "Eleanor Patel increased investment to $10,000." > fund-note.txt\n'
        'cat fund-note.txt | datagin ingest "Extract financial data" - '
        "--output-agilink ingestedFinancials.duckdb"
    )
    datagin_stdin_response = None
    if run_datagin_stdin.value:
        datagin_stdin_response = await agint_post(
            "/datagin/ingest",
            {
                "prompt": "Extract financial data",
                "input": "-",
                "stdin": "Eleanor Patel increased investment to $10,000.",
                "output_agilink": "ingestedFinancials.duckdb",
            },
        )
    example_panel(run_datagin_stdin, datagin_stdin_command, datagin_stdin_response)
    return (datagin_stdin_response,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # dagify

    Compose, refine, resolve, and compile workflow DAGs from natural-language
    instructions.
    """)
    return


@app.cell(hide_code=True)
async def _(agint_post, example_panel, run_dagify_compose):
    dagify_compose_command = (
        'dagify compose "A workflow representing hedge fund due diligence" '
        "--ascii --intelligence 25 > hedgefund.flow"
    )
    dagify_compose_response = None
    if run_dagify_compose.value:
        dagify_compose_response = await agint_post(
            "/dagify/compose",
            {
                "prompt": "A workflow representing hedge fund due diligence",
                "ascii": True,
                "intelligence": 25,
            },
        )
    example_panel(
        run_dagify_compose,
        dagify_compose_command,
        dagify_compose_response,
        output_name="hedgefund.flow",
    )
    return (dagify_compose_response,)


@app.cell(hide_code=True)
async def _(FILES, agint_post, example_panel, run_dagify_refine):
    dagify_refine_command = (
        'dagify refine "Improve all nodes in this workflow" hedgefund.flow '
        "--ascii --intelligence 25 > improved.flow"
    )
    dagify_refine_response = None
    if run_dagify_refine.value:
        dagify_refine_response = await agint_post(
            "/dagify/refine",
            {
                "prompt": "Improve all nodes in this workflow",
                "data": FILES.get("hedgefund.flow", ""),
                "ascii": True,
                "intelligence": 25,
            },
        )
    example_panel(
        run_dagify_refine,
        dagify_refine_command,
        dagify_refine_response,
        output_name="improved.flow",
    )
    return (dagify_refine_response,)


@app.cell(hide_code=True)
async def _(FILES, agint_post, example_panel, run_dagify_resolve):
    dagify_resolve_command = "dagify resolve improved.flow --ascii --intelligence 25"
    dagify_resolve_response = None
    if run_dagify_resolve.value:
        dagify_resolve_response = await agint_post(
            "/dagify/resolve",
            {
                "data": FILES.get("improved.flow", ""),
                "ascii": True,
                "intelligence": 25,
            },
        )
    example_panel(run_dagify_resolve, dagify_resolve_command, dagify_resolve_response)
    return (dagify_resolve_response,)


@app.cell(hide_code=True)
async def _(FILES, agint_post, example_panel, run_dagify_compile):
    dagify_compile_command = (
        "dagify compile improved.flow --type-floor pure "
        "--build-target crewai --intelligence 25"
    )
    dagify_compile_response = None
    if run_dagify_compile.value:
        dagify_compile_response = await agint_post(
            "/dagify/compile",
            {
                "data": FILES.get("improved.flow", ""),
                "type_floor": "pure",
                "build_target": "crewai",
                "intelligence": 25,
            },
        )
    example_panel(run_dagify_compile, dagify_compile_command, dagify_compile_response)
    return (dagify_compile_response,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # dagent

    Validate, optimize, execute, interpret, and synthesize workflow DAGs.
    """)
    return


@app.cell(hide_code=True)
async def _(FILES, agint_post, example_panel, run_dagent_execute):
    dagent_execute_command = (
        'cat hedgefund.flow | dagent execute - "Large cap stocks only" '
        "--intelligence 25"
    )
    dagent_execute_response = None
    if run_dagent_execute.value:
        dagent_execute_response = await agint_post(
            "/dagent/execute",
            {
                "plan": "-",
                "data": "Large cap stocks only",
                "stdin": FILES.get("hedgefund.flow", ""),
                "intelligence": 25,
            },
        )
    example_panel(run_dagent_execute, dagent_execute_command, dagent_execute_response)
    return (dagent_execute_response,)


if __name__ == "__main__":
    app.run()
