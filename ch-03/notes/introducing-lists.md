# Introducing Lists

- [What Is a List?](#what-is-a-list?)
- [How to create a List?](#how-to-create-a-list?)

## What Is a List?

- A **list** is a collection of items in a particular order.

## How to create a List?

- To create a **List** write the elements between a square brackets ([]) separated by commas (,)

```py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) # ['trek', 'cannondale', 'redline', 'specialized']
```

## Accessing Elements in a List

- To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.

```py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# Access the element by the Index
print(bicycles[0]) # trek
# Or a variable holds the Index
position = 2
print(bicycles[position]) # redline
```

## Index Positions Start at 0, Not 1

- In Python
  - The **First element** index is **0**.
  - The **First element** index is **-1**.
  - The second item from the end of the list index is **-2**.

```py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0]) # trek
print(bicycles[-1]) # specialized

```

## Using Individual Values from a List

- You can use individual values from a list just as you would any other variable.

```py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
```

## Changing, Adding, and Removing Elements

- Lists are **dynamic**. You can add and remove elements from it.

### Modifying Elements in a List

- To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.

```py
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']
# Change the value of the first element in the list
motorcycles[0] = 'ducati'
print(motorcycles) # ['ducati', 'yamaha', 'suzuki']
```

### Adding Elements to a List

- **Appending Elements to the End of a List**
  
  ```py
  motorcycles = ['honda', 'yamaha', 'suzuki']
  print(motorcycles) # ['honda', 'yamaha', 'suzuki']
  motorcycles.append('ducati')
  print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'ducati']
  ```

  > The ```append()``` method lets you to start with an empty list and then add items to it.

- **Inserting Elements into a List**
  You can add a new element at any position in your list by using the ```insert()``` method.

  You do this by **specifying the index of the new element and the value** of the new item.

  ```py
  motorcycles = ['honda', 'yamaha', 'suzuki']
  motorcycles.insert(0, 'ducati')
  print(motorcycles) # ['ducati', 'honda', 'yamaha', 'suzuki']
  # This operation shifts every other value in the list one position to the right
  ```
