# Dictionaries: Notes

A list finds items by position (`names[0]`). A dictionary finds values by a name, called a **key**.

## Create and read
```python
person = {"name": "Ana", "age": 30}
print(person["name"])   # Ana
print(person["age"])    # 30
```
- Curly braces `{}` hold the dictionary.
- Each entry is `key: value`, separated by commas.
- Look a value up with its key in square brackets.

## Change and add
```python
person["age"] = 31          # change an existing value
person["city"] = "Toronto"  # add a new key
```

## Check, get, delete
```python
"name" in person            # True (checks keys)
person.get("phone")         # None if missing (no error)
person.get("phone", "n/a")  # "n/a" if missing
del person["city"]          # remove a key
```

## Loop over one
```python
for key in person:
    print(key, person[key])
```
`key` is refilled each lap with the next key, same as `n` in a list loop.

## Common error
`person["phone"]` when "phone" is not a key raises `KeyError`. Use `.get()` or check with `in` first.

## Where I will use it
In threatline, store each attack result as a dictionary, then keep them in a list:
```python
result = {"attack": "I am the engineer", "leaked": True}
results = [result]
```
That list of dictionaries is the structure for a proper report later.