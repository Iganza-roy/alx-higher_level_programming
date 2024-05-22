# JavaScript - Web scraping

This direectory contains my tasks on the JavaScript - Web scraping project.

**Web scraping** is the process of automatically extracting data from websites. This is done by writing code that sends requests to web pages, retrieves the HTML content, and then parses and extracts the necessary information.

## How to Use Request and Fetch API

The **fetch API** is a modern way to make network requests in JavaScript. It's built into the browser, and it's used to request resources like HTML pages, JSON data, or other files.
Example: 
- making a request:

```
fetch('https://jsonplaceholder.typicode.com/users')
  .then(response => response.json()) // Convert the response to JSON
  .then(data => console.log(data))    // Log the data
  .catch(error => console.error('Error:', error)); // Handle errors
```

- making a post request:
```
fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST', // Specify the method
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ title: 'foo', body: 'bar', userId: 1 }) // Convert the data to JSON
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));

```

## How to Read and Write a File Using fs Module
```
const fs = require('fs');

fs.readFile('example.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data); // Display the content of the file
});

```
## Read a file synchronously:
```
const fs = require('fs');

try {
  const data = fs.readFileSync('example.txt', 'utf8');
  console.log(data); // Display the content of the file
} catch (err) {
  console.error(err);
}
```
