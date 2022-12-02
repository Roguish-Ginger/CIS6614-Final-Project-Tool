# CIS6614-Final-Project-Tool
This is the code of the final project deliverable for the UCD CIS6614 Course

Project is based off the open source code found at https://github.com/mmcatcd/pii-tool

Current build and modifications to the above project can be found in this repository. 


## Installation

Supported Data Sources:
* JSON
* MySQL Database
* CSV
* TXT

### Prerequisuites:
* Python 3.9 or greater and the "pip" manager
  * check version with following command
  ```
  py -v
  ```
### To Download
Please download the associated files from this repository or use the below command:
```
git clone https://github.com/Roguish-Ginger/CIS6614-Final-Project-Tool.git
```
cd into the repo:

```
cd path/to/the/repo/updated project
```
```
pip install -r requirements.txt
```

### Troubleshooting

Sometimes the libraries in the requirements.txt wont download correctly to solve this just individually install the libraries from requirements.txt

## Usage

Feel free to use our test files found in the repository and download for your own testing purposes

### Commands for testing: 

```
py pii_tool.py -i tests/people.csv
```
```
py pii_tool.y -d hostname username database tablename
```
```
py pii_tool.py -i tests/string.txt
```
```
py pii_tool.py -i tests/employees.json
```
