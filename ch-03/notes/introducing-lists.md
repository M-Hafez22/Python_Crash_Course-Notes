# Introducing Lists

- [What Is a List?](#what-is-a-list?)
- [How to create a List?](#how-to-create-a-list?)
- [Accessing Elements in a List](#accessing-elements-in-a-list)
- [Index Positions Start at 0, Not 1](#index-positions-start-at-0,-not-1)
- [Using Individual Values from a List](#using-individual-values-from-a-list)
- [Changing, Adding, and Removing Elements](#changing,-adding,-and-removing-elements)
- [Organizing a List](#organizing-a-list)
- [Avoiding Index Errors When Working with Lists](#avoiding-index-errors-when-working-with-lists)

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

### Removing Elements from a List

#### Removing an Item by Index

- **Removing an Item Using the del Statement**
  If you know the **Index** of the item you want to remove from a list, you can use the `del` statement.

  ```py
  motorcycles = ['honda', 'yamaha', 'suzuki']
  print(motorcycles) # ['honda', 'yamaha', 'suzuki']
  del motorcycles[0]
  print(motorcycles) # ['yamaha', 'suzuki']
  ```
  
  > you can no longer access the value that was removed by `del` statement.

- **Removing an Item Using the `pop()` Method**
  - The `pop()` method *removes the last item* in a list, but it lets you *work with that item after removing* it.
  - It manages you:
    1. to **delete** the last element from the list
    and
    2. **assign** it to a variable

    ```py
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles) # ['honda', 'yamaha', 'suzuki']
    popped_motorcycle = motorcycles.pop()
    print(motorcycles)  # ['honda', 'yamaha']
    print(popped_motorcycle) # suzuki
    ```

- **Popping Items from any Position in a List**
  You can use `pop()` to remove an item in a list by including the index of the item in the parentheses.

  ```py
  motorcycles = ['honda', 'yamaha', 'suzuki']
  first_owned = motorcycles.pop(1)
  print('The first motorcycle I owned was a ' + first_owned.title() + '.') # The first motorcycle I owned was a Yamaha.
  ```

#### Removing an Item by Value

- To remove an element by its value use `remove()`

```py
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('yamaha')
print(motorcycles) # ['honda', 'suzuki', 'ducati']
```

```py
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)  # ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles) # ['honda', 'yamaha', 'suzuki']
print("\nA " + too_expensive.title() + " is too expensive for me.")  # A Ducati is too expensive for me.
```

> The remove() method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to determine if all occurrences of the value have been removed.

## Organizing a List

### Sorting a List Permanently with the `sort()` Method

The `sort()` method sorts the elements in the list alphabetically.

```py
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # ['audi', 'bmw', 'subaru', 'toyota']
```

### Sorting a List Temporarily with the `sorted()` Function

- The `sorted()` function lets you display your list in a particular order but doesn’t affect the actual order of the list.

```py
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
```

> Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase. There are several ways to interpret capital letters when you’re deciding on a sort order, and specifying the exact order can be more complex than we want to deal with at this time. However, most approaches to sorting will build directly on what you learned in this section.

### Printing a List in Reverse Order

- To reverse the original order of a list, you can use the `reverse()` method.
- Notice that `reverse()` *doesn’t sort backward alphabetically*; it simply **reverses the order of the list**.

```py
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) # ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)  # ['subaru', 'toyota', 'audi', 'bmw']
```

### Finding the Length of a List

```py
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars)) # 4
```

> Python counts the items in a list starting with one, so you shouldn’t run into any off-by-one errors when determining the length of a list.

## Avoiding Index Errors When Working with Lists

- An index error means Python can’t figure out the index you requested.

> If an index error occurs and you can’t figure out how to resolve it, try printing your list or just printing the length of your list. Your list might look much different than you thought it did, especially if it has been managed dynamically by your program. Seeing the actual list, or the exact number of items in your list, can help you sort out such logical errors.
