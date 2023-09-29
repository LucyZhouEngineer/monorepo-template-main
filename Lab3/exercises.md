# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!

## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:

   - _edit your response_ MObject is a concrete class. Abstract classes usually contain at least one abstract method and are defined using the abc module, but MObject has no such method and does not use the abc module.

2. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?

   - _edit your response_ **del** is a destructor, which is called when the object is destroyed. But in this class, the code for the **del** method is commented out, so it doesn't actually do anything. If uncommented and implemented, it will be executed at the end of the object's lifetime.

3. What class does Texture inherit from?

   - _edit your response_ The Texture class inherits from the Image class.

4. What methods and attributes does the Texture class inherit from 'Image'?

   - _edit your response_ The Texture class inherits all methods and attributes of the Image class since it's a subclass of Image. This includes the **init**, getWidth, getHeight, getPixelColorR, getPixels, setPixelsToRandomValue methods, and the attributes m_width, m_height, m_colorChannels, and m_Pixels.

5. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!

   - _edit your response_ This depends on the context. If a texture is conceptually a type of image, then 'is-a' (inheritance) is appropriate. However, if a texture simply utilizes an image as part of its representation but has other properties and behaviors that make it distinct from a regular image, then a 'has-a' (composition) relationship might be more appropriate. If going with composition, the Texture class might contain an instance of Image as an attribute rather than inheriting from it.

6. I did not declare a constructor for Texture. Does Python automatically create constructors for us?
   - _edit your response_ Yes, if a class doesn't provide a constructor, it inherits the constructor of its parent class. In the case of Texture, since it doesn't define its own **init** method, it inherits the **init** method of the Image class. If Texture didn't have a parent class with a defined constructor, it would default to the base object's constructor.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:

- The first time the logger is constructed, it will print out:
  - `Logger created exactly once`
- If the logger is already initialized, it will print: - `logger already created`
  Note: You do not 'have' a constructor, but you construct the object in the _instance_ member function where you will create an object.  
  Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?
   _edit the code directly_ Singletons in the way we've implemented above are not inherently thread-safe. If multiple threads try to create an instance of the Logger class at the same time (before \_instance is set), it's possible that two separate instances get created. To make the Singleton pattern thread-safe, we would typically use thread locking mechanisms to ensure that only one thread can create the instance at a time.
