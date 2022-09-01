import sys
from datetime import datetime, timedelta
from pprint import pprint

from pymongo import MongoClient, DESCENDING
from bson.objectid import ObjectId
import pandas as pd

from src.config import CONNECTION_STRING, DEBUG, GERMAN_ABSTRACTS_PATH, NO_OF_ANNOTATION_PER_DOC
from src.models.response import return_pass, return_fail


class GermanAbstractsDB:
    def __init__(self):
        client = MongoClient(CONNECTION_STRING)
        if 'ok' not in client.users_DB.command('ping'):
            sys.exit("Can't connect German Abstracts DB ...")
        self.db = client.MedicalDocumentsDB['GermanAbstracts']

    def insert_doc(self, _doc):
        _doc['time'] = datetime.now()
        self.db.insert(_doc)
        return True

    def insert_csv(self, file_path: str):
        if DEBUG:
            print("[STEP] Read CSV file ...")
        df = pd.read_csv(file_path, index_col=0, encoding='utf-8', sep=",")
        if DEBUG:
            print("[STEP] Insert Data to Database ...")
        self.db.insert_many(df.to_dict('records'))
        if DEBUG:
            print("[STEP] Insert date and annotation count docs ...")
        self._update_docs_with_time_and_annotation_count()
        if DEBUG:
            print("[RESULT] Data inserted successfully")
        return True

    def _update_docs_with_time_and_annotation_count(self):
        self.db.update_many({}, {"$set": {"annotation_count": 0, "time": datetime.now()}})

    def get_document(self, username):
        query = {
            "english_abstract": {"$exists": True},
            "annotations": {"$exists": False},
            "annotation_count": {"$lt": NO_OF_ANNOTATION_PER_DOC},
            "usernames": {"$nin": [username]}
        }
        projection = {
                "authors": False,
                "institutes": False,
                "date": False,
                "collaborators": False,
                "time": False,
            }
        try:
            result = self.db.find_one(query, projection=projection, sort=[("annotation_count", DESCENDING)])
            if result is None:
                return return_fail("Failed to find documents for annotation! Please context WisPerMed team!")
            return return_pass(result)
        except Exception as e:
            print(e)
            return return_fail("Failed to connect DB please try later or contact WisPerMed team!")

    def add_document_annotation(self, username, _id, param):
        self.db.update_many({"_id": ObjectId(_id)}, {"$inc": {"annotation_count": 1}, '$push': {'annotator': {"username": username, "value": param, "time": datetime.now()}, 'usernames': username}})


if __name__ == '__main__':
    print('PyCharm')
    db_obj = GermanAbstractsDB()
    # print(db_obj.insert_csv(GERMAN_ABSTRACTS_PATH))
    print(db_obj.get_document("test")["value"].keys())