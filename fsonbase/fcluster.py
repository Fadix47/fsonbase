import json
from uuid import uuid4
from typing import Union
from json import JSONDecodeError


class fcluster:
    def __init__(self, filepath):
        self.filepath = filepath
        self.name = self.filepath[self.filepath.rfind('\\')+1:][:-5]
        self.cache = {}

    def readjson(self, fp):
        try:
            with open(fp, encoding='UTF-8') as file:
                content = json.load(file)
                self.cache = dict(content.items())
                return content
        except JSONDecodeError:
            with open(self.filepath, 'w') as file: json.dump(self.cache, file, ensure_ascii=True, indent=4)
            return self.cache

    def readall(self) -> list:
        return list(self.readjson(self.filepath).values())

    def find_one_and_replace_document(self, document, content) -> None:
        if isinstance(document, dict) and isinstance(content, dict):
            try:
                json.dumps(content)
                content_ = self.readjson(self.filepath)

                try:
                    response = [x for x in list(content_.values()) if document.items() <= x.items()][0]
                    keys = list(content_.keys())
                    vals = list(content_.values())
                    content_[keys[vals.index(response)]] = content
                    with open(self.filepath, 'w') as file: json.dump(content_, file, ensure_ascii=True, indent=4)

                except IndexError:
                    return Exception(f"Document not found in {self.name}")
            except TypeError:
                return TypeError("Input dict contains not supported elements!")
        else:
            return TypeError(f"Input type {type(content)} instead of <class 'dict'>")

    def find_many_and_replace_document(self, document, content) -> None:
        if isinstance(document, dict) and isinstance(content, dict):
            try:
                json.dumps(content)
                content_ = self.readjson(self.filepath)

                try:
                    response = [x for x in list(content_.values()) if document.items() <= x.items()]

                    keys = list(content_.keys())
                    vals = list(content_.values())

                    for _ in response:
                        content_[keys[vals.index(_)]] = content

                    with open(self.filepath, 'w') as file: json.dump(content_, file, ensure_ascii=True, indent=4)

                except IndexError:
                    return Exception(f"Document not found in {self.name}")
            except TypeError:
                return TypeError("Input dict contains not supported elements!")
        else:
            return TypeError(f"Input type {type(content)} instead of <class 'dict'>")

    def find_one_and_update_document(self, document, content) -> None:
        if isinstance(document, dict) and isinstance(content, dict):
            try:
                json.dumps(content)
                content_ = self.readjson(self.filepath)

                try:
                    response = [x for x in list(content_.values()) if document.items() <= x.items()][0]
                    keys = list(content_.keys())
                    vals = list(content_.values())
                    content_[keys[vals.index(response)]].update(content)
                    with open(self.filepath, 'w') as file: json.dump(content_, file, ensure_ascii=True, indent=4)

                except IndexError:
                    return Exception(f"Document not found in {self.name}")
            except TypeError:
                return TypeError("Input dict contains not supported elements!")
        else:
            return TypeError(f"Input type {type(content)} instead of <class 'dict'>")

    def find_many_and_update_document(self, document, content) -> None:
        if isinstance(document, dict) and isinstance(content, dict):
            try:
                json.dumps(content)
                content_ = self.readjson(self.filepath)

                try:
                    response = [x for x in list(content_.values()) if document.items() <= x.items()]

                    keys = list(content_.keys())
                    vals = list(content_.values())

                    for _ in response:
                        content_[keys[vals.index(_)]].update(content)

                    with open(self.filepath, 'w') as file: json.dump(content_, file, ensure_ascii=True, indent=4)

                except IndexError:
                    return Exception(f"Document not found in {self.name}")
            except TypeError:
                return TypeError("Input dict contains not supported elements!")
        else:
            return TypeError(f"Input type {type(content)} instead of <class 'dict'>")

    def find_documents(self, content) -> Union[list, None]:
        if isinstance(content, dict):

            content_ = list(self.readjson(self.filepath).values())
            response = [x for x in content_ if content.items() <= x.items()]

            if response:
                return response
            else:
                return None
        else:
            return TypeError(f"Input type {type(content)} instead of <class 'dict'>")

    def find_one_document(self, content) -> Union[dict, None]:
        if isinstance(content, dict):

            content_ = list(self.readjson(self.filepath).values())

            try:
                response = [x for x in content_ if content.items() <= x.items()][0]
            except IndexError:
                response = None

            return response
        else:
            return TypeError(f"Input type {type(content)} instead of <class 'dict'>")

    def insert_document(self, content) -> None:
        if isinstance(content, dict):

            content = dict({uuid4().hex: content})
            content_ = self.readjson(self.filepath)
            content_.update(content)

            try:
                json.dumps(content_)
                with open(self.filepath, 'w') as file: json.dump(content_, file, ensure_ascii=True, indent=4)
            except TypeError:
                return TypeError("Input dict contains not supported elements!")
        else:
            return TypeError(f"Input type {type(content)} instead of <class 'dict'>")

    def delete_document(self, document) -> None:
        if isinstance(document, dict):
            try:
                content_ = self.readjson(self.filepath)

                try:
                    response = [x for x in list(content_.values()) if document.items() <= x.items()][0]

                    keys = list(content_.keys())
                    vals = list(content_.values())

                    content_.pop(keys[vals.index(response)])

                    with open(self.filepath, 'w') as file: json.dump(content_, file, ensure_ascii=True, indent=4)

                except IndexError:
                    return Exception(f"Document not found in {self.name}")
            except TypeError:
                return TypeError("Input dict contains not supported elements!")
        else:
            return TypeError(f"Input type {type(document)} instead of <class 'dict'>")

    def delete_many_documents(self, document) -> None:
        if isinstance(document, dict):
            try:
                content_ = self.readjson(self.filepath)

                try:
                    response = [x for x in list(content_.values()) if document.items() <= x.items()]

                    keys = list(content_.keys())
                    vals = list(content_.values())

                    [content_.pop(keys[vals.index(_)]) for _ in response]

                    with open(self.filepath, 'w') as file: json.dump(content_, file, ensure_ascii=True, indent=4)

                except IndexError:
                    return Exception(f"Document not found in {self.name}")
            except TypeError:
                return TypeError("Input dict contains not supported elements!")
        else:
            return TypeError(f"Input type {type(document)} instead of <class 'dict'>")

    def clear_document(self) -> None:
        with open(self.filepath, 'w') as file: json.dump({}, file, ensure_ascii=True, indent=4)
