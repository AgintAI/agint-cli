                                                                                
 Usage: dagify [OPTIONS] COMMAND [ARGS]...                                      
                                                                                
 CLI for dagify                                                                 
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.      │
│ --show-completion             Show completion for the current shell, to copy │
│                               it or customize the installation.              │
│ --help                        Show this message and exit.                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ compose  Create a workflow DAG using detailed natural-language.              │
│ refine   Refines an existing workflow by improving metadata, details,        │
│          instructions and tags.                                              │
│ resolve  Executes one pass of AI-assisted refinement to upgrade the DAG to a │
│          more concrete type.                                                 │
│ compile  Compiles a DAG into an executable format.                           │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: dagent [OPTIONS] COMMAND [ARGS]...                                      
                                                                                
 CLI for dagent                                                                 
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.      │
│ --show-completion             Show completion for the current shell, to copy │
│                               it or customize the installation.              │
│ --help                        Show this message and exit.                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ validate    Validates the correctness of a DAG by checking its structure,    │
│             dependencies, and execution feasibility.                         │
│ optimize    Optimizes AI-driven DAG nodes (e.g., prompts, spec stages) to    │
│             improve accuracy and reliability.                                │
│ execute     Execute a DAG plan with structured input and AI-assisted         │
│             processing.                                                      │
│ interpret   Generates a DAG plan dynamically and executes it immediately.    │
│ synthesize  Generates a DAG plan, compiles it to executable code, and        │
│             executes it.                                                     │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: schemagin [OPTIONS] COMMAND [ARGS]...                                   
                                                                                
 CLI for schemagin                                                              
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.      │
│ --show-completion             Show completion for the current shell, to copy │
│                               it or customize the installation.              │
│ --help                        Show this message and exit.                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ compose    Create a completely new data schema from a natural‑language       │
│            prompt.                                                           │
│ refine     Iteratively improve or extend an existing schema. Accepts         │
│            structured schema                                                 │
│ visualize  Render a schema diagram and export it to various formats.         │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: datagin [OPTIONS] COMMAND [ARGS]...                                     
                                                                                
 CLI for datagin                                                                
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.      │
│ --show-completion             Show completion for the current shell, to copy │
│                               it or customize the installation.              │
│ --help                        Show this message and exit.                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ ingest      Extract and structure unstructured data using intuitive          │
│             natural-language prompts.                                        │
│ synthesize  Generate synthetic data based on schema and prompt.              │
│ transform   Convert and adapt unstructured data between different schemas    │
│             using natural-language.                                          │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: agicat [OPTIONS] COMMAND [ARGS]...                                      
                                                                                
 CLI for agicat                                                                 
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.      │
│ --show-completion             Show completion for the current shell, to copy │
│                               it or customize the installation.              │
│ --help                        Show this message and exit.                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ schema  Extract schema from a given database and output it in the desired    │
│         format.                                                              │
│ data    Extract data from a given database and output it in the desired      │
│         format.                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: agiwrite [OPTIONS] COMMAND [ARGS]...                                    
                                                                                
 CLI for agiwrite                                                               
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.      │
│ --show-completion             Show completion for the current shell, to copy │
│                               it or customize the installation.              │
│ --help                        Show this message and exit.                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ schema  Write schema to target database.                                     │
│ data    Write schema and data to target database.                            │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: agitransfer [OPTIONS] COMMAND [ARGS]...                                 
                                                                                
 CLI for agitransfer                                                            
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.      │
│ --show-completion             Show completion for the current shell, to copy │
│                               it or customize the installation.              │
│ --help                        Show this message and exit.                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ get-user-path  Get a user's path in the AGI volume based on their API key.   │
│ get-file       Retrieve a file from storage.                                 │
│ zip-directory  Convert a folder to a zip and return an S3 presigned link for │
│                download.                                                     │
│ upload-file    Upload a local file or directory directly to AGI storage.     │
│ delete         Delete a file or directory from AGI storage.                  │
│ create-git     Initialize the user's root directory as a Git repo and        │
│                associate it with a GitHub URL.                               │
│ get-github     Retrieve the GitHub repository URL associated with the user.  │
│ update-git     Perform git add, commit, and push on the user's root          │
│                directory.                                                    │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: dagify compose [OPTIONS] PROMPT [CONTEXT]                               
                                                                                
 Create a workflow DAG using detailed natural-language.                         
                                                                                
 Generate detailed workflow graphs for any process or task using AI-assisted    
 composition.                                                                   
                                                                                
                                                                                
                                                                                
                                                                                
     Examples:                                                                  
                                                                                
                                                                                
         # Create a workflow for analyzing a stock                              
                                                                                
         dagify compose "create a workflow for analyzing a stock, make it       
 reasonably sophisticated, and use fundamental data"                            
                                                                                
                                                                                
                                                                                
         # Create a workflow that can help a levels.fyi recruiter help a        
 candidate negotiate                                                            
                                                                                
         echo "a workflow to help a software engineer who has a job offer       
 negotiate his offer with a company." | pbcopy                                  
                                                                                
         pbpaste | dagify compose - --intelligence 0 --ascii                    
                                                                                
                                                                                
                                                                                
         # Create a workflow for a autobiographical novel                       
                                                                                
         dagify compose "a workflow for writing an autobiographical novel,      
                                                                                
             branch the workflow to compose each chapter concurrently and       
                                                                                
             each chapter's paragraph as well. Make it 12 chapters with 3 parts 
 in each chapter."                                                              
                                                                                
                                                                                
                                                                                
         # Create a workflow that demonstates concurrent processing             
                                                                                
         dagify compose "3 events A B C, happen concurrently with no            
 dependencies on each other,                                                    
                                                                                
             but then AB happens after A and B and likewise for AC and BC and   
 lastly                                                                         
                                                                                
                 they all join at ABC concurrently" --ascii --intelligence 0    
                                                                                
                                                                                
                                                                                
         # Create a machine learning pipeline                                   
                                                                                
         dagify compose "a workflow of a feedforward neural network with 12     
 layers,                                                                        
                                                                                
             where each layer has 6 nodes, each of which are evaluated          
 concurrently. "                                                                
                                                                                
                                                                                
                                                                                
         # Create a Transformer                                                 
                                                                                
         dagify compose "a transformer architecture for GPT-5" --intelligence   
 50                                                                             
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    prompt       TEXT       Description of the process or workflow to       │
│                              generate a DAG for                              │
│                              [required]                                      │
│      context      [CONTEXT]  Workflow context - can be a JSON file, agilink  │
│                              URI, JSON string, or database connection. Use   │
│                              '-' for stdin                                   │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --type                                TEXT     Type of DAG to generate       │
│                                                (plain_text, typed, spec,     │
│                                                stub, shim, pure)             │
│                                                [default: typed]              │
│ --intelligence                        INTEGER  Intelligence level (0-50) for │
│                                                AI-assisted DAG generation    │
│                                                [default: 0]                  │
│ --mode                                TEXT     DAG modify mode: full,        │
│                                                node-delta, or dag-delta      │
│                                                [default: full]               │
│ --patch-fast-attempts                 INTEGER  Number of fast patch attempts │
│                                                [default: 1]                  │
│ --patch-planning-attempts             INTEGER  Number of full patch attempts │
│                                                [default: 1]                  │
│ --patch-schema-diff,--no-patc…                 Enable schema diff escalation │
│                                                during patch planning         │
│                                                [default: True]               │
│ --patch-strict,--no-patch-str…                 Enable strict JSON patch      │
│                                                validation                    │
│ --concurrency                         INTEGER  Maximum concurrent node       │
│                                                operations                    │
│                                                [default: 32]                 │
│ --tools                               TEXT     YAML/JSON tool catalog file   │
│                                                or inline catalog for Dagify  │
│                                                tool selection                │
│ --tool-choice-mode                    TEXT     Override the catalog's tool   │
│                                                choice mode for generated     │
│                                                nodes                         │
│ --tool-selection-convention           TEXT     Dynamic schema convention for │
│                                                catalog-bound tool selection  │
│                                                [default: specialized]        │
│ --seed                                INTEGER  Seed for deterministic        │
│                                                workflow generation           │
│ --format                              TEXT     Format for DAG output (yaml,  │
│                                                json)                         │
│                                                [default: yaml]               │
│ --visual                              TEXT     Format(s) for DAG             │
│                                                visualization (d2, graphviz,  │
│                                                ascii)                        │
│ --ascii                                        Show ASCII visualization of   │
│                                                the generated DAG             │
│ --output-dir                          TEXT     Directory to save the         │
│                                                generated DAG and             │
│                                                visualization                 │
│                                                [default: ./outputs/dagify/]  │
│ --verbose                                      Enable verbose output         │
│ --help                                         Show this message and exit.   │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: dagify refine [OPTIONS] PROMPT [WORKFLOW]                               
                                                                                
 Refines an existing workflow by improving metadata, details, instructions and  
 tags.                                                                          
                                                                                
 Enhance and extend already composed DAGs with additional context,              
 requirements, or improvements.                                                 
                                                                                
                                                                                
                                                                                
                                                                                
     Examples:                                                                  
                                                                                
                                                                                
         # Refine a workflow to add more detail to specific nodes               
                                                                                
         dagify refine "Add more detailed instructions to the data cleaning     
 step" workflow.yaml                                                            
                                                                                
                                                                                
                                                                                
         # Add error handling to all nodes in a workflow                        
                                                                                
         dagify refine "Add error handling to all nodes" complex_workflow.json  
 --ascii                                                                        
                                                                                
                                                                                
                                                                                
         # Improve a machine learning workflow with hyperparameter tuning       
                                                                                
         cat ml_pipeline.yaml | dagify refine "Add hyperparameter tuning steps  
 after model training" -                                                        
                                                                                
                                                                                
                                                                                
         # Convert a sequential workflow to a parallel one where possible       
                                                                                
         dagify refine "Optimize by running independent nodes in parallel"      
 workflow.yaml --intelligence 50                                                
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    prompt        TEXT        Description of the refinement to be applied   │
│                                [required]                                    │
│      workflow      [WORKFLOW]  Workflow DAG source - can be a JSON file,     │
│                                agilink URI, or JSON string. Use '-' for      │
│                                stdin                                         │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --intelligence                        INTEGER  Intelligence level (0-50) for │
│                                                AI-assisted DAG generation    │
│                                                [default: 0]                  │
│ --mode                                TEXT     DAG modify mode: full,        │
│                                                node-delta, or dag-delta      │
│                                                [default: full]               │
│ --patch-fast-attempts                 INTEGER  Fast patch attempts for patch │
│                                                planning                      │
│                                                [default: 1]                  │
│ --patch-planning-attempts             INTEGER  Planning patch attempts for   │
│                                                patch planning                │
│                                                [default: 1]                  │
│ --patch-schema-diff,--no-patc…                 Enable schema diff escalation │
│                                                during patch planning         │
│                                                [default: True]               │
│ --patch-strict,--no-patch-str…                 Enable strict JSON patch      │
│                                                validation                    │
│ --concurrency                         INTEGER  Maximum concurrent node       │
│                                                operations                    │
│                                                [default: 4]                  │
│ --seed                                INTEGER  Seed for deterministic        │
│                                                workflow generation           │
│ --tools                               TEXT     YAML/JSON tool catalog file   │
│                                                or inline catalog for Dagify  │
│                                                tool selection                │
│ --tool-choice-mode                    TEXT     Override the catalog's tool   │
│                                                choice mode for modified      │
│                                                nodes                         │
│ --tool-selection-convention           TEXT     Dynamic schema convention for │
│                                                catalog-bound tool selection  │
│                                                [default: specialized]        │
│ --context                             TEXT     Optional supporting context   │
│                                                for the refinement request    │
│ --format                              TEXT     Format for DAG output (yaml,  │
│                                                json)                         │
│                                                [default: yaml]               │
│ --visual                              TEXT     Format(s) for DAG             │
│                                                visualization (d2, graphviz,  │
│                                                ascii)                        │
│ --ascii                                        Display ASCII visualization   │
│                                                of the generated DAG          │
│ --output-dir                          TEXT     Directory to save the refined │
│                                                DAG and viz                   │
│ --verbose                                      Enable verbose output         │
│ --yaml-display                                 Display YAML representation   │
│                                                of the DAG in console when    │
│                                                not piped                     │
│ --help                                         Show this message and exit.   │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: dagify resolve [OPTIONS] WORKFLOW                                       
                                                                                
 Executes one pass of AI-assisted refinement to upgrade the DAG to a more       
 concrete type.                                                                 
                                                                                
 Transform DAGs from abstract descriptions to more concrete implementations     
 with detailed specifications.                                                  
                                                                                
                                                                                
                                                                                
                                                                                
     Examples:                                                                  
                                                                                
                                                                                
         # Resolve a plain text DAG to a typed DAG                              
                                                                                
         dagify resolve plain_workflow.yaml --ascii                             
                                                                                
                                                                                
                                                                                
         # Resolve a workflow with increased intelligence for better results    
                                                                                
         dagify resolve workflow.json --intelligence 50 --yaml-display          
                                                                                
                                                                                
                                                                                
         # Pipe a workflow and display the resolved version with visualization  
                                                                                
         cat abstract_workflow.yaml | dagify resolve - --visual d2 --ascii      
                                                                                
                                                                                
                                                                                
         # Resolve a DAG and save to a specific directory                       
                                                                                
         dagify resolve workflow.yaml --output-dir ./my_workflows/              
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    workflow      TEXT  The workflow DAG to resolve (file path, JSON        │
│                          string, or agilink URI)                             │
│                          [required]                                          │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --intelligence                        INTEGER  Intelligence level (0-50) for │
│                                                AI-assisted DAG generation    │
│                                                [default: 0]                  │
│ --mode                                TEXT     DAG modify mode: full,        │
│                                                node-delta, or dag-delta      │
│                                                [default: full]               │
│ --patch-fast-attempts                 INTEGER  Fast patch attempts for patch │
│                                                planning                      │
│                                                [default: 1]                  │
│ --patch-planning-attempts             INTEGER  Planning patch attempts for   │
│                                                patch planning                │
│                                                [default: 1]                  │
│ --patch-schema-diff,--no-patc…                 Enable schema diff escalation │
│                                                during patch planning         │
│                                                [default: True]               │
│ --patch-strict,--no-patch-str…                 Enable strict JSON patch      │
│                                                validation                    │
│ --concurrency                         INTEGER  Maximum concurrent node       │
│                                                operations                    │
│                                                [default: 4]                  │
│ --seed                                INTEGER  Seed for deterministic        │
│                                                workflow generation           │
│ --tools                               TEXT     YAML/JSON tool catalog file   │
│                                                or inline catalog for         │
│                                                resolving selected tools      │
│ --guidance                            TEXT     Optional guidance for the     │
│                                                resolve transition            │
│ --context                             TEXT     Optional supporting context   │
│                                                for the resolve transition    │
│ --format                              TEXT     Format for DAG output (yaml,  │
│                                                json)                         │
│                                                [default: yaml]               │
│ --visual                              TEXT     Format(s) for DAG             │
│                                                visualization (d2, graphviz,  │
│                                                ascii)                        │
│ --ascii                                        Show ASCII visualization of   │
│                                                the generated DAG             │
│ --output-dir                          TEXT     Directory to save the         │
│                                                resolved DAG and viz          │
│ --verbose                                      Enable verbose output         │
│ --yaml-display                                 Display YAML representation   │
│                                                of the DAG in console when    │
│                                                not piped                     │
│ --help                                         Show this message and exit.   │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: dagify compile [OPTIONS] [WORKFLOW]                                     
                                                                                
 Compiles a DAG into an executable format.                                      
                                                                                
 The compilation process transforms abstract workflow definitions into          
 concrete, executable code.                                                     
                                                                                
                                                                                
                                                                                
                                                                                
     The compilation process involves two steps:                                
                                                                                
     1. Resolving the DAG to the specified type floor                           
     2. (Optional) Converting to a target format                                
                                                                                
                                                                                
                                                                                
     If no build target is specified, outputs the resolved DAG in YAML format.  
                                                                                
                                                                                
                                                                                
                                                                                
     Examples:                                                                  
                                                                                
                                                                                
         # Compile a DAG to CrewAI format                                       
                                                                                
         dagify compile workflow.yaml --build-target crewai                     
                                                                                
                                                                                
                                                                                
         # Compile a workflow ensuring it meets minimum typed requirements      
                                                                                
         dagify compile workflow.json --type-floor typed --ascii                
                                                                                
                                                                                
                                                                                
         # Process piped input and compile to WDL format                        
                                                                                
         cat complex_workflow.yaml | dagify compile - --build-target wdl        
                                                                                
                                                                                
                                                                                
         # Compile with increased intelligence for better code generation       
                                                                                
         dagify compile workflow.yaml --build-target crewai-flat --intelligence 
 50                                                                             
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│   workflow      [WORKFLOW]  The workflow DAG to compile (file path, JSON     │
│                             string, or agilink URI). Use '-' for stdin       │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --type-floor                          TEXT     Minimum DAG type to resolve   │
│                                                to before compilation         │
│                                                [default: typed]              │
│ --build-target                        TEXT     Target format for compilation │
│                                                (crewai, crewai-flat,         │
│                                                langchain, wdl, wdl-shims,    │
│                                                baml)                         │
│ --intelligence                        INTEGER  Intelligence level (0-50) for │
│                                                AI-assisted compilation       │
│                                                [default: 0]                  │
│ --mode                                TEXT     DAG modify mode: full,        │
│                                                node-delta, or dag-delta      │
│                                                [default: full]               │
│ --patch-fast-attempts                 INTEGER  Number of fast patch attempts │
│                                                for patch planning            │
│                                                [default: 1]                  │
│ --patch-planning-attempts             INTEGER  Number of planning patch      │
│                                                attempts for patch planning   │
│                                                [default: 1]                  │
│ --patch-schema-diff,--no-patc…                 Enable schema diff escalation │
│                                                during patch planning         │
│                                                [default: True]               │
│ --patch-strict,--no-patch-str…                 Enable strict JSON patch      │
│                                                validation                    │
│ --concurrency                         INTEGER  Maximum concurrent node       │
│                                                operations                    │
│                                                [default: 4]                  │
│ --tools                               TEXT     YAML/JSON tool catalog file   │
│                                                or inline catalog for         │
│                                                resolving selected tools      │
│ --output-dir                          TEXT     Base directory for DAG        │
│                                                outputs                       │
│                                                [default: ./outputs/dagify]   │
│ --ascii                                        Show ASCII visualization of   │
│                                                the generated DAG             │
│ --verbose                                      Enable verbose output         │
│ --help                                         Show this message and exit.   │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: dagent validate [OPTIONS] WORKFLOW                                      
                                                                                
 Validates the correctness of a DAG by checking its structure, dependencies,    
 and execution feasibility.                                                     
                                                                                
 Performs comprehensive checks to ensure workflow integrity and executability   
 before deployment.                                                             
                                                                                
                                                                                
                                                                                
                                                                                
     Performs validation checks including:                                      
                                                                                
     - DAG structural integrity (node/edge consistency, cycles)                 
     - Execution compatibility (AI-executable steps, missing dependencies)      
     - Schema correctness for external data sources                             
                                                                                
                                                                                
                                                                                
                                                                                
     Examples:                                                                  
                                                                                
                                                                                
         # Validate a workflow with default settings                            
                                                                                
         dagent validate workflow.yaml                                          
                                                                                
                                                                                
                                                                                
         # Validate with strict checking to catch all potential issues          
                                                                                
         dagent validate complex_workflow.json --strict                         
                                                                                
                                                                                
                                                                                
         # Validate a workflow from stdin                                       
                                                                                
         cat generated_workflow.yaml | dagent validate - --verbose              
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    workflow      TEXT  The DAG workflow to validate. Can be a DAGify JSON  │
│                          file, agilink URI, or DAG JSON string (stdin)       │
│                          [required]                                          │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --strict           Enable strict validation (fail on warnings)               │
│ --verbose          Enable verbose output                                     │
│ --help             Show this message and exit.                               │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: dagent optimize [OPTIONS] WORKFLOW TEST_DATA                            
                                                                                
 Optimizes AI-driven DAG nodes (e.g., prompts, spec stages) to improve accuracy 
 and reliability.                                                               
                                                                                
 Fine-tunes workflow components against test data to maximize performance and   
 result quality.                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     Optimization can adjust:                                                   
                                                                                
     - Prompt structure                                                         
     - Spec-level AI-generated values                                           
     - Other AI-dependent nodes in the DAG                                      
                                                                                
                                                                                
                                                                                
                                                                                
     Examples:                                                                  
                                                                                
                                                                                
         # Optimize a workflow against test data using accuracy metric          
                                                                                
         dagent optimize workflow.yaml test_data.csv --metric accuracy          
                                                                                
                                                                                
                                                                                
         # Run extended optimization with more iterations for better results    
                                                                                
         dagent optimize ai_workflow.yaml tuning_set.parquet --max-iterations   
 20                                                                             
                                                                                
                                                                                
                                                                                
         # Optimize using custom metrics with verbose output                    
                                                                                
         dagent optimize workflow.json evaluation_data.json --metric custom     
 --verbose                                                                      
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    workflow       TEXT  The DAG workflow to optimize. Can be a DAGify JSON │
│                           file, agilink URI, or DAG JSON string (stdin)      │
│                           [required]                                         │
│ *    test_data      TEXT  The test dataset to optimize against. Can be a     │
│                           structured data file (JSON, CSV, Parquet) or       │
│                           agilink URI                                        │
│                           [required]                                         │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --metric                TEXT     Optimization metric to use                  │
│                                  [default: accuracy]                         │
│ --max-iterations        INTEGER  Maximum optimization passes [default: 10]   │
│ --output-dir            TEXT     Directory to save results                   │
│                                  [default: ./outputs/optimized/dagent/]      │
│ --verbose                        Enable verbose output                       │
│ --help                           Show this message and exit.                 │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: dagent execute [OPTIONS] [WORKFLOW] [CONTEXT]                           
                                                                                
 Execute a DAG plan with structured input and AI-assisted processing.           
                                                                                
 Runs workflows with optional context and input, generating structured outputs  
 from each processing node.                                                     
                                                                                
                                                                                
                                                                                
                                                                                
     Features:                                                                  
                                                                                
     - Saves the full execution results to a file in the output directory       
                                                                                
     - Displays final node outputs to stderr                                    
                                                                                
     - Pipes full results to stdout if requested                                
                                                                                
     - Supports JIT refinement during execution (when enabled)                  
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     Examples:                                                                  
                                                                                
                                                                                
         # Execute from YAML file and save results to                           
 ./outputs/dagent/workflow/execution_results/                                   
                                                                                
         dagent execute workflow.yaml --output-dir ./outputs/dagent/            
                                                                                
                                                                                
                                                                                
         # Execute from JSON file with external context                         
                                                                                
         dagent execute workflow.json context.csv                               
                                                                                
                                                                                
                                                                                
         # Execute from stdin                                                   
                                                                                
         cat my_dag.json | dagent execute -                                     
                                                                                
                                                                                
                                                                                
         # Execute a CrewAI project in the current directory                    
                                                                                
         dagent execute .                                                       
                                                                                
                                                                                
                                                                                
         # Execute a specific CrewAI project directory                          
                                                                                
         dagent execute ./my_crewai_project/ context.yaml                       
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│   workflow      [WORKFLOW]  Workflow DAG to execute. Can be a JSON file,     │
│                             agilink URI, or JSON string. Use '-' for stdin   │
│   context       [CONTEXT]   External context to provide during execution     │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --intelligence                INTEGER  Intelligence level (0-50) to          │
│                                        determine model selection             │
│                                        [default: 0]                          │
│ --jit                         TEXT     Just-in-time (JIT) refinement mode    │
│ --execution-type              TEXT     Execution backend for DAG plans       │
│                                        [default: llm]                        │
│ --mock-mode                   TEXT     Mock behavior for CodeDAG function    │
│                                        execution                             │
│                                        [default: llm]                        │
│ --denied-tool-policy          TEXT     Behavior when a runtime tool is not   │
│                                        allowlisted                           │
│                                        [default: fail]                       │
│ --tool-simulation-mode        TEXT     Simulation behavior for denied        │
│                                        runtime tools                         │
│                                        [default: llm]                        │
│ --input-validation            TEXT     Root-node input sufficiency policy:   │
│                                        require, warn, or skip                │
│                                        [default: require]                    │
│ --seed                        INTEGER  Seed for deterministic execution      │
│ --tools                       TEXT     Structured tool catalog YAML/JSON, a  │
│                                        path to one, or '-' for stdin         │
│ --allowed-tools               TEXT     Comma-separated allowlist of CLI      │
│                                        tools the runtime may execute         │
│ --allowed-tools-file          TEXT     File containing an allowlist of tools │
│                                        (one per line)                        │
│ --input                       TEXT     Structured input_args.yaml content, a │
│                                        path to one, or '-' for stdin         │
│ --output-format               TEXT     Format for execution results (yaml,   │
│                                        json)                                 │
│                                        [default: yaml]                       │
│ --output-dir                  TEXT     Base directory to save execution      │
│                                        results                               │
│                                        [default: ./outputs/dagent/]          │
│ --output-scope                TEXT     Workflow value to emit/save:          │
│                                        all-nodes, terminal-nodes, or         │
│                                        nodes:name_a,name_b                   │
│                                        [default: all-nodes]                  │
│ --view-scope                  TEXT     Human view to display on stderr:      │
│                                        auto, terminal-nodes, all-nodes,      │
│                                        nodes:name_a,name_b, or none          │
│                                        [default: terminal-nodes]             │
│ --verbose                              Enable verbose output                 │
│ --help                                 Show this message and exit.           │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: dagent interpret [OPTIONS] [TASK] [CONTEXT]                             
                                                                                
 Generates a DAG plan dynamically and executes it immediately.                  
                                                                                
 Creates and runs workflows on-the-fly based on natural language descriptions,  
 without saving intermediate DAG definitions.                                   
                                                                                
                                                                                
                                                                                
                                                                                
     Features:                                                                  
                                                                                
     - One-shot workflow creation and execution                                 
                                                                                
     - Integration with external data sources                                   
                                                                                
     - Support for tools and system commands                                    
                                                                                
     - JIT refinement capabilities                                              
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     Examples:                                                                  
                                                                                
                                                                                
         # Analyze data and generate a report in one command                    
                                                                                
         dagent interpret "Analyze sales data and generate a report"            
 sales_data.csv                                                                 
                                                                                
                                                                                
                                                                                
         # Run a CI/CD pipeline with access to development tools                
                                                                                
         dagent interpret "Run a CI/CD pipeline for my project" --allowed-tools 
 git,docker,kubectl                                                             
                                                                                
                                                                                
                                                                                
         # Process data with recursive workflow generation                      
                                                                                
         dagent interpret "Process customer data and generate insights"         
 customer_data.csv --recursive                                                  
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│   task         [TASK]     Natural language description of the DAG plan       │
│   context      [CONTEXT]  Input context dataset or connection                │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --recursive                       Allow recursively generated DAGs           │
│ --jit                       TEXT  Just-in-time (JIT) refinement mode         │
│ --allowed-tools             TEXT  Comma-separated list of CLI tools          │
│                                   available in the runtime                   │
│ --allowed-tools-file        TEXT  File containing an allowlist of tools (one │
│                                   per line)                                  │
│ --output-dir                TEXT  Directory to save results                  │
│                                   [default: ./outputs/dagent/]               │
│ --verbose                         Enable verbose output                      │
│ --help                            Show this message and exit.                │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: dagent synthesize [OPTIONS] [TASK] [CONTEXT]                            
                                                                                
 Generates a DAG plan, compiles it to executable code, and executes it.         
                                                                                
 End-to-end workflow generation, compilation and execution in a single command  
 for maximum automation.                                                        
                                                                                
                                                                                
                                                                                
                                                                                
     Features:                                                                  
                                                                                
     - All-in-one workflow generation and execution                             
                                                                                
     - Persistent runtime code compilation                                      
                                                                                
     - Integration with external tools and data sources                         
                                                                                
     - Support for recursive workflow generation                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     Examples:                                                                  
                                                                                
                                                                                
         # Create and run an ETL pipeline with database connection              
                                                                                
         dagent synthesize "Create an ETL pipeline for user data"               
 db_connection_string                                                           
                                                                                
                                                                                
                                                                                
         # Build and deploy a web application with CI/CD tools                  
                                                                                
         dagent synthesize "Build and deploy the webapp" --allowed-tools        
 git,docker --runtime-dir ./runtime/                                            
                                                                                
                                                                                
                                                                                
         # Process data with custom output directory                            
                                                                                
         dagent synthesize "Process medical images and generate reports"        
 data_folder/ --output-dir ./medical_results/                                   
                                                                                
                                                                                
                                                                                
         # Create a complex analysis workflow with high intelligence setting    
                                                                                
         dagent synthesize "Analyze market trends and predict future patterns"  
 market_data.csv --intelligence 50                                              
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│   task         [TASK]     Natural language description of the DAG            │
│   context      [CONTEXT]  Input context dataset or connection                │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --recursive                       Allow recursively generated DAGs           │
│ --jit                       TEXT  Just-in-time (JIT) refinement mode         │
│ --allowed-tools             TEXT  Comma-separated list of CLI tools          │
│                                   available in the runtime                   │
│ --allowed-tools-file        TEXT  File containing an allowlist of tools (one │
│                                   per line)                                  │
│ --runtime-dir               TEXT  Directory where compiled code will be      │
│                                   stored and registered                      │
│                                   [default: ./outputs/dagent/runtime/]       │
│ --output-dir                TEXT  Directory to save execution results        │
│                                   [default: ./outputs/dagent/]               │
│ --verbose                         Enable verbose output                      │
│ --help                            Show this message and exit.                │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: schemagin compose [OPTIONS] PROMPT                                      
                                                                                
 Create a completely new data schema from a natural‑language prompt.            
                                                                                
 Ideal to quickly set up a database schema for a new project or structuring     
 mock datasets.                                                                 
                                                                                
                                                                                
                                                                                
                                                                                
         Examples:                                                              
                                                                                
                                                                                
             # JSON schema with DBML visualization from an existing schema      
 context                                                                        
                                                                                
             schemagin compose --format=json -F dbml "Blog posts & comments" -c 
 schema.yaml                                                                    
                                                                                
                                                                                
                                                                                
             # Schema generation via stdin, ASCII output, and increased         
 complexity without foreign keys                                                
                                                                                
             echo "Add audit log table" | schemagin compose --ascii             
 --no-foreign-keys --intelligence=80                                            
                                                                                
                                                                                
                                                                                
             # Compose a db schema for a blog, output it in json format         
                                                                                
             schemagin compose "Blog schema with tags" --format=json >          
 schema.json                                                                    
                                                                                
                                                                                
                                                                                
             # Refine and extend an existing JSON schema file                   
                                                                                
             schemagin refine "Add soft‑delete flags to all tables" -c          
 schema.json --format=json  > schema2.json                                      
                                                                                
                                                                                
                                                                                
             # Visualize a schema provided via stdin                            
                                                                                
             cat existing_schema.sql | schemagin visualize - --ascii            
                                                                                
                                                                                
                                                                                
             # Create a local database and from a dynamically generated schema  
                                                                                
             schemagin compose "a database schema for a relational file system  
 backing the metadata and contents of every file on an operating system  "      
                                                                                
                                                                                
         | agiwrite schema - --target-db=instant.db                             
                                                                                
                                                                                
                                                                                
             # Pipeline composition to immediate database deployment            
                                                                                
             schemagin compose "Order and invoice schema for online store"      
          | agiwrite schema --target-db=postgresql://user@host/db               
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    prompt      TEXT  Natural language description of the schema to         │
│                        generate.                                             │
│                        [required]                                            │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --context                             TEXT     Raw data, Path to existing    │
│                                                schema file, '-' for stdin,   │
│                                                or agilink:// URI             │
│ --ascii,--no-ascii                             Display ASCII visualization   │
│                                                of the schema.                │
│ --no-foreign-keys,--no-no-for…                 Disable foreign key           │
│                                                constraints in the generated  │
│                                                schema.                       │
│ --format                              TEXT     Specify the output format of  │
│                                                the schema file.              │
│                                                [default: yaml]               │
│ --visual                              TEXT     Generate diagram outputs in   │
│                                                one or more format            │
│                                                <dot|dbml|d2>.                │
│ --output-dir                          TEXT     Base output directory path.   │
│                                                Defaults to                   │
│                                                outputs/schemagin/. A unique  │
│                                                subdirectory will be created  │
│                                                inside.                       │
│                                                [default: outputs/schemagin]  │
│ --intelligence                        INTEGER  Intelligence level. 0-100     │
│                                                [default: 0]                  │
│ --seed                                INTEGER  Set a seed value for          │
│                                                deterministic schema          │
│                                                generation.                   │
│ --verbose,--no-verbose                         Show additional debug         │
│                                                information.                  │
│ --quiet                                        Suppress all output except    │
│                                                critical errors.              │
│ --help                                         Show this message and exit.   │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: schemagin refine [OPTIONS] PROMPT                                       
                                                                                
 Iteratively improve or extend an existing schema. Accepts structured schema    
                                                                                
 definitions from files, stdin, or explicit database links as context.          
                                                                                
                                                                                
                                                                                
                                                                                
         Examples:                                                              
                                                                                
                                                                                
             # Create a base schema for a blog with tags                        
                                                                                
             schemagin compose "Blog schema with tags" --format=yaml >          
 schema.yaml                                                                    
                                                                                
                                                                                
                                                                                
             # Refine an existing schema, output in SQL, with DBML              
 visualization                                                                  
                                                                                
             schemagin refine --format=sql -F dbml "Add analytics for each      
 page" -c schema.yaml                                                           
                                                                                
                                                                                
                                                                                
             # Refine with stdin input, convert yaml to json format             
                                                                                
             echo "Add an audit log table and a users banned table" |           
                                                                                
                                                                                
     schemagin refine - -c schema.yaml --ascii --no-foreign-keys                
 --intelligence=80 --format=json                                                
                                                                                
                                                                                
                                                                                
             # Refine by adding an audit log with enhanced intelligence         
                                                                                
             schemagin refine "Add an audit log table" -c schema.yaml --ascii   
 --no-foreign-keys --intelligence=80 --format=json                              
                                                                                
                                                                                
                                                                                
             # Add soft-delete capability to all tables, converting yaml to     
 json                                                                           
                                                                                
             schemagin refine "Add soft‑delete flags to all tables" -c          
 schema.yaml --format=json > schema2.json                                       
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    prompt      TEXT  Natural language description of the refinements to    │
│                        make.                                                 │
│                        [required]                                            │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ *  --context                           TEXT     Path to existing schema      │
│                                                 file, '-' for stdin, or      │
│                                                 agilink:// URI               │
│                                                 [required]                   │
│    --format                            TEXT     Output format for the        │
│                                                 schema.                      │
│                                                 [default: yaml]              │
│    --ascii,--no-ascii                           Display ASCII visualization  │
│                                                 of the schema.               │
│    --no-foreign-keys,--no-no-f…                 Disable foreign key          │
│                                                 constraints in the generated │
│                                                 schema.                      │
│    --visual                            TEXT     Generate diagram outputs in  │
│                                                 one or more format           │
│                                                 <dot|dbml|d2>.               │
│    --output-dir                        TEXT     Base output directory path.  │
│                                                 Defaults to                  │
│                                                 outputs/schemagin/. A unique │
│                                                 subdirectory will be created │
│                                                 inside.                      │
│                                                 [default: outputs/schemagin] │
│    --intelligence                      INTEGER  Intelligence level. 0-100    │
│                                                 [default: 0]                 │
│    --seed                              INTEGER  Set a seed value for         │
│                                                 deterministic schema         │
│                                                 generation.                  │
│    --verbose,--no-verbose                       Show additional debug        │
│                                                 information.                 │
│    --quiet                                      Suppress all output except   │
│                                                 critical errors.             │
│    --help                                       Show this message and exit.  │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: schemagin visualize [OPTIONS] SCHEMA                                    
                                                                                
 Render a schema diagram and export it to various formats.                      
                                                                                
                                                                                
                                                                                
 Arguments:                                                                     
                                                                                
   <schema> Provide the schema input from: YAML/JSON/SQL/DBML file, agilink://  
 or URI stdin (indicated by "-")                                                
                                                                                
                                                                                
                                                                                
 Default Outputs:                                                               
                                                                                
   - Diagram files: `<basename>.<fmt>` for each format specified with `-F`.     
                                                                                
   - Inline ASCII diagram output to stdout if `--ascii` is set.                 
                                                                                
   - Concurrently exported schema file: `<basename>.<ext>` if `-f` is used.     
                                                                                
                                                                                
                                                                                
                                                                                
 Examples:                                                                      
                                                                                
     # Visualize DBML schema in ASCII art and export as D2 format               
                                                                                
     schemagin visualize schema.dbml --ascii -F d2                              
                                                                                
                                                                                
                                                                                
     # Convert D2 output to a PNG image (using d2 tool)                         
                                                                                
     d2 ./outputs/schemagin/visualizations/schema.d2 schema.png && open         
 schema.png                                                                     
                                                                                
                                                                                
                                                                                
     # Visualize schema from Agilink URI with JSON export and DOT format        
                                                                                
     schemagin visualize agilink://raw_customers --format=json -F dot           
                                                                                
                                                                                
                                                                                
     # Visualize a schema from stdin with ASCII output                          
                                                                                
     cat existing_schema.sql | schemagin visualize - --ascii                    
                                                                                
                                                                                
                                                                                
     # Generate ASCII and DOT format from JSON schema via stdin                 
                                                                                
     cat schema.json | schemagin visualize - --ascii -F dot                     
                                                                                
                                                                                
                                                                                
     # Visualize Agilink schema in both DBML and DOT formats                    
                                                                                
   schemagin visualize agilink://raw_schema -F dbml -F dot                      
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    schema      TEXT  Path to schema file, '-' for stdin, or agilink:// URI │
│                        [required]                                            │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --ascii,--no-ascii                  Display ASCII visualization of the       │
│                                     schema.                                  │
│ --format                      TEXT  Concurrently export the schema in the    │
│                                     specified format.                        │
│ --visual                      TEXT  Generate diagram outputs in one or more  │
│                                     format <dot|dbml|d2>.                    │
│                                     [default: d2]                            │
│ --output-dir                  TEXT  Output directory path. Defaults to       │
│                                     outputs/schemagin/                       │
│                                     [default: outputs/schemagin]             │
│ --verbose,--no-verbose              Show additional debug information.       │
│ --quiet                             Suppress all output except critical      │
│                                     errors.                                  │
│ --help                              Show this message and exit.              │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: datagin ingest [OPTIONS] PROMPT INPUT                                   
                                                                                
 Extract and structure unstructured data using intuitive natural-language       
 prompts.                                                                       
                                                                                
 Convert raw data into structured formats using AI-powered extraction           
 techniques.                                                                    
                                                                                
                                                                                
                                                                                
                                                                                
     Examples:                                                                  
                                                                                
                                                                                
         # Extract structured names and emails from a CSV file into a local     
 DuckDB database                                                                
                                                                                
         datagin ingest "Extract names,emails" messy_input_data.txt             
 --output-agilink ./local.duckdb                                                
                                                                                
                                                                                
                                                                                
         # Extract and structure the first 50 invoices from a PDF document      
                                                                                
         datagin ingest --rows=50 "Parse invoices" invoices.pdf                 
 --output-agilink agilink://raw_invoices                                        
                                                                                
                                                                                
                                                                                
         # Structure skewed JSON data provided via stdin into agilink           
                                                                                
         cat data.json | datagin ingest "Structure JSON" - --output-agilink     
 ./local.duckdb                                                                 
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    prompt      TEXT  Natural-language description providing guidance for   │
│                        the data extraction task.                             │
│                        [required]                                            │
│ *    input       TEXT  Source data provided via stdin ("-"), File path, or   │
│                        agilink:// URI                                        │
│                        [required]                                            │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --output-agilink              TEXT     Agilink URI where structured data     │
│                                        will be written                       │
│                                        [default: defaultdir]                 │
│ --output-dir                  TEXT     Base directory for output files       │
│                                        [default: ./outputs/datagin]          │
│ --intelligence                INTEGER  Intelligence level (0-100). 0-33:     │
│                                        Super fast small, 34-66: Super fast   │
│                                        big, 67-100: Thinking mode            │
│                                        [default: 50]                         │
│ --rows                        INTEGER  Number of rows to transfer if input   │
│                                        is a large dataset                    │
│ --verbose,--no-verbose                 Show detailed processing output       │
│ --help                                 Show this message and exit.           │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: datagin synthesize [OPTIONS] PROMPT SCHEMA                              
                                                                                
 Generate synthetic data based on schema and prompt.                            
                                                                                
 Create realistic mock data for testing, development, and demonstration         
 purposes.                                                                      
                                                                                
                                                                                
                                                                                
                                                                                
     Examples:                                                                  
                                                                                
                                                                                
         # Generate a large dataset of realistic customer data for testing      
                                                                                
         datagin synthesize "Generate 100 realistic customer records"           
 schema.yaml --output-agilink "sqlite:///customers.db" --rows 100               
                                                                                
                                                                                
                                                                                
         # Create a small test dataset for order processing development         
                                                                                
         datagin synthesize "Create 5 test orders" "agilink://path/to/schema"   
 --output-agilink "duckdb:///orders.db" -r 5                                    
                                                                                
                                                                                
                                                                                
         # Quickly create test users from an inline schema definition           
                                                                                
         echo 'tables: users: columns: id: INTEGER name: TEXT' | datagin        
 synthesize "Make 2 users" - --output-agilink "sqlite:///:memory:" -r 2         
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    prompt      TEXT  Natural language description of data to generate      │
│                        [required]                                            │
│ *    schema      TEXT  Schema file path, inline YAML/JSON, or agilink URI    │
│                        [required]                                            │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --output-agilink              TEXT     Agilink URI where generated data will │
│                                        be stored                             │
│                                        [default: defaultdir]                 │
│ --output-dir                  TEXT     Base directory for output files       │
│                                        [default: ./outputs/datagin]          │
│ --intelligence                INTEGER  Intelligence level (0-100). 0-33:     │
│                                        Super fast small, 34-66: Super fast   │
│                                        big, 67-100: Thinking mode            │
│                                        [default: 50]                         │
│ --rows                        INTEGER  Number of rows to generate            │
│                                        [default: 10]                         │
│ --verbose,--no-verbose                 Show detailed processing output       │
│ --help                                 Show this message and exit.           │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: datagin transform [OPTIONS] PROMPT INPUT OUTPUT_AGILINK                 
                                                                                
 Convert and adapt unstructured data between different schemas using            
 natural-language.                                                              
                                                                                
 Transform, merge, and normalize datasets to fit your target schema             
 requirements.                                                                  
                                                                                
                                                                                
                                                                                
                                                                                
     Examples:                                                                  
                                                                                
                                                                                
         # Merge user and order data from a directory into a structured agilink 
                                                                                
         datagin transform "Merge user & order tables" ./data_folder/           
 agilink://merged_data                                                          
                                                                                
                                                                                
                                                                                
         # Preview anonymizing Personally Identifiable Information (PII)        
 transformation without applying                                                
                                                                                
         datagin transform --dry-run "Anonymize PII" agilink://raw_customers    
 agilink://anon_customers                                                       
                                                                                
                                                                                
                                                                                
         # Generate explicit schema transformation rules for manual review      
                                                                                
         datagin transform --explicit "Normalize transaction fields"            
 agilink://transactions agilink://normalized_transactions                       
                                                                                
                                                                                
                                                                                
         # Apply predefined schema transformation from an Agiform file          
                                                                                
         datagin transform --explicit=rules.agiform "Apply existing             
 transformation rules" agilink://source_data agilink://destination_data         
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    prompt              TEXT  Natural language guidance for executing the   │
│                                transformation                                │
│                                [required]                                    │
│ *    input               TEXT  Source data provided via stdin ("-"), File    │
│                                path, or agilink:// URI                       │
│                                [required]                                    │
│ *    output_agilink      TEXT  Agilink URI where transformed data will be    │
│                                stored                                        │
│                                [required]                                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --verbose,--no-verbose          Show detailed processing output              │
│ --help                          Show this message and exit.                  │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: agicat schema [OPTIONS] [SOURCE]                                        
                                                                                
 Extract schema from a given database and output it in the desired format.      
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│   source      [SOURCE]  Source path (DuckDB file, Postgres URL, or workspace │
│                         path)                                                │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --source-db                            TEXT  URI of the source database      │
│ --output-format                        TEXT  Output format for the schema.   │
│                                              Options: yaml, json             │
│                                              [default: yaml]                 │
│ --display-ascii,--no-display-a…              Display the schema as an ASCII  │
│                                              table                           │
│ --verbose,--no-verbose                       Show additional debug           │
│                                              information                     │
│ --help                                       Show this message and exit.     │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: agicat data [OPTIONS] [SOURCE]                                          
                                                                                
 Extract data from a given database and output it in the desired format.        
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│   source      [SOURCE]  Source path (DuckDB file, Postgres URL, or workspace │
│                         path)                                                │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --source-db                           TEXT     URI of the source database    │
│ --output-format                       TEXT     Output format for the data.   │
│                                                Options: csv, directory       │
│                                                [default: csv]                │
│ --max-rows                            INTEGER  Maximum number of rows to     │
│                                                fetch per table               │
│                                                [default: 1000]               │
│ --display-data,--no-display-d…                 Display the data in the       │
│                                                terminal                      │
│ --output-dir                          TEXT     Directory to save data files  │
│                                                (for directory mode)          │
│ --verbose,--no-verbose                         Show additional debug         │
│                                                information                   │
│ --help                                         Show this message and exit.   │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: agiwrite schema [OPTIONS] SCHEMA_FILE                                   
                                                                                
 Write schema to target database.                                               
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    schema_file      TEXT  Path to schema file or schema content [required] │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ *  --target-db                   TEXT  URI of the target database [required] │
│    --input-format                TEXT  Format of the input schema. Options:  │
│                                        yaml, json                            │
│                                        [default: yaml]                       │
│    --force,--no-force                  Overwrite the existing schema without │
│                                        confirmation                          │
│                                        [default: True]                       │
│    --verbose,--no-verbose              Show additional debug information     │
│    --help                              Show this message and exit.           │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: agiwrite data [OPTIONS] SCHEMA_FILE DATA_PATH                           
                                                                                
 Write schema and data to target database.                                      
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    schema_file      TEXT  Path to schema file or schema content [required] │
│ *    data_path        TEXT  Path to folder containing CSV files [required]   │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ *  --target-db                   TEXT  URI of the target database [required] │
│    --input-format                TEXT  Format of the input schema. Options:  │
│                                        yaml, json                            │
│                                        [default: yaml]                       │
│    --force,--no-force                  Overwrite existing data without       │
│                                        confirmation                          │
│                                        [default: True]                       │
│    --augment,--no-augment              Treat input data as updates to        │
│                                        existing rows by matching column      │
│                                        values                                │
│    --verbose,--no-verbose              Show additional debug information     │
│    --help                              Show this message and exit.           │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: agitransfer get-user-path [OPTIONS]                                     
                                                                                
 Get a user's path in the AGI volume based on their API key.                    
                                                                                
 If no API key is provided, uses the AGINT_APIKEY environment variable.         
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --verbose          Enable verbose output                                     │
│ --help             Show this message and exit.                               │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: agitransfer get-file [OPTIONS] PATH                                     
                                                                                
 Retrieve a file from storage.                                                  
                                                                                
 In direct mode, reads the file directly from EFS storage. In presigned mode,   
 copies the file to S3 and generates a download URL that expires after 1 hour.  
                                                                                
 If no API key is provided, uses the AGINT_APIKEY environment variable.         
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    path      TEXT  Path to file (can include agitransfer:// prefix)        │
│                      [required]                                              │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --presigned              Return a presigned URL instead of file content      │
│ --output           TEXT  Output file path (default: stdout)                  │
│ --verbose                Enable verbose output                               │
│ --help                   Show this message and exit.                         │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: agitransfer zip-directory [OPTIONS] DIRECTORY_PATH                      
                                                                                
 Convert a folder to a zip and return an S3 presigned link for download.        
                                                                                
 If no API key is provided, uses the AGINT_APIKEY environment variable.         
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    directory_path      TEXT  Directory path to zip (can include            │
│                                agitransfer:// prefix)                        │
│                                [required]                                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --verbose          Enable verbose output                                     │
│ --help             Show this message and exit.                               │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: agitransfer upload-file [OPTIONS] SOURCE DESTINATION                    
                                                                                
 Upload a local file or directory directly to AGI storage.                      
                                                                                
 If a directory path is provided as the source, it will be zipped before        
 uploading.                                                                     
 The destination path will be the specified path with '.zip' appended.          
                                                                                
 If no API key is provided, uses the AGINT_APIKEY environment variable.         
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    source           TEXT  Local file or directory path to upload.          │
│                             [required]                                       │
│ *    destination      TEXT  Destination path in AGI storage (can include     │
│                             agitransfer:// prefix).                          │
│                             [required]                                       │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --verbose          Enable verbose output.                                    │
│ --help             Show this message and exit.                               │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: agitransfer delete [OPTIONS] [PATH]                                     
                                                                                
 Delete a file or directory from AGI storage.                                   
                                                                                
 WARNING: If no path is provided, this will attempt to delete the entire        
 contents                                                                       
 of the user's root directory. Confirmation will be required unless --force is  
 used.                                                                          
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│   path      [PATH]  Path to file/directory to delete (can include            │
│                     agitransfer:// prefix). If omitted, deletes the user's   │
│                     root directory.                                          │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --force            Force deletion without confirmation (use with extreme     │
│                    caution, especially for root).                            │
│ --verbose          Enable verbose output.                                    │
│ --help             Show this message and exit.                               │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: agitransfer create-git [OPTIONS]                                        
                                                                                
 Initialize the user's root directory as a Git repo and associate it with a     
 GitHub URL.                                                                    
                                                                                
 Derives repo name from user email, attempts to init/push, and stores URL in    
 DynamoDB.                                                                      
 If no API key is provided, uses the AGINT_APIKEY environment variable.         
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --verbose          Enable verbose output.                                    │
│ --help             Show this message and exit.                               │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: agitransfer get-github [OPTIONS]                                        
                                                                                
 Retrieve the GitHub repository URL associated with the user.                   
                                                                                
 If no API key is provided, uses the AGINT_APIKEY environment variable.         
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --verbose          Enable verbose output.                                    │
│ --help             Show this message and exit.                               │
╰──────────────────────────────────────────────────────────────────────────────╯


                                                                                
 Usage: agitransfer update-git [OPTIONS] COMMIT_MESSAGE                         
                                                                                
 Perform git add, commit, and push on the user's root directory.                
                                                                                
 Requires the user's root directory to be an initialized Git repository.        
 If no API key is provided, uses the AGINT_APIKEY environment variable.         
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    commit_message      TEXT  The commit message to use for the update.     │
│                                [required]                                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --verbose          Enable verbose output.                                    │
│ --help             Show this message and exit.                               │
╰──────────────────────────────────────────────────────────────────────────────╯

