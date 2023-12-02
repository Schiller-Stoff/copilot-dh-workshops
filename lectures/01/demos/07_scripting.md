

# Scripting with Copilot

Examples for small everyday operations that can be performed via copilot.


## 1. Refactor folder structure

Given: You have a folder structure like:

- vor1
--- vor1.xml
- vor2
--- vor2.xml
- vor3
--- vor3.xml
- vor4
--- vor4.xml


Task: All the xml files should be renamed to SOURCE.xml 

Solution(s): 
    - Prompt: /generate a small python script. I want to loop through all folders at the given directory and rename contained vor*.xml files to source.xml. 
    - Prompt: /terminal I want to loop through all folders in the current working directory and rename contained vor*.xml files to source.xml.


## 2. Check availability of service

Given: You have a service running under http://localhost:3030/rest/. You are unsure if the service is running correctly.

Task: Check if the service is available (accepts an HTTP GET request). 

Solution(s): 
    - /terminal Check if the service at http://localhost:3030/rest/ accepts GET requests as expected. The response status code should be 200.

