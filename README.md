# Clean Answers over Dirty Databases: A Probabilistic Approach
## Course Code: CS702	<br/>
## Course Project: Distributed Database Management System	<br/>

### Overview		<br/>
Authors propose a complementary approach that permits declarative query answering over duplicated data, where each duplicate is associated with a probability of being in the clean database. This repository contains the simulation of author work[1] using python[2] script in which they rewrite queries over a database containing duplicates to return each answer with the probability that the answer is in the clean database.

### Refernce Dataset
Cora Dataset

### Simulating Simulator	<br/>

Simulator script should be executed as

`./python simulator.py`

### Simulator SQL Command Format

`Select Attribute1,Attribute2,...,AttributeN from Table1,Table2 where condition1,condition2..,conditionN groupBy Attribute1,...AttributeN`

### References         <br/>

[1] P. Andritsos, A. Fuxman, R.J. Miller, "Clean Answers over Dirty Databases: A Probabilistic Approach", Proceedings of the 22nd International Conference on Data Engineering, 2006.

[2] https://github.com/mysql/mysql-server
