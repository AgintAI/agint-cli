# Agint CLI

A command-line interface (CLI) client for interacting with Agint.

## Installation

Run the install script — it creates a virtual environment, installs the CLI, and prompts you for your API credentials:

```bash
curl -sSL https://raw.githubusercontent.com/AgintAI/agint-cli/main/install.sh | bash
```

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

```bash
# Analyze a stock
dagify compose "Analyze a stock using fundamental data" --ascii --intelligence 5

```

```bash
# Coordinate a complex series of events
dagify compose "3 events A B C, happen concurrently with no dependencies on each other,                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                          
             but then AB happens after A and B and likewise for AC and BC and lastly                                                                                                                                                                       
                                                                                                                                                                                                                                                                                                                          
                 they all join at ABC concurrently" --ascii --intelligence 5

```

```bash
# Refine a workflow to add more detail to specific nodes
dagify refine "Add more detailed instructions to the data cleaning step" workflow.yaml   --ascii

```

```bash
# Improve a machine learning workflow with hyperparameter tuning                                                                                                                                                                                    

cat ml_pipeline.yaml | dagify refine "Turn the hyperparameters up to 11" -   
```

```bash
# Compose a db schema for a blog, output it in json format

schemagin compose "Blog schema with tags" --format=json > schema.json  

```

```bash
# Create a local database and from a dynamically generated schema
schemagin compose "a database schema for a relational file system backing the metadata and contents of every file on an operating system  "                                                                                                                                                                  
         | agiwrite schema - --target-db=instant.db    
                                                                                                                                
```
```bash
# Extract structured names and emails from a CSV file into a local DuckDB database
datagin ingest "Extract names,emails" messy_input_data.txt --output-agilink ./local.duckdb                                                                                                                                                                             
```

```bash
# Extract and structure the first 50 invoices from a PDF document                                                                                                                                
datagin ingest --rows=50 "Parse invoices" invoices.pdf --output-agilink agilink://raw_invoices                                                                                                                                                                                                                                                                                                     
# Structure skewed JSON data provided via stdin into agilink                                                                                                                                 
cat data.json | datagin ingest "Structure JSON" - --output-agilink ./local.duckdb    

```
