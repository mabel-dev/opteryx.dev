# Lessons Learnt So Far

_9th December 2022_

We never thought building a SQL Engine from scratch was going to be easy, and we expected some hard learnings.


**The conventions in SQL Engines generally make good sense, follow them**

If most SQL Engines work a particular way, chances are they've done that because they've probably 




**Unit testing is fine, but write hundreds of tests cases which run real SQL queries**

Testing individual components in isolation is important, and for some components the only real way to get assurance that it works as expected; but we find that writing SQL queries to exercise the entire stack usually, test-per-test, provides more value on average.

The key finding is that a SQL Engine is complex, where a minor change in one component can have an unexpected impact on another.

**Have real systems and real users as your beta testers**

If you want real users to be able to use your system, make sure you have real users on your system early. This can be problematic, especially if you can't guarantee the accuracy of the engine and perforance is likely to be pretty poor.

**You can't fabricate test data for all your test scenarios**

You will never write tests that cover the variation of real-world data.



**Storage read speed will kill any performance boosts from algorithmic improvements**


**If you don't control of the the thing writing of the data - assume the worst**




**Bonus Point: PyArrow is awesome, but it has bugs, odd limitations and some parts are so slow it hurts**

bugs
- date diff just doesn't work for months

odd limitations
- can't join on tables with arrays or structs

so slow it hurts
- Abstraction == Slow, if you want fast, you need to get as close to the bare metal or raw API as possible