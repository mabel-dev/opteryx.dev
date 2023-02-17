# Project Structure

## Folder Structure

Opteryx's repository folder structure is described below:

~~~
opteryx/                 <- main opteryx library
 ├── components/         <- the planning and management of the query engine
 ├── connectors/         <- modules to connect to data sources
 ├── functions/          <- modules to execute functions within SQL statements
 ├── managers/           <- libraries responsible for key functional units
 │   ├── cache/          <- modules implementing caching systems
 │   ├── expression/     <- modules implementing expression evaluation
 │   ├── kvstore/        <- modules implementing interfacing with KV Stores
 │   └── schemes/        <- modules implementing storage schemes
 ├── models/             <- internal data models
 ├── operators/          <- modules implementing steps in the query plan
 ├── samples/            <- sample data ($planets, $astronauts, $satellites)
 ├── shared/             <- global resources
 ├── third_party/        <- third party code
 │   ├── distogram/ 
 │   ├── fuzzy/   
 │   ├── pyarrow_ops/ 
 │   └── ...  
 ├── utils/              <- helper libraries
 └── ...       
src/                     <- Rust libraries
testdata/                <- Data referenced in unit tests
tests/                   <- Unit tests
~~~

