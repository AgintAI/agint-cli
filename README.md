# Agint CLI

A command-line interface (CLI) client for interacting with Agint.

## Installation

Recommended:

```bash
curl -sSL https://raw.githubusercontent.com/AgintAI/agint-cli/main/install.sh | bash
```

Manual:

```bash
pip install git+https://github.com/AgintAI/agint-cli.git
```

See [Appendix](#appendix) for credentials, reinstall behavior, and artifact sync
details.

## Examples

```bash
# Analyze a stock
dagify compose "Analyze a stock using fundamental data" --ascii --intelligence 5

```

```bash
# Coordinate a complex series of events
dagify compose "3 events A B C happen concurrently with no dependencies on each other, \
but then AB happens after A and B, AC happens after A and C, BC happens after B and C, \
and lastly they all join at ABC concurrently" \
  --ascii \
  --intelligence 5
```

```bash
# Refine a workflow to add more detail to specific nodes
dagify refine "Add more detailed instructions to the data cleaning step" \
  workflow.yaml \
  --ascii \
  --intelligence 5
```

```bash
# Improve a machine learning workflow with hyperparameter tuning
cat ml_pipeline.yaml \
  | dagify refine "Turn the hyperparameters up to 11" - \
    --intelligence 5
```

```bash
# Resolve a workflow to the next concrete DAG type
dagify resolve workflow.yaml \
  --ascii \
  --intelligence 5
```

```bash
# Resolve a tool-aware workflow; --tools is used to look up already-selected tool signatures
dagify resolve workflow.yaml context.md \
  --tools tools.yaml \
  --guidance "preserve existing tool choices while improving typed contracts" \
  --ascii \
  --intelligence 5
```

```bash
# Execute a workflow with runtime context, structured input args, and selected-tool allowlist
dagent execute workflow.yaml context.md \
  --input input_args.yaml \
  --tools tools.yaml \
  --intelligence 5
```

```bash
# Compose a db schema for a blog, output it in json format
schemagin compose "Blog schema with tags" \
  --format=json \
  > schema.json
```

```bash
# Generate schema diagram source artifacts
schemagin compose "A schema representing a hedge fund" \
  --visual dot --visual dbml --visual d2 \
  --output-dir ./outputs/schemagin
```

```bash
# Export diagram source artifacts from an existing schema
schemagin visualize schema.yaml \
  --visual dot --visual dbml --visual d2 \
  --output-dir ./outputs/schema_docs
```

```bash
# Create a local database and from a dynamically generated schema
schemagin compose "a database schema for a relational file system backing the metadata and contents of every file on an operating system" \
  | agiwrite schema - \
    --target-db=instant.db
```

```bash
# Materialize a generated schema into DuckDB
agiwrite schema schema.yaml --target-db ingestedFinancials.duckdb
```

```bash
# Read a schema back from DuckDB
agicat schema ingestedFinancials.duckdb --output-format yaml > exported_schema.yaml
```

```bash
# Export table data as CSV files
agicat data ingestedFinancials.duckdb \
  --output-format directory \
  --output-dir ./exports/financials
```

```bash
# Extract structured names and emails from a CSV file into a local DuckDB database
datagin ingest "Extract names,emails" \
  messy_input_data.txt \
  --output-agilink ./local.duckdb
```

```bash
# Extract and structure the first 50 invoices from a PDF document
datagin ingest --rows=50 \
  "Parse invoices" \
  invoices.pdf \
  --output-agilink agilink://raw_invoices

# Structure skewed JSON data provided via stdin into agilink
cat data.json \
  | datagin ingest "Structure JSON" - \
    --output-agilink ./local.duckdb
```

## Marimo notebooks

Try the examples locally, in molab, or on GitHub Pages.

### Run locally

Run the local CLI notebook with marimo from a project virtual environment:

```bash
# Clone the repo if you do not already have it locally
git clone https://github.com/AgintAI/agint-cli.git
cd agint-cli

# Create and activate a local virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install marimo and the thin client package
python -m pip install --upgrade pip
python -m pip install marimo
python -m pip install -e .

# Provide API credentials for live examples
export DOCKER_BUILDER_API_URL=https://your-agint-api.example.com
export AGINT_APIKEY=your-api-key

# Open the local notebook
marimo edit agint_cli_examples.py
```

The local notebook has API URL/key fields and controls for setup, sanity checks,
and examples.

### Run WASM locally

To run the WebAssembly notebook locally with marimo instead of GitHub Pages:

```bash
source .venv/bin/activate
marimo edit agint_cli_examples_wasm.py
```

### Open in molab

Open the local/server notebook in molab:

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/AgintAI/agint-cli/blob/main/agint_cli_examples.py)

Open the WebAssembly notebook in molab:

[https://molab.marimo.io/github/AgintAI/agint-cli/blob/main/agint_cli_examples_wasm.py/wasm](https://molab.marimo.io/github/AgintAI/agint-cli/blob/main/agint_cli_examples_wasm.py/wasm)

### Try in browser

Try the WebAssembly browser notebook on GitHub Pages:

[https://agintai.github.io/agint-cli/](https://agintai.github.io/agint-cli/)

The local notebook runs real CLI commands. The WebAssembly notebook shows the
same commands and calls the AGInt API directly in the browser.

## Appendix

### Credentials

The client uses:

```bash
export DOCKER_BUILDER_API_URL=your-agint-instance
export AGINT_APIKEY=your-api-key
```

The curl installer stores these in `~/agint/.env`. For beta API access, contact
accounts@agintai.com.

### Curl Installer

The installer creates `~/agint/.venv` and `~/agint/work`. Run commands from a
workspace such as `~/agint/work`, not the install root.

After install, it can open an activated shell in the workspace. On Windows Git
Bash, the activation path is usually `~/agint/.venv/Scripts/activate`; the
installer prints the exact command.

Rerunning the installer backs up the old install, shows preserved credentials as
defaults, and lets Enter keep them or new input replace them.

### Artifact Sync

Generated-tool commands sync selected local artifacts with the remote
`agitransfer://` workspace before and after command execution.

Sync-enabled command groups:

```text
agicat
agiwrite
dagify
dagent
schemagin
datagin
```

Synced extensions:

```text
.csv .d2 .dbml .dot .duckdb .flow .html .json .md .pdf .png .py .sql .svg .txt .yaml .yml
```

Large `.duckdb`, `.pdf`, `.png`, and `.svg` files have a conservative upload
size limit.

### Full Command Reference

See `commands.md` for the generated command manual.
