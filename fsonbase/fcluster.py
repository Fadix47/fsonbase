import json
from uuid import uuid4
from typing import Union


def readjson(fp):
    try:
        with open(fp) as file: return json.load(file)
    except json.decoder.JSONDecodeError:
        with open(fp, 'w') as file: json.dump({}, file, ensure_ascii=False, indent=4)
        return {}


class fcluster:
    def __init__(self, filepath):
        self.filepath = filepath
        self.name = self.filepath[self.filepath.rfind('\\')+1:][:-5]

    def readall(self) -> dict:
        return readjson(self.filepath)

    def find_one_and_replace_document(self, document, content) -> None:
        if isinstance(document, dict) and isinstance(content, dict):
            try:
                json.dumps(content)
                content_ = readjson(self.filepath)

                try:
                    response = [x for x in list(content_.values()) if document.items() <= x.items()][0]
                    keys = list(content_.keys())
                    vals = list(content_.values())
                    content_[keys[vals.index(response)]] = content
                    with open(self.filepath, 'w') as file: json.dump(content_, file, ensure_ascii=False, indent=4)

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
                content_ = readjson(self.filepath)

                try:
                    response = [x for x in list(content_.values()) if document.items() <= x.items()]

                    for _ in response:
                        keys = list(content_.keys())
                        vals = list(content_.values())
                        content_[keys[vals.index(_)]] = content
                        with open(self.filepath, 'w') as file: json.dump(content_, file, ensure_ascii=False, indent=4)

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
                content_ = readjson(self.filepath)

                try:
                    response = [x for x in list(content_.values()) if document.items() <= x.items()][0]
                    keys = list(content_.keys())
                    vals = list(content_.values())
                    content_[keys[vals.index(response)]].update(content)
                    with open(self.filepath, 'w') as file: json.dump(content_, file, ensure_ascii=False, indent=4)

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
                content_ = readjson(self.filepath)

                try:
                    response = [x for x in list(content_.values()) if document.items() <= x.items()]
                    for _ in response:
                        keys = list(content_.keys())
                        vals = list(content_.values())
                        content_[keys[vals.index(_)]].update(content)
                        with open(self.filepath, 'w') as file: json.dump(content_, file, ensure_ascii=False, indent=4)

                except IndexError:
                    return Exception(f"Document not found in {self.name}")
            except TypeError:
                return TypeError("Input dict contains not supported elements!")
        else:
            return TypeError(f"Input type {type(content)} instead of <class 'dict'>")

    def find_documents(self, content) -> Union[list, None]:
        if isinstance(content, dict):

            content_ = list(readjson(self.filepath).values())
            response = [x for x in content_ if content.items() <= x.items()]

            if response:
                return response
            else:
                return None
        else:
            return TypeError(f"Input type {type(content)} instead of <class 'dict'>")

    def find_one_document(self, content) -> Union[dict, None]:
        if isinstance(content, dict):

            content_ = list(readjson(self.filepath).values())

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
            content_ = readjson(self.filepath)
            content_.update(content)

            try:
                json.dumps(content_)
                with open(self.filepath, 'w') as file: json.dump(content_, file, ensure_ascii=False, indent=4)
            except TypeError:
                return TypeError("Input dict contains not supported elements!")
        else:
            return TypeError(f"Input type {type(content)} instead of <class 'dict'>")

    def delete_document(self, document) -> None:
        if isinstance(document, dict):
            try:
                content_ = readjson(self.filepath)

                try:
                    response = [x for x in list(content_.values()) if document.items() <= x.items()][0]

                    keys = list(content_.keys())
                    vals = list(content_.values())

                    content_.pop(keys[vals.index(response)])

                    with open(self.filepath, 'w') as file: json.dump(content_, file, ensure_ascii=False, indent=4)

                except IndexError:
                    return Exception(f"Document not found in {self.name}")
            except TypeError:
                return TypeError("Input dict contains not supported elements!")
        else:
            return TypeError(f"Input type {type(document)} instead of <class 'dict'>")

    def delete_all(self) -> None:
        with open(self.filepath, 'w') as file: json.dump({}, file, ensure_ascii=False, indent=4)
