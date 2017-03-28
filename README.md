# Clean Answers over Dirty Databases: A Probabilistic Approach
## Course Code: CS702	<br/>
## Course Project: Distributed Database Management System	<br/>

### Overview		<br/>
Authors propose a complementary approach that permits declarative query answering over duplicated data, where each duplicate is associated with a probability of being in the clean database. This repository contains the simulation of author work[1] using python[2] script in which they rewrite queries over a database containing duplicates to return each answer with the probability that the answer is in the clean database.

### Reference Dataset
Synthetic Data Generator, UIS Database Generator and Cora Dataset

### Simulating Simulator	<br/>

Simulator script should be executed as

```python
./python simulator.py
```

### Simulator Command Format

```sql
Select Attribute1,Attribute2,...,AttributeN 
   from Table1,Table2 
      where condition1,condition2..,conditionN 
         groupBy Attribute1,...AttributeN
```
### Query Re-Writing Example
Dataset Snippet of Customer Table

id | custId | name | balance | prob |
--- | --- | --- | --- | --- |
c1 | m1 | John | 20 | 0.7 |
c1 | m2 | John | 30 | 0.3 | 
c2 | m3 | Mary | 27 | 0.2 | 
c2 | m4 | Marion | 5 | 0.8 | 

Normal SQL query to fetch id of those customers having balance > 10<br/>

```sql
select id,prob
   from customer
      where balance>10
```
id | prob |
--- | --- |
c1 | 0.7 |
c1 | 0.3 |
c2 | 0.2 |

But if we apply clean answers over Dirty Database using Probabilistic Database
```sql
select id,sum(prob)
   from customer
      where balance>10
        groupby id
```
id | prob |
--- | --- |
c1 | 0.1 |
c2 | 0.2 |

### Enhancement
<p align="center">
   <img src="https://drive.google.com/file/d/0B5nKw4aBVyAdWk9qNXFxVk5MMXM/view?usp=sharing" width="350" />
</p>
### References         <br/>

[1] P. Andritsos, A. Fuxman, R.J. Miller, "Clean Answers over Dirty Databases: A Probabilistic Approach", Proceedings of the 22nd International Conference on Data Engineering, 2006.

[2] https://github.com/mysql/mysql-server
