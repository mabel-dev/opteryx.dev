# Project Structure

## Folder Structure

Opteryx's repository folder structure is described below:

~~~
opteryx/                 <- main opteryx library
 ├── compiled/           <- cython-compiled modules for performance
 ├── connectors/         <- modules to connect to data sources
 ├── constants/          <- constant definitions used across the codebase
 ├── datatypes/          <- data type definitions and handling
 ├── functions/          <- modules to execute functions within SQL statements
 ├── managers/           <- libraries responsible for key functional units
 │   ├── cache/          <- modules implementing caching systems
 │   ├── execution/      <- query execution management
 │   ├── expression/     <- modules implementing expression evaluation
 │   ├── kvstores/       <- modules implementing interfacing with KV Stores
 │   ├── permissions/    <- permission and access control management
 │   └── schemes/        <- modules implementing storage schemes
 ├── models/             <- internal data models
 ├── operators/          <- modules implementing steps in the query plan
 ├── planner/            <- the planning and management of the query engine
 │   ├── binder/         <- binds identifiers to schemas and resolves references
 │   ├── logical_planner/ <- creates logical query plans from AST
 │   ├── optimizer/      <- optimizes query plans for performance
 │   └── views/          <- view management
 ├── shared/             <- global resources
 ├── third_party/        <- third party code
 │   ├── abseil/ 
 │   ├── alantsd/
 │   ├── cyan4973/
 │   ├── fastfloat/
 │   ├── maki_nage/
 │   ├── query_builder/
 │   ├── sqloxide/
 │   ├── tktech/
 │   ├── travers/
 │   ├── ulfjack/
 │   └── ...  
 ├── utils/              <- helper libraries
 ├── virtual_datasets/   <- sample data (e.g. $planets, $astronauts, $satellites)
 └── ...       
src/                     <- Rust libraries
testdata/                <- Data referenced in unit tests
tests/                   <- Unit tests
~~~

