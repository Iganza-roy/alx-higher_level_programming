# Python - Network #1

## Fetch Internet Resources Using The urllib Package
![logo](https://www.educative.io/api/edpresso/shot/6312878216839168/image/6501873970315264)
**urllib.request** is a Python module for fetching URLs (Uniform Resource Locators). It offers a very simple interface, in the form of the ```urlopen``` function. This is capable of fetching URLs using a variety of different protocols. It also offers a slightly more complex interface for handling common situations - like basic authentication, cookies, proxies and so on. These are provided by objects called handlers and openers.

urllib.request supports fetching URLs for many “URL schemes” (identified by the string before the ```":"``` in URL - for example ```"ftp"```` is the URL scheme of ```"ftp://python.org/"```) using their associated network protocols (e.g. FTP, HTTP)
