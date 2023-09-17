# Preparing for Opteryx v0.12: A Sneak Peek into Our Revamped Query Planner and More

As we gear up for the next release of Opteryx version 0.12, which has been a few months coming, we're thrilled to offer a sneak peek into some of the groundbreaking changes coming your way. While the journey of crafting a query engine has always been an ambitious endeavor, the upcoming version promises to take it to the next level.

## The Query Planner: A Complete Overhaul

The most significant update in v0.12 is a complete rewrite of the query planner. This rewrite aims to retain existing functionalities and maintain API consistency, but it also paves the way for new and exciting optimizations.

Not all features will be immediately available in v0.12, these should be less well-trodden features such as filters on `SHOW` queries and `IN` subquery. The goal is to restore anything missing by v0.14.

## Optimizer: New Capabilities on the Horizon

v0.13 will likely be a stability release, where limited new features are added, but rather the focus will be on edge cases and documentation. v0.14 will likely see the reintroduction of a query optimizer:

**Advanced Projection and Predicate Pushing**: Not just limited to single-table queries anymore.   
**Cost-based Expression Evaluation**: In the pipeline, contingent upon a rewritten function catalogue.   
**Join Order Optimization**: In planning, and dependent on new data profiles.   
**Pushing Group By, Sort, and Limits**: More freedom to offload these tasks to the database sources.   

## Overcoming Soft Challenges: The Human Aspect

We've had our share of ups and downs, from struggling to maintain motivation amidst a sea of failed unit tests to wrestling with focus when other exciting parts of the project catch our attention. Despite these hurdles, we've managed to turn challenges into stepping stones.

## What's on the Horizon: The Push-Based Execution Engine

The rewrite of the planning phases is a strategic move to facilitate our transition to a push-based execution engine that incorporates parallel execution, aiming to further accelerate query performance.

The inclusion of the binder into the planning phase has shifted a significant amount of logic out of the execution phase. Making the execution phase stateless is a precursor to parallelizing these activities, which is the long-term goal.

## Our New Team Member: ChatGPT

We have been using ChatGPT in diverse roles:

**Code Reviewer**: Analyzing and offering improvements for code.   
**Test Analyst**: Assisting in creating robust unit tests.   
**Senior Developer**: Identifying performance bottlenecks and providing solutions.   
**Technical Writer**: Writing docstrings and contributing to technical documentation.   

While ChatGPT has had a variable performance and sometimes has not been as helpful as the hype will have you believe, its contributions have been invaluable.

## Stay Tuned for the Full Release

We're putting the finishing touches on v0.12 and look forward to sharing the full details with you in the coming weeks. We're incredibly excited about what's ahead and hope you are too.

As always, we appreciate your support and welcome any questions or feedback. Keep an eye out for the full release details coming soon!