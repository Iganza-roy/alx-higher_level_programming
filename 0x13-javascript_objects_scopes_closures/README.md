# JavaScript - Objects, Scopes and Closures

![logo](https://www.tabnine.com/academy/wp-content/uploads/2020/10/academy_3.png)

This repo contains my tasks on JavaSriptc - Objects, scopes and closures project.
Every code written here follows the [semi standard](https://github.com/standard/semistandard) style for coding:
![standard](https://raw.githubusercontent.com/standard/semistandard/master/badge.svg) 

An **object** is a collection of related data and/or functionality. These usually consist of several variables and functions (which are called properties and methods when they are inside objects). 

**Scope** refers to the visibility and accessibility of variables, functions, and objects in different parts of your code during runtime. It determines which variables are accessible from where in your code and how those variables are resolved when they are referenced.
JavaScript has two main types of scope:
 - Global scope: (Variables declared outside of any function or block have global)
 - local scope: (Variables declared within a function or block have local scope.)

**A closure** is a combination of a function and the lexical environment within which that function was declared. It allows a function to access and manipulate variables from its outer scope, even after the outer function has finished executing.
# Example:

```
function outer() {
    let counter = 0;
    return function inner() {
        counter++;
        console.log(counter);
    };
}
const increment = outer();
increment(); // Output: 1
increment(); // Output: 2
```
