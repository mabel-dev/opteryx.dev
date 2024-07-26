~~~mermaid
flowchart TD

    subgraph  
        subgraph Z[" "]
            USER
        end
        EXE --> |Results| USER
        USER  --> |SQL| SQLRE(SQL Rewriter)
        PHYPL --> |Plan| EXE(Executor)
        SQLRE --> |SQL| PARSER(Parser)
        PARSER --> |AST| ASTRE(AST Rewriter)
        ASTRE --> |AST| LOGPL(Logical Planner)
        LOGPL --> |Plan| BINDER(Binder)
        OPT --> |Plan| PHYPL(Physical Planner)
        CATALOG[(Catalog)] --> |Schemas| BINDER
        CATALOG --> |Stats| OPT(Optimizer)
        CATALOG --> |Manifests| EXE
        BINDER --> |Plan| OPT

    end
~~~