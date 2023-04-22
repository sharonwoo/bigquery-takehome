# Question 4

> In your own words (short paragraphs conveying your thoughts), answer the following questions:

> a. What is refactoring? When and why should you refactor?

> b. What is testing? When and why should you write test cases?

## On Refactoring

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

### Why is refactoring even needed? 
Typically, refactoring aims to make life easier by saving time, money, or both by: 
* making code easier to read and maintain in the future, in the worst case even ensuring it can be maintained going forward
* reducing the amount of resources that is needed to run and secure a given service / application, therefore bringing down overall costs over time 

The broadest need for refactoring is often driven by trade offs, such as
* External pressures like deadlines, leading to choices in software design and implementation that may take less time to implement now, but will eventually require compounded amounts of time to fix in the future - "technical debt"
* External pressures - e.g. management drive to cut costs or customer complaints about latency (due to growth beyond an intended service maximum, or a poor product experience, etc) 
* Changes to a critical dependency - e.g. the deprecation of Python 2 and cessation of support of it on AWS Lambda in 2020-21 forced migration of these workloads to Python 3
* The implementation of new product features impacting existing systems - e.g. 
* Sheer inexperience 

The classic essay [Big Ball of Mud](http://www.laputan.org/mud/), if you can get to the end without despairing, often gets brought up in software communities because it lists down many of the reasons why refactoring needs to happen. To summarise, brought to an extreme, a lack of care can lead to code declining "to the point where it is beyond repair, or even comprehension" which then makes it easier to burn it down and completely rebuild it from the ground up. 

### When and why should you refactor? 

![https://giphy.com/gifs/rebekah-mad-eye-moody-fGRLXXhta9eGtWAyvn](/images/moody.gif)
 
In general, refactoring is like showering and should be done on a regular basis in order to maintain the mental health of everyone who works around it. 

The most common scenario for refactoring involves code reviews and feedback on how to improve the quality of the code. 

The below is not exhaustive but I think sums many of my own personal experiences up: 

| When to refactor | Why refactor    |
| ---              | ---             |
| Code review feedback identifies issues | To address issues with code and standardis coding practices across a system/company. |
| Technical debt and/or poor coding practices | To make code easier to understand and maintain. |
| Performance issues | To improve the efficiency and speed of the system, and/or to lower its running and maintenance costs. |
| Implementing new features | To make the code base more extensible or to reduce complexity, making it easier to add new functionality in the future. |
| Deprecation of critical dependencies | To ensure ongoing functionality of the system. |
