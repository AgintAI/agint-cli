# Agint CLI

A command-line interface (CLI) client for interacting with Agint.

## Installation

Run the install script — it creates a virtual environment, installs the CLI,
creates a default workspace, and prompts you for your API credentials:

```bash
curl -sSL https://raw.githubusercontent.com/AgintAI/agint-cli/main/install.sh | bash
```

By default this installs into `~/agint`, stores credentials in `~/agint/.env`,
and creates `~/agint/work` for running commands. At the end of the install, the
script asks whether to open an activated shell in that workspace. If you answer
yes, it runs the equivalent of:

```bash
source ~/agint/.venv/bin/activate
cd ~/agint/work
```

On Windows Git Bash, the activation path is usually
`~/agint/.venv/Scripts/activate`; the installer prints the exact command for
your environment.

Run `exit` to return to your previous shell.

If you rerun the installer, it preserves `~/agint/.env`, moves the old install
to a timestamped backup such as `~/agint.backup.20260605173000`, and creates a
fresh install plus workspace.

Or install manually with pip:

```bash
pip install git+https://github.com/AgintAI/agint-cli.git
```

## Configuration

The client requires the following environment variables:

- `DOCKER_BUILDER_API_URL`: The URL of your Agint instance
- `AGINT_APIKEY`: Your Agint API key

You can set these in a `.env` file in your working directory or export them directly:

```bash
export DOCKER_BUILDER_API_URL=your-agint-instance
export AGINT_APIKEY=your-api-key
```
- Please reach out to accounts@agintai.com for an API Key if you are interested in our beta. 
- The endpoint url is subject to changes as we iterate through our beta testing phase. 

## Usage

- Please refer to `commands.md` to view the full manual for available commands

### Artifact sync

For generated-tool commands, the thin client keeps local generated artifacts and
the remote `agitransfer://` workspace in sync:

- before a command, selected local files in the current directory are uploaded to
  the authenticated user's remote workspace;
- after a successful command, the remote workspace is zipped and downloaded back
  into the current directory.

Run commands from a project/work directory, such as `~/agint/work`, instead of
the install root. The curl installer creates that workspace for this purpose.

The sync-enabled command groups are:

```text
agicat
agiwrite
dagify
dagent
schemagin
datagin
```

When the server advertises the `agicat` and `agiwrite` OpenAPI groups, the thin
client exposes direct `agicat` and `agiwrite` console commands. Older installs
can use the parent command form, such as `agi-tools agicat ...` or
`agi-tools agiwrite ...`.

This supports common generated artifacts such as schemas, DAGs, diagrams,
rendered outputs, DuckDB files, CSVs, Markdown, SQL, and source files. Synced
extensions include:

```text
.csv .d2 .dbml .dot .duckdb .flow .html .json .md .pdf .png .py .sql .svg .txt .yaml .yml
```

Large binary/rendered artifacts such as `.duckdb`, `.pdf`, `.png`, and `.svg`
are subject to a conservative size limit during upload.

### Example commands

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
  --ascii
```

```bash
# Improve a machine learning workflow with hyperparameter tuning
cat ml_pipeline.yaml \
  | dagify refine "Turn the hyperparameters up to 11" -
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

This repo includes marimo notebooks for trying the thin client examples locally
or in a browser.

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

The local notebook also has configuration fields for API URL and API key. Opening
it does not install or run anything automatically; use the notebook controls to
choose which setup, sanity-check, or example cells to run.

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

The local notebook runs the actual CLI commands. The WebAssembly notebook shows
the same copyable CLI commands, then makes the equivalent AGInt API calls
directly in the browser and renders stdout, stderr, ASCII output, and generated
files. Browser execution requires the AGInt API to allow CORS requests from the
GitHub Pages and molab origins. If the API is only available inside a VPN, users
must run the browser notebook from a browser that can reach that endpoint.
