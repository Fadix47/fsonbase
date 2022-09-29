from pathlib import Path
from os.path import isdir, isfile, exists
from os import listdir, remove
from .fcluster import fcluster
from typing import Union
from json import dump


class fsonbase:
    def __init__(self, filepath):
        filepath = filepath.replace('\\', '/')
        if isdir(filepath):
            self.filepath = filepath
            self.clusters = tuple([fcluster(fr"{self.filepath}/{x}").name for x in listdir(self.filepath) if Path(x).suffix == '.json'])
        else:
            raise TypeError("Invalid filepath. Should be directory")

    def connect(self, cluster: str) -> fcluster:
        if isfile(fr"{self.filepath}/{cluster}.json"):
            return fcluster(fr"{self.filepath}/{cluster}.json")
        else:
            raise FileNotFoundError('Cluster not found')

    def create(self, cluster: str) -> fcluster:
        if not exists(fr"{self.filepath}/{cluster}.json"):
            with open(fr"{self.filepath}/{cluster}.json", 'w') as file: dump({}, file, ensure_ascii=False, indent=4)

            return fcluster(fr"{self.filepath}/{cluster}.json")
        else:
            raise FileExistsError("Cluster already exists!")

    def delete(self, cluster: Union[fcluster, str]) -> None:
        name = fcluster(fr"{self.filepath}/{cluster}.json").name if isinstance(cluster, str) else cluster.name
        print(name)

        if exists(fr"{self.filepath}/{name}.json"):
            remove(fr"{self.filepath}/{name}.json")
        else:
            raise FileNotFoundError("Cluster does not exist!")
