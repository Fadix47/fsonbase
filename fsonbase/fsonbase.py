from pathlib import Path
from os.path import isdir, isfile, exists
from os import listdir, remove
from .fcluster import fcluster
from .mcluster import mcluster
from typing import Union
from ujson import dump
import pymongo


class fsonbase:
    def __init__(self, url: str, cluster_name: str = None):
        url = url.replace('\\', '/')
        self.cluster_name = cluster_name
        if isdir(url):
            self.url = url
            self.connection = None
            self.clusters = tuple([fcluster(fr"{self.url}/{x}").name for x in listdir(self.url) if Path(x).suffix == '.json'])
        elif url.startswith("mongodb://"):
            if cluster_name is None:
                raise TypeError("'cluster_name' need to be specified for mongodb connection")
            if not isinstance(cluster_name, str):
                raise TypeError("'cluster_name' must be <str> parameter")
            self.url = url
            self.connection = pymongo.MongoClient(url)

            self.clusters = self.connection[cluster_name].list_collections()
        else:
            raise TypeError("Invalid url. Should be a local directory or mongodb url")

    def connect(self, cluster: str) -> fcluster | mcluster:
        if isfile(fr"{self.url}/{cluster}.json"):
            return fcluster(fr"{self.url}/{cluster}.json")
        elif self.connection:
            return mcluster(self.connection[self.cluster_name][cluster])
        else:
            raise FileNotFoundError('Cluster not found')

    def create(self, cluster: str) -> fcluster | mcluster:
        if not self.connection:
            if not exists(fr"{self.url}/{cluster}.json"):
                with open(fr"{self.url}/{cluster}.json", 'w') as file: dump({}, file, ensure_ascii=False, indent=4)
                return fcluster(fr"{self.url}/{cluster}.json")
            else:
                raise FileExistsError("Cluster already exists!")
        else:
            return mcluster(self.connection[self.cluster_name][cluster])

    def delete(self, cluster: Union[fcluster, str]) -> None:
        if not self.connection:
            name = fcluster(fr"{self.url}/{cluster}.json").name if isinstance(cluster, str) else cluster.name
            print(name)

            if exists(fr"{self.url}/{name}.json"):
                remove(fr"{self.url}/{name}.json")
            else:
                raise FileNotFoundError("Cluster does not exist!")
        else:
            self.connection[self.cluster_name].drop_collection(cluster)
