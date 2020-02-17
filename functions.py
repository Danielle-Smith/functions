def full_name(first, last):
  print(f'{first} {last}') # 2 lines space after function is good practice


full_name('Kristine', 'Hudgens')

def auth(email, password):
  if email == 'kristine@hudgens.com' and password == 'secret':
    print('You are authorized')
  else:
    print('You are not authorized')


auth('kristine@hudgens.com', 'asdf')

def hundred():
  for num in range(1, 101):
    print(num)


hundred()

def counter(max_value):
  for num in range(1, max_value):
    print(num)


counter(501)

# Return a value from a python function

def full_name(first, last):
  return f'{first} {last}' # return saves it for future use and print just prints in the terminal for debugging and doesn't save


kristine = full_name('Kristine', 'Hudgens')# input

def greeting(name): # function calling the previous function and the input
  print(f'Hi {name}!')


greeting(kristine)

# Nesting functions in functions

def greeting(first, last):
  def full_name():
    return f'{first} {last}'

  print(f'Hi {full_name()}!')


greeting('Kristine', 'Hudgens')

# When to nest functions and when to separate

# if you never need to call this full_name function except in the context of greeting so greeting is the only function that calls the values here. Then there is no reason for this full_name function to be in a different part of the application you can nested inside and then call it whenever you need to.
# However, if some other part of the program does need access to the full name function then you may want to keep it separate and call them independent of each other. That's my personal rule of thumb when it comes to choosing when and when not to nest functions in Python.


#Guide to default arguments in python

def greeting(name = 'Guest'):
  print(f'Hi {name}!')

greeting()
greeting('Kristine')

# Nope
def some_function(collection = []): # It is bad practice to set a default argument as a list. It saves the info.
  collection.append(1)
  print(id(collection))
  return collection


print(some_function())
print(some_function())

# named function arguments

def full_name(first, last): 
  print(f'{first} {last}')


full_name('Kristine', 'Hudgens')
full_name(first = 'Kristine', last = 'Hudgens')
full_name(last = 'Hudgens', first = 'Kristine')

# function argument unpacking
# when unpacking *args you get a tuple when you unpack **kwargs (key word argument) you get a dictionary.
def greeting(*args): # * for taking in arguments when you don't know how many there will be. *args is python good practice.
  print('Hi ' + ' '.join(args)) # .join will combine into a list


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')


def greeting(*names):
  print('Hi ' + ' '.join(names))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')


def greeting(time_of_day, *args):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
greeting('Morning', 'Tiffany', 'Hudgens')


# keyword arguments
def greeting(**kwargs): #**kwargs (key word argument) you get a dictionary. *args you get a tuple when you unpack
  print(kwargs)


greeting()
greeting(first = 'Kristine', last = 'Hudgens')

def greeting(**kwargs):
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!") # order matters here
  else:
    print('Hi Guest!')


greeting()
greeting(first = 'Kristine', last = 'Hudgens') # order doesn't matter because the order is defined in the print function

# combined all argument types in a function
def greeting(time_of_day, *args, **kwargs):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}.") # Hi ('Danielle', 'Smith') is what you get if you don't do the .join()

  if kwargs:
    print('Your tasks for the day are:')
    for key, val in kwargs.items():
      print(f'{key} -> {val}')


greeting('Morning',
         'Kristine', 'Hudgens',
         first = 'Empty dishwasher',
         second = 'Take pupper out',
         third = 'math homework')


# lambda - Lambda gives you the ability to quickly and easily wrap functionality, store it in a variable and then pass that entire process to other functions and other parts of your program
full_name = lambda first, last: f'{first} {last}' # you can add as many variables as you want


def greeting(name):
  print(f'Hi there {name}')


greeting(full_name('Kristine', 'Hudgens'))