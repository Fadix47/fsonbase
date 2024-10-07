import json
from typing import Union
import pymongo.collection


class mcluster:
    def __init__(self, cluster: pymongo.collection.Collection):
        self.cluster = cluster
        self.name = cluster.name
        self.cache = {}

    def readall(self) -> list:
        return [{k: v for k, v in d.items() if k != '_id'} for d in list(self.cluster.find({}))]

    def find_one_and_replace_document(self, document, content) -> None:
        if isinstance(document, dict) and isinstance(content, dict):
            try:
                json.dumps(content)

                try:
                    self.cluster.find_one_and_replace(document, content)
                except:
                    return Exception(f"Document not found in {self.name}")
            except TypeError:
                return TypeError("Input dict contains not supported elements!")
        else:
            return TypeError(f"Input type {type(content)} instead of <class 'dict'>")

    def find_many_and_replace_document(self, document, content) -> None:
        if isinstance(document, dict) and isinstance(content, dict):
            try:
                json.dumps(content)
                try:
                    alldocs = self.cluster.find(document)
                    [self.cluster.find_one_and_replace(doc, content) for doc in alldocs]
                except Exception as e:
                    return Exception(e)
            except TypeError:
                return TypeError("Input dict contains not supported elements!")
        else:
            return TypeError(f"Input type {type(content)} instead of <class 'dict'>")

    def find_one_and_update_document(self, document, content) -> None:
        if isinstance(document, dict) and isinstance(content, dict):
            try:
                json.dumps(content)

                try:
                    self.cluster.find_one_and_update(document, {'$set': content})
                except Exception as e:
                    return Exception(e)
            except TypeError:
                return TypeError("Input dict contains not supported elements!")
        else:
            return TypeError(f"Input type {type(content)} instead of <class 'dict'>")

    def find_many_and_update_document(self, document, content) -> None:
        if isinstance(document, dict) and isinstance(content, dict):
            try:
                json.dumps(content)

                try:
                    alldocs = self.cluster.find(document)
                    [self.cluster.find_one_and_update(doc, {'$set': content}) for doc in alldocs]
                except Exception as e:
                    return Exception(e)
            except TypeError:
                return TypeError("Input dict contains not supported elements!")
        else:
            return TypeError(f"Input type {type(content)} instead of <class 'dict'>")

    def find_documents(self, content) -> Union[list, None]:
        if isinstance(content, dict):
            return [{k: v for k, v in d.items() if k != '_id'} for d in list(self.cluster.find(content))]
        else:
            return TypeError(f"Input type {type(content)} instead of <class 'dict'>")

    def find_one_document(self, content) -> Union[dict, None]:
        if isinstance(content, dict):
            try:
                return {k: v for k, v in self.cluster.find_one(content).items() if k != '_id'}
            except AttributeError:
                return None
            except Exception as e:
                return Exception(e)
        else:
            return TypeError(f"Input type {type(content)} instead of <class 'dict'>")

    def insert_document(self, content) -> None:
        if isinstance(content, dict):
            try:
                json.dumps(content)
                self.cluster.insert_one(content)
            except TypeError:
                return TypeError("Input dict contains not supported elements!")
        else:
            return TypeError(f"Input type {type(content)} instead of <class 'dict'>")

    def delete_document(self, document) -> None:
        if isinstance(document, dict):
            try:
                json.dumps(document)
                try:
                    self.cluster.delete_one(document)
                except Exception as e:
                    return Exception(e)
            except TypeError:
                return TypeError("Input dict contains not supported elements!")
        else:
            return TypeError(f"Input type {type(document)} instead of <class 'dict'>")

    def delete_many_documents(self, document) -> None:
        if isinstance(document, dict):
            try:
                json.dumps(document)
                try:
                    self.cluster.delete_many(document)
                except Exception as e:
                    return Exception(e)
            except TypeError:
                return TypeError("Input dict contains not supported elements!")
        else:
            return TypeError(f"Input type {type(document)} instead of <class 'dict'>")

    def clear_document(self) -> None:
        try:
            self.cluster.delete_many({})
        except Exception as e:
            return Exception(e)
