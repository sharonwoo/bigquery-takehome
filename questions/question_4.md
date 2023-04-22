# Question 4

> In your own words (short paragraphs conveying your thoughts), answer the following questions:

> a. What is refactoring? When and why should you refactor?

> b. What is testing? When and why should you write test cases?

## What is refactoring? When and why should you refactor?

### What is refactoring? 
Refactoring in a software context refers to any re-write of code which does not change how the system this code is part of behaves and/or is intended to behave. 

Below is a simple example...

```
c = 'hello world'
print(c)

# output: > 'hello world'
```
...where changing the name of a variable improves readability with an identical output: 

```
printed_message = 'hello world'
print(printed_message)

# output: > 'hello world'
```

This may not seem important now as the two lines are next to each other, but if I am trying to trace what `printed_message` does about 2,000 lines of code and 6 months later, I will probably be slightly more sane thanks to the action of past me than if I had to call `c`. More on this shortly. 

I had fun looking at these examples while writing this: [disasters](https://github.com/sobolevn/python-code-disasters/tree/master)

### Why is refactoring even needed? 
Typically, refactoring aims to make life easier by saving time, money, or both by: 
* making code easier to read and maintain in the future, in the worst case even ensuring it can be maintained going forward
* reducing the amount of resources that is needed to run and secure a given service / application, therefore bringing down overall costs over time 

Some personal experiences: 
* External pressures like deadlines, leading to choices in software design and implementation that may take less time to implement now, but will eventually require compounded amounts of time to fix in the future - "technical debt"
* External pressures - e.g. management drive to cut costs or customer complaints about latency (due to growth beyond an intended service maximum, or a poor product experience, etc) 
* Changes to a critical dependency - e.g. the deprecation of Python 2 and cessation of support of it on AWS Lambda in 2020-21 forced migration of these workloads to Python 3
* The implementation of a new feature necessitating a rewrite - e.g. the Github Actions of this repository changing to check only the `questions` folder, when I added tests written in Python that also triggered writing tables to staging
* Sheer inexperience 

The classic essay [Big Ball of Mud](http://www.laputan.org/mud/), if you can get to the end without despairing, often gets brought up in software communities because it lists down many of the reasons why refactoring needs to happen. To summarise, brought to an extreme, a lack of care can lead to code declining "to the point where it is beyond repair, or even comprehension" which then makes it easier to burn it down and completely rebuild it from the ground up. 

### When and why should you refactor? 

![https://giphy.com/gifs/rebekah-mad-eye-moody-fGRLXXhta9eGtWAyvn](/images/moody.gif)
 
In general, refactoring is like showering and should be done on a regular basis in order to maintain the mental health of everyone who works around it. 

The below is not exhaustive but I think sums many of my own personal experiences up: 

| When to refactor | Why refactor    |
| ---              | ---             |
| Code review feedback identifies issues | To address issues with code and standardise coding practices across a system/company. |
| Technical debt and/or poor coding practices | To make code easier to understand and maintain. |
| Performance issues | To improve the efficiency and speed of the system, and/or to lower its running and maintenance costs. |
| Implementing new features | To make the code base more extensible or to reduce complexity, making it easier to add new functionality in the future. |
| Deprecation of critical dependencies | To ensure ongoing functionality of the system. |

## What is testing? When and why should you write test cases?

### What is testing? 

In layman's terms, testing is making sure you get what you expect. 

Testing in a software context refers to creating checks that the software system/service/component does what its requirements state it should do. Common types of tests in this context: 

| Test type | What the test does |
| ---       | --- |
| Unit test | Test to check that atomic parts of software work as intended, e.g. a function to print a statement prints a statement. Can usually be automated easily. |
| Integration test | Test to check that parts of a system work together as intended, e.g. Amazon's More Like This shows a carousell with a minimum number of products. |
| Performance test | Test to check that the system works under specific conditions, e.g. Shopee's 11:11 not crashing the site. |
| User acceptance test | Test to check that the system meets the business requirements and is ready for business stakeholders to sign off. |

### When and why should you write test cases?

Always and even before the start, because it's fun?

I personally find that having a comprehensive test suite also serves to make sure that requirements are properly gathered and expressed. 

![govtech tdd coding dojo - that's me as an instructor](/images/govtech27may-codingdojo.jpg)

More seriously, integrating testing into development aka **test-driven development** helps to ensure that whatever is in development works as expected before it is deployed into production. 

Also, the tests for this take home were easy to write because the requirements were clearly stated in terms of expected results for the tables created in questions 1-3. 