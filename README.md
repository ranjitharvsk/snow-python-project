# Python Project Template for Snowpark

Use this template to start writing data applications on Snowflake using Python.

# Set up snowcli < from [documentation](https://docs.snowflake.com/en/developer-guide/snowflake-cli-v2/installation/installation) >
## worth watching videos https://www.youtube.com/@snowflakedevelopers/playlists

brew tap snowflakedb/snowflake-cli
brew update

brew install snowflake-cli

snow --help

snow --info  
# to see the path that has config.toml
# open config.toml file to create the conection details and default connection
# add the following to the toml

default_connection_name = "trial1"

[connections.trial1]
account = "gcavadk-gk73809"
user = "RANJITHARVSK"
password = "********"
database = "CBA_CODECHALLENGE"
schema = "PUBLIC"
warehouse = "COMPUTE_WH"
role = "ACCOUNTADMIN"


# configring the default connection from terminal
snow connection set-default trial1
# you see the message "Default connection set to: trial"
# this is going to be the default connection when ever we are going to use connection name in CLI

# test the connection and see everything has been successfully configured
snow connection test --connection trial1
# The output should be
+----------------------------------------------------------+
| key             | value                                  |
|-----------------+----------------------------------------|
| Connection name | trial1                                 |
| Status          | OK                                     |
| Host            | gcavadk-gk73809.snowflakecomputing.com |
| Account         | gcavadk-gk73809                        |
| User            | RANJITHARVSK                           |
| Role            | ACCOUNTADMIN                           |
| Database        | CBA_CODECHALLENGE                      |
| Warehouse       | COMPUTE_WH                             |
+----------------------------------------------------------+



## Setup

Set the following environment variables with your Snowflake account information:

```bash
# Linux/MacOS
export SNOWSQL_ACCOUNT=<replace with your account identifer>
export SNOWSQL_USER=<replace with your username>
export SNOWSQL_ROLE=<replace with your role>
export SNOWSQL_PWD=<replace with your password>
export SNOWSQL_DATABASE=<replace with your database>
export SNOWSQL_SCHEMA=<replace with your schema>
export SNOWSQL_WAREHOUSE=<replace with your warehouse>
```

```powershell
# Windows/PowerShell
$env:SNOWSQL_ACCOUNT = "<replace with your account identifer>"
$env:SNOWSQL_USER = "<replace with your username>"
$env:SNOWSQL_ROLE = "<replace with your role>"
$env:SNOWSQL_PWD = "<replace with your password>"
$env:SNOWSQL_DATABASE = "<replace with your database>"
$env:SNOWSQL_SCHEMA = "<replace with your schema>"
$env:SNOWSQL_WAREHOUSE = "<replace with your warehouse>"

# [connections.trial1]
# account = "gcavadk-gk73809"
# user = "RANJITHARVSK"
# password = "*********"
# database = "CBA_CODECHALLENGE"
# schema = "PUBLIC"
# warehouse = "COMPUTE_WH"
# role = "ACCOUNTADMIN"
export SNOWSQL_ACCOUNT=gcavadk-gk73809
export SNOWSQL_USER=RANJITHARVSK
export SNOWSQL_ROLE=ACCOUNTADMIN
export SNOWSQL_PWD=********
export SNOWSQL_DATABASE=CBA_CODECHALLENGE
export SNOWSQL_SCHEMA=PUBLIC
export SNOWSQL_WAREHOUSE=COMPUTE_WH

```

Optional: You can set this env var permanently by editing your bash profile (on Linux/MacOS) or 
using the System Properties menu (on Windows).

### Install dependencies

Create and activate a conda environment using [Anaconda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands):

```bash
conda env create --file environment.yml
conda activate snowpark
```

### Configure IDE

#### VS Code

Press `Ctrl`+`Shift`+`P` to open the command palette, then select **Python: Select Interpreter** and select the **snowpark** interpreter under the **Conda** list.

#### PyCharm

Go to **File** > **Settings** > **Project** > **Python Interpreter** and select the snowpark interpreter.

## Prereqs

To develop your applications locally, you will need

- A Snowflake account
- Python 3.8 or greater
- An IDE or code editor (VS Code, PyCharm, etc.)

## Usage

Once you've set your credentials and installed the packages, you can test your connection to Snowflake by executing the stored procedure in [`app.py`](src/procs/app.py):

```bash
python src/app.py
```

You should see the following output:

```
------------------------------------------------------
|Hello world                                         |
------------------------------------------------------
|Welcome to Snowflake!                               |
|Learn more: https://www.snowflake.com/snowpark/     |
------------------------------------------------------
```

### Run tests

You can run the test suite locally from the project root:

```bash
python -m pytest
```

### Deploy to Snowflake

The GitHub Actions [workflow file](.github/workflows/build-and-deploy.yml) allows you to continously deploy your objects to Snowflake. When you're ready,
create secrets in your GitHub repository with the same name and values as the environment variables you created earler (`SNOWSQL_PWD`, `SNOWSQL_ACCOUNT`, etc.). The workflow will create a stage, upload the Python source code, and create the stored procedure object. For more information, see [`resources.sql`](resources.sql).

## Docs

- [Snowpark Developer Guide for Python](https://docs.snowflake.com/en/developer-guide/snowpark/python/index)
- [Creating Stored Procedures](https://docs.snowflake.com/en/developer-guide/snowpark/python/creating-sprocs)
- [Snowpark API Reference](https://docs.snowflake.com/developer-guide/snowpark/reference/python/index.html)

## Contributing

Have a question or ran into a bug? Please [file an issue](https://github.com/Snowflake-Labs/snowpark-python-template/issues/new) and let us know.

Have an idea for an improvement? Fork this repository and open a PR with your idea!
