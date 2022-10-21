## What is Flask?
Flask is web application mini framework written in python. Its a micro-framwork in that it does not include feature like [ORM](https://stackoverflow.com/questions/1279613/what-is-an-orm-how-does-it-work-and-how-should-i-use-one) (Object Relational Manager) It  however, has alot of other cool features like url routing and template engines. 
## Why Flask
I'm struggling with an opening statement for this subsection so, I'm just gonna jump right in. 
Flask is a very powerful Framework considering what it brings on the table that other Tech stacks don't. 
Alot of big websites like [Netflix](https://netflix.com) uses Flask for their backend infrustructure to serve their API's and more. 
Speaking of cool, the coolest feature I've come across(So far ) is Flash messages. 


## Getting started with Flask 

To get started with flask, you dont really need a trip around the moon and back. The very basic knowledged of Python, HTML and some CSS is all  you need to roll. 

## Making the magic happen
Enough with the talks. So, how do you build your first site in Flask huh? To write your first web App  using the flask framework, fire up your favourite text editor ( I use emacs BTW ) and create a file ending with a ```".py"``` extention.

The first thing we need to do in our file is to import the Flask class from the flask module, at the very first line of our code. 

 ``` from flask import Flask ```

The next thing is to instantiate the Flask class or create an object of the Flask class passing in ```__name__``` an argument. Remember whenever a class is instantiated in python, the  constructor is called (the ```__init__``` method of that class) In this case, Flask's constructor takes one argument. Which is the name of the current module. 


```app = Flask(__name__)```


Here *app* can be any valid variable name, it doesnt have to be named app.

Next, we create a decorator for a route and map a function to it (Trust me, its much simple than it sounds :P ) But before we do that, lets talk briefly about decorators and  mapping.  By definition, decorators  are functions that take other functionds and  extent the behaviour of the latter function without explicitly modifying it.  This sound confusing but its really not, especially after you have seen some examples of how decorators work from this article [Here]("https://github.com/realtpython/materials/primer-on-python-decorators") 

The route on the other hand is just the path that you follow after the website's url. Take for example, a website with the url of *example.xyz* when you visit *example.xyz/here*, *here* in this case it the path, or the route. When the path is not specified, by  definition that is called the index path, or the entry point. On most sites, that is considered the home url. 

To define a path in Flask, you just add a decorator to the object's route call, passing the path as a string and occassionaly the HTTP Methods as a list of strings. Lets see this in an example.

```@app.route("/")```

in the above example, app is the object we initialized earlier in our course and route is a method defined in the Flask class. the forwad slash here indicate the route. ( Assuming our website was *example.xyz*)The full path would have been *example.xyz/* Which is just the index. 

We want to setup our webstie such that when someone visits *example.xyz/*, The website responds with something. This is made possible by wrapping a function the route. 

~~~~
def index():
        return "Hi Mom!" 
~~~~
The last thing to do is to call the run() method on the object we created and the website should be up and running. 

Putting the pieces together, the entire code should look like this


Congratulations you just said __Hi__ to your mom in Flask



~~~

    

~~~