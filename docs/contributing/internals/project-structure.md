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
 │   ├── planner/        <- modules implementing query planning and optimizing
 │   └── schemes/        <- modules implementing storage schemes
 ├── models/             <- internal data models
 ├── operators/          <- modules implementing steps in the query plan
 ├── samples/            <- sample data
 ├── shared/             <- global resources
 ├── third_party/        <- third party code
 │   ├── distogram/ 
 │   ├── fuzzy/   
 │   ├── hyperloglog/  
 │   ├── pyarrow_ops/ 
 │   └── ...  
 ├── utils/              <- helper libraries
 └── ...       
~~~

