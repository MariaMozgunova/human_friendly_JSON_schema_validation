### User-friendly JSON schema validation
This program validates JSON files and schemas for them. In case of success, JSON file is validated against JSON schema. JSON schemas and JSON files should be in different directories. Errors during validation are logged to the logs.txt. The user chooses dirs to work with with graphical interface provided by `tkinter.filedialog.askdirectory`.


### Motivation
All the errors are logged in the user friendly way, so that nonprogammer could fix the bug in JSON file or schema if there are any.


### Installation
- Firstly, `cd` to the directory where you want program to be installed; 
- Then clone the project to your computer `git clone https://github.com/MariaMozgunova/user_friendly_JSON_schema_validation.git [dir_name]`. dir_name is optional. You need to use it in case you want cloned project to be named differently;  
- `cd` to the project folder;
- Make virtual environment `python -m venv venv`;
- Activate virtual environment;
- Install dependencies `pip install requirements.txt`.

Notice that you should have separate directories for JSON files and JSON schemas.
Great! Now you are ready to go.

### How to use?
- Run the script `validate.py` with the activated environment;
- Choose three directories: path to files, schemas and where to store results;
- Logs will be in the specified folder under the name `logs.txt`. Results with be presented in the following way: `%(current_time)s >> %(error_message)s.`

Example of running the program:
```
2020-11-25 17:08:23,899 >> While validating file "1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json" against schema "label_selected.schema": 'id' is a required property.

2020-11-25 17:08:23,904 >> While validating file "297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json" against schema "sleep_created.schema": 'source' is a required property.

2020-11-25 17:08:23,905 >> In the file "29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json" keyword "event" is not presented. Add value "event" and a name of the JSON schema without extension as a key.

2020-11-25 17:08:23,905 >> No such JSON schema "meditation_created.schema" mentioned in the file "2e8ffd3c-dbda-42df-9901-b7a30869511a.json". Correct the value with the key "event" or create a new schema.

2020-11-25 17:08:23,905 >> No such JSON schema "cmarker_calculated.schema" mentioned in the file "3ade063d-d1b9-453f-85b4-dda7bfda4711.json". Correct the value with the key "event" or create a new schema.

2020-11-25 17:08:23,906 >> While validating file "3b4088ef-7521-4114-ac56-57c68632d431.json" against schema "cmarker_created.schema": 'cmarkers' is a required property.

2020-11-25 17:08:23,907 >> No such JSON schema "meditation_created.schema" mentioned in the file "6b1984e5-4092-4279-9dce-bdaa831c7932.json". Correct the value with the key "event" or create a new schema.

2020-11-25 17:08:23,907 >> In the file "a95d845c-8d9e-4e07-8948-275167643a40.json" keyword "event" is not presented. Add value "event" and a name of the JSON schema without extension as a key.

2020-11-25 17:08:23,907 >> No such JSON schema "label_       selected.schema" mentioned in the file "ba25151c-914f-4f47-909a-7a65a6339f34.json". Correct the value with the key "event" or create a new schema.

2020-11-25 17:08:23,912 >> While validating file "bb998113-bc02-4cd1-9410-d9ae94f53eb0.json" against schema "sleep_created.schema": 'source' is a required property.

2020-11-25 17:08:23,912 >> No such JSON schema "meditation_created.schema" mentioned in the file "c72d21cf-1152-4d8e-b649-e198149d5bbb.json". Correct the value with the key "event" or create a new schema.

2020-11-25 17:08:23,915 >> While validating file "cc07e442-7986-4714-8fc2-ac2256690a90.json" against schema "label_selected.schema": 'id' is a required property.

2020-11-25 17:08:23,917 >> While validating file "e2d760c3-7e10-4464-ab22-7fda6b5e2562.json" against schema "cmarker_created.schema": 'cmarkers' is a required property.

2020-11-25 17:08:23,919 >> While validating file "f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json" against schema "sleep_created.schema": 'source' is a required property.

2020-11-25 17:08:23,921 >> While validating file "fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json" against schema "cmarker_created.schema": 'cmarkers' is a required property.

2020-11-25 17:08:23,922 >> While validating file "ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json" against schema "cmarker_created.schema": 'cmarkers' is a required property.
```
