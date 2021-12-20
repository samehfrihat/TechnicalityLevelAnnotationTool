"# TechnicalityLevelAnnotationTool" 

How to index the abstracts/documents into tocal mongoDB?
- install MongoDB locally
- update mongodb connection string in "src/config.py" (the default is "mongodb://127.0.0.1:27017")
- go to "src/controllers/german_abstracts_db.py" and run the following 
```
db_obj = GermanAbstractsDB()
print(db_obj.insert_csv(GERMAN_ABSTRACTS_PATH))
```
