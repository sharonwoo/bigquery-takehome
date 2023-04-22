# Question 4

> In your own words (short paragraphs conveying your thoughts), answer the following questions:
>  a. What is refactoring? When and why should you refactor?
> b. What is testing? When and why should you write test cases?

## On Refactoring

### What is refactoring? 
Refactoring in a software context refers to any re-write of code which does not change how it behaves and/or is intended to behave. 

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

This may not seem important now as the two lines are next to each other, but we'll get to that shortly.

### Why is refactoring even needed? 
Typically, refactoring aims to make life easier by saving time, money, or both by: 
* making code easier to read and maintain
* reducing the amount of resources that is needed to run and secure a given service / application, therefore bringing down overall costs over time 

There is a classic essay - [Big Ball of Mud](http://www.laputan.org/mud/) that frequently gets brought up in software communities, often paired with suggestions of whiskey to wash down. 

If you can get to the end without despairing, it lists down many of the reasons why refactoring is needed. This is often due to external pressures like deadlines and/or lack of experience, leading to choices in software design and implementation that may take less time to implement now, but will eventually require compounded amounts of time to fix in the future - "technical debt". 

### When and why should you refactor? 

![https://giphy.com/gifs/rebekah-mad-eye-moody-fGRLXXhta9eGtWAyvn](/images/moody.gif)

