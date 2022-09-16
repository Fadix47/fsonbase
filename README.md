# fsonbase
Simple module that helps to use json as a strong databases

How to install 
```
pip install fsonbase
```

# Classes

### fsonbase - directory with json files
### fcluster - file ".json" extension

# Methods

### fsonbase

|    Method      |             Arguments         | Return |   Information   |
|:--------------:|:-----------------------------:|:------:|:---------------:|
|   connect    |  cluster: `str` |  `fcluster`  |  The name of json file without extension   |
|   create  | cluster: `str` | `fcluster` | Create the json file with chosen name |
| delete | cluster: `Union[fcluster, str]` | `None` | Delete the json file with chosen name or chosen cluster |

### fcluster

|    Method      |             Arguments         | Return |   Information   |
|:--------------:|:-----------------------------:|:------:|:---------------:|
|   readall    |  `None` |  `dict`  |  Return all information from cluster   |
|   insert_document  | content: `dict` | `None` | Adding document in json file on custom_id |
| delete_document | document: `dict` | `None` | Delete document with information from file |
| delete_all | `None` | `None` | Delete all information inside cluster |
| find_one_document | content: `dict` | `Union[dict, None]` | Return full information about ONE document or `None` if document not found |
| find_documents | content: `dict` | `Union[list, None]` | Returns list with information with all documents or `None` if documents not found |
| find_one_and_replace_document | document: `dict`, content: `dict` | `None` | Find one document and replace all information on `content` |
| find_one_and_update_document | document: `dict`, content: `dict` | `None` | Find one document and add new `content` |
| find_many_and_replace_document | document: `dict`, content: `dict` | `None` | Find all documents and replace all information on `content` |
| find_many_and_update_document | document: `dict`, content: `dict` | `None` | Find all documents and add new `content` |

# Usage example 
### Data structure of `E:\testdir`
```
📁jsons
└─ testbase.json
test.py
```
### Code example
```py
from fsonbase import fsonbase

base = fsonbase(r"E:\testdir\jsons")
cluster = base.connect("testbase")

print(cluster.readall())
```
### Output
```
{'7154f767321d488cad9e26f0af9b17bf': {'test': 'information', 'more': {'key': 10003, 'list': [202, 'test', 'testbase']}}}
```

