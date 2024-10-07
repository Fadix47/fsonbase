# fsonbase
Simple module based on ujson that helps to use json as a strong databases

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
|   connect    |  cluster: `str` |  `Union[fcluster, mcluster]`  |  The name of json file without extension or mongo collection name  |
|   create  | cluster: `str` | `Union[fcluster, mcluster]` | Create the json file with chosen name or creates a collection in mongo |
| delete | cluster: `Union[fcluster, str]` | `None` | Delete the json file with chosen name or chosen cluster. **Works only with local files** |

### fcluster

|    Method      |             Arguments         | Return |   Information   |
|:--------------:|:-----------------------------:|:------:|:---------------:|
|   readall    |  `None` |  `list`  |  Return all information from file   |
|   insert_document  | content: `dict` | `None` | Adding document in json file on custom_id |
| delete_document | document: `dict` | `None` | Delete one document with information from file |
| delete_many_documents | document: `dict` | `None` | Delete all documents with given information from file |
| clear_document | `None` | `None` | Delete all information inside cluster |
| find_one_document | content: `dict` | `Union[dict, None]` | Return full information about ONE document or `None` if document not found |
| find_documents | content: `dict` | `Union[list, None]` | Returns list with information with all documents or `None` if documents not found |
| find_one_and_replace_document | document: `dict`, content: `dict` | `None` | Find one document and replace all information on `content` |
| find_one_and_update_document | document: `dict`, content: `dict` | `None` | Find one document and add new `content` |
| find_many_and_replace_document | document: `dict`, content: `dict` | `None` | Find all documents and replace all information on `content` |
| find_many_and_update_document | document: `dict`, content: `dict` | `None` | Find all documents and add new `content` |

### mcluster

|    Method      |             Arguments         | Return |   Information   |
|:--------------:|:-----------------------------:|:------:|:---------------:|
|   readall    |  `None` |  `list`  |  Return all information from collection   |
|   insert_document  | content: `dict` | `None` | Adding document in collection |
| delete_document | document: `dict` | `None` | Delete one document with information from collection |
| delete_many_documents | document: `dict` | `None` | Delete all documents with given information from collection |
| clear_document | `None` | `None` | Delete all information inside collection |
| find_one_document | content: `dict` | `Union[dict, None]` | Return full information about ONE document or `None` if document not found |
| find_documents | content: `dict` | `Union[list, None]` | Returns list with information with all documents or `None` if documents not found |
| find_one_and_replace_document | document: `dict`, content: `dict` | `None` | Find one document and replace all information on `content` |
| find_one_and_update_document | document: `dict`, content: `dict` | `None` | Find one document and add new `content` |
| find_many_and_replace_document | document: `dict`, content: `dict` | `None` | Find all documents and replace all information on `content` |
| find_many_and_update_document | document: `dict`, content: `dict` | `None` | Find all documents and add new `content` |


# Usage example with local files
### Data structure of `E:\testdir`
```
📁jsons
└─ testbase.json
test.py
```
### Code example
```py
from fsonbase import fsonbase

base = fsonbase(url=r"E:\testdir\jsons")
cluster = base.connect("testbase")

print(cluster.readall())
```
### Output
```
[{'test': 'information', 'more': {'key': 10003, 'list': [202, 'test', 'testbase']}}]
```


# Usage example with mongodb
### Code example
```py
from fsonbase import fsonbase

base = fsonbase(url=r"mongodb://localhost:27017/", cluster_name="myproject")
cluster = base.connect("testbase")

print(cluster.readall())
```
### Output
```
[{'test': 'information', 'more': {'key': 10003, 'list': [202, 'test', 'testbase']}}]
```
