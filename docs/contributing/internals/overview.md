~~~mermaid
flowchart TD

    USER[User]
    SQLRE[SQL Rewriter]
    PARSER[Parser & Lexer]
    ASTRE[AST Rewriter]
    LOGPL[Logical Planner]
    BINDER[Binder]
    OPT[Optimizer]
    PHYPL[Physical Planner]
    EXE[Executor]
    CATALOG[(Catalog)]

    USER -->|SQL Query| SQLRE
    SQLRE -->|Rewritten SQL| PARSER
    PARSER -->|AST| ASTRE
    ASTRE -->|Rewritten AST| LOGPL
    LOGPL -->|Logical Plan| BINDER
    BINDER -->|Bound Plan| OPT
    OPT -->|Optimized Plan| PHYPL
    PHYPL -->|Physical Plan| EXE
    EXE -->|Results| USER
    
    CATALOG -->|Schemas| BINDER
    CATALOG -->|Statistics| OPT
    CATALOG -->|Manifests| EXE
~~~