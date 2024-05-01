# Project Structure

## Folder Structure

Opteryx's repository folder structure is described below:

~~~
opteryx/                 <- main opteryx library
 ├── connectors/         <- modules to connect to data sources
 ├── compiled/           <- cython modules
 ├── functions/          <- modules to execute functions within SQL statements
 ├── managers/           <- libraries responsible for key functional units
 │   ├── cache/          <- modules implementing caching systems
 │   ├── expression/     <- modules implementing expression evaluation
 │   ├── kvstore/        <- modules implementing interfacing with KV Stores
 │   └── schemes/        <- modules implementing storage schemes
 ├── models/             <- internal data models
 ├── operators/          <- modules implementing steps in the query plan
 ├── planner/            <- the planning and management of the query engine
 ├── virtual_data/       <- sample data (e.g. $planets, $astronauts, $satellites)
 ├── shared/             <- global resources
 ├── third_party/        <- third party code
 │   ├── distogram/ 
 │   ├── fuzzy/   
 │   └── ...  
 ├── utils/              <- helper libraries
 └── ...       
src/                     <- Rust libraries
testdata/                <- Data referenced in unit tests
tests/                   <- Unit tests
~~~

