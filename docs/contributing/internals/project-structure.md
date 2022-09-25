# Project Structure

## Folder Structure

Opteryx's repository folder structure is described below:

~~~
opteryx/                 <- main opteryx library
 ├── connectors/         <- modules to connect to data sources
 ├── functions/          <- modules to execute functions within SQL statements
 ├── managers/           <- libraries responsible for key functional units
 │   ├── expression/     <- modules implementing expression evaluation
 │   ├── kvstore/        <- modules implementing interfacing with KV Stores
 │   ├── process/        <- modules implementing process management
 │   ├── query/          <- modules implementing query planning 
 │   └── schemes/        <- modules implementing storage schemes
 ├── models/             <- internal data models
 ├── operators/          <- modules implementing steps in the query plan
 ├── samples/            <- sample data
 ├── third_party/        <- third party code
 │   ├── distogram/ 
 │   ├── fuzzy/   
 │   ├── hyperloglog/  
 │   ├── pyarrow_ops/ 
 │   └── ...  
 ├── utils/              <- helper libraries
 └── ...       
raptor/                  <- query optimizer
~~~

