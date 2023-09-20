# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping)
   and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL.
   Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

_Edit your responses here_
The naming of functions and member functions is crucial for code clarity. For instance, 'pop' accurately removes an element, but it could be clearer if it were named 'popAndGet' or 'popAndReturn' when both removal and returning the value occur. Descriptive and action-oriented function names enhance code readability and maintainability.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

_Edit your response here_
A dictionary differs from a list in its underlying data structure. A dictionary uses a key-value pair mapping, associating unique keys with corresponding values. In contrast, a list employs a sequential, ordered collection of elements without key-value associations.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

_Edit your response here_
Yes, lists allow random access, you can access any element in the list by index, e.g. myList[7], myList[0].

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.).
   What do you think are the pros/cons of a library that can work with any data type?

_Edit your response here_
A library that can handle any data type offers flexibility, allowing developers to work with various data, from numbers to custom types. This versatility supports code reuse and accommodates diverse scenarios. However, it may risk type-related errors, especially in statically typed languages, and could introduce performance overhead due to type checks and conversions. Additionally, managing multiple data types within one container can make the code more complex. Deciding to use such a library should consider the trade-off between flexibility and the need for clear, safe, and efficient code.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
   Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

_Edit your responses here_
The functions in the Requests module are well-named. They follow a clear and intuitive naming convention, making it easy to understand their purpose and usage from the documentation.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

_Edit your responses here_
For example, the prepare method in the Requests class seems to have a large number of parameters. While it's not uncommon for lower-level functions to accept multiple arguments, having a large number of arguments can make a function more complex and error-prone to use, especially when the user needs to provide values for many of those arguments. In this case, careful documentation and clear usage examples are crucial to reducing confusion and errors.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?

_Edit your responses here_
**kwargs is a keyword in Python used to pass a variable-length list of keyword arguments to a function. It can be beneficial for a method to have a **kwargs argument because it allows for flexibility and extensibility, enabling users to pass additional named parameters without modifying the method's signature. However, it can be challenging for code maintainability, as it makes it less explicit which arguments are accepted and might lead to unexpected behavior if not used carefully.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text.
   Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

_Edit your responses here_
In the Session class, some methods have arguments with None as default values, while others lack defaults. This flexibility lets users specify values or rely on None as a default. Varying argument values align with method behavior. Predetermined values simplify usage and increase predictability.
