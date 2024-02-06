![logo](https://i.ytimg.com/vi/Rv2rKCpO5tk/maxresdefault.jpg)

# python-input_output
A file is a container that stores information. In computer systems, a file is a contiguous set of bytes. Data in a computer system is always stored into files. Files can take different forms depending on the user requirements like data files, text files, program executable file etc.
There are several ways to present the output of a program; data can be printed in a human-readable form, or written to a file for future use.

### Reading and writing into files
The ```open()``` method returns a *file object*, and is most commonly used with two positional arguments and one keyword argument: ```open(filename, mode, encoding=None)```
The ```read()``` method is used to read the entire content of a file.
```
with open('filename.txt', 'r') as file:
    content = file.read()
    print(content)
```
A loop can e used to iterate through the lines of a file using the ```readline()``` method.
```
with open('filename.txt', 'r') as file:
    for line in file:
        print(line)

```
Using the **with** statement automatically closes the file when the block is exited, ensuring proper resource management.

```
with open('filename.txt', 'r') as file:
    # file operations here
    # file is automatically closed after exiting the block

```

![JSON](https://i.morioh.com/2020/04/11/02e4f4ae6ba3.jpg)

# JSON
JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write, and easy for machines to parse and generate.
- **Format:** JSON is composed of key-value pairs and supports various data types.

- **Syntax:** It uses a simple and readable syntax, making it easy to understand and write.

- **Data Types:** Supports common data types such as strings, numbers, objects, arrays, booleans, and null.

- **Serialization:** The process of converting a Python data structure into a JSON-formatted string.

- **Deserialization:** The process of reconstructing a data structure from a JSON-formatted string.

- **Use Cases:** Commonly used for data interchange between web servers and clients, configuration files, and storing structured data.

**example:**
```
{
  "name": "John Doe",
  "age": 25,
  "city": "Example City",
  "is_student": false,
  "grades": [95, 88, 72],
  "contact": {
    "email": "john@example.com",
    "phone": "123-456-7890"
  }
}

```
