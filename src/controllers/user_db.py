import sys
from datetime import datetime
from unittest.case import _id

from bson import ObjectId
from flask_babel import gettext
from pymongo import MongoClient, DESCENDING, operations

from src.config import CONNECTION_STRING, DEBUG
from src.models.response import return_fail, return_pass


class UsersDB:
    def __init__(self):
        client = MongoClient(CONNECTION_STRING)
        if 'ok' not in client.users_DB.command('ping'):
            sys.exit("Can't connect Users DB ...")
        self.db = client.MedicalDocumentsDB['UserDB']

    def _insert_doc(self, _doc):
        if DEBUG:
            print("[STEP] Store document in users database ....")
        try:
            _doc['time'] = datetime.now()
            _doc['annotations'] = 0
            _doc['level'] = gettext("annotation newbee")
            self.db.insert_one(_doc)
            _doc['username'] = 'user_' + str(_doc['_id'])
            self.db.update_one({"_id": _doc['_id']}, {"$set": {'username': _doc['username']}})
            return return_pass()
        except Exception as e:
            return return_fail(f"Failed to insert User, Error: {e.__str__()}")

    def new_user(self, _doc, admin=False):
        if DEBUG:
            print("[STEP] Validate user data ....")
        if "german_language_level" not in _doc or "english_language_level" not in _doc or "Med_level" not in _doc:
            return return_fail("Not a valid input!")
        _doc["admin"] = admin
        return self._insert_doc(_doc)

    def update_user(self, _doc):
        return self.db.update_one({"username": _doc['username']},
                                  {"$set": {'annotations': _doc['annotations'], 'level': _doc['level']}})

    def login(self, _doc):
        if DEBUG:
            print("[STEP] Check if user exist in DB")
        try:
            result = self.db.find_one({'username': _doc['username']}, projection={"_id": True, 'password': False})
            if result and len(result) > 0:
                return return_pass()
            return return_fail("Username or password incorrect, Please try again!")
        except Exception as e:
            print(e)
            return return_fail("Failed to connect DB please try later or contact WisPerMed team!")

    def change_password(self, username, _doc):
        if DEBUG:
            print("[STEP] Check if user exist in DB")
        try:
            result = self.db.find_one({"username": username, 'password': _doc['oldpass']}, projection={"_id": True})
            if not result or len(result) < 1:
                return return_fail("Something went wrong, Please try again!")
            query = {"_id": result["_id"]}
            self.db.update_one(query, {"$set": {'password': _doc['newpass']}})
            return return_pass()
        except Exception as e:
            print(e)
            return return_fail("Failed to connect DB please try later or contact WisPerMed team!")


if __name__ == '__main__':
    print('PyCharm')
    obj = UsersDB()
    _doc = {'username': 'test', 'password': '1234'}
    # print(obj.new_user(_doc))
    print(obj.login(_doc))
