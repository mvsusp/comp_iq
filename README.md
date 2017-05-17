# Objective
The objective of this exercise is to assess your problem solving ability and your development skill. We'll not only be looking for the logically correct solution but also for a solution that is...

- clean
- terse
- well-written
- well-documented

# Instructions
- The preferred language for this exercise is Python but if you are significantly more comfortable in another language, that is OK.
- Submit the exercise as a ZIP file by email.

# Format of Solution
In your solution, add a README.md file which should contain description of your solution and the answers to all the questions.

Other than that, follow whatever code format you like for the solution.

# How Long Should This Take?
Based on our experience, this should take less than 2 hours.

# Data
There are two CSV files.

- `user-compensation-records.csv` contains the base and bonus records for all of the users in our sample dataset (https://s3.amazonaws.com/compiq-engineering/user-compensation-records.csv)
- `firms.csv` contains the list of firms along with their `compiq_index` (https://s3.amazonaws.com/compiq-engineering/firms.csv)

# Definitions
- base: the base salary
- bonus: annual bonus
- title: the role that the candidate performs at their company, e.g. Senior Analyst

# Formulas
```python
import math

def are_similar(firm_1, firm_2):
    return math.fabs(firm_1["compiq_index"] - firm_2["compiq_index"]) < 0.15
```


# Questions
1. Write code that according to the following:

## Input
A dictionary `User`, which should contain the following info:

- title
- firm_id
- user_id

e.g. {"user_id": 889, "firm_id": 2, "title": "Analyst"}

## Logic
Compute the percentile the user's base and bonus are at compared to the base and bonus records for *this user's title* across all "similar" firms as well as other users' records from this user's same firm, but not including the user's own record.


## Output
The output should be as follows:
```
{
    "user_id": # user's id.
    "user_base": # user's base,
    "user_bonus": # user's bonus,
    "percentile_base": # nth percentile of user's base,
    "percentile_bonus": # nth percentile of user's bonus
}
```

2. What is the result for user with id = 889? (Check the user-compensation-records.csv file to get the corresponding `firm_id` and `title`)
