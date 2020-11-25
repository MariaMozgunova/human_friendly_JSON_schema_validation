import json
import logging
import os
import sys
from tkinter import Tk, filedialog

from jsonschema import exceptions, validate


def choose_dir():
    """Asks where to find JSON files, schemas and where to store logs"""
    root = Tk()
    root.withdraw()
    currdir = os.getcwd()
    ask = lambda message: filedialog.askdirectory(
        parent=root, 
        initialdir=currdir, 
        title=message,
    )
    events = ask('Choose dir with JSON files')
    schemas = ask('Choose dir with JSON schemas')
    results = ask('Choose dir where to store logs')

    return events, schemas, results


def configure_log(results):
    """Configures logs"""
    logging.basicConfig(
            format='%(asctime)s >> %(message)s', 
            level=logging.INFO, 
            filename=os.path.join(results, "logs.txt"), 
            filemode='w',
        )


def main():
    """
    Validates each event and schema against JSON format.
    In case of success, event is validated against specified JSON schema.
    """

    invalide_schemas = set()
    events, schemas, results = choose_dir()
    configure_log(results)
    
    for event in os.listdir(events):
        with open(os.path.join(events, event), 'r') as e:                
            try:
                s = None
                event_data = json.load(e)
                schema = event_data['event']
                schema += ".schema"

                if schema in invalide_schemas:  # have already encountered it
                    continue

                with open(os.path.join(schemas, schema), 'r') as s:
                    schema_data = json.load(s)
                validate(instance=event_data, schema=schema_data)

            except (KeyError, TypeError):
                logging.info(
                    f'In the file "{event}" keyword "event" is not ' + 
                    'presented. Add value "event" and a name of the ' +
                    'JSON schema without extension as a key.\n'
                )
                
            except FileNotFoundError as ex:
                logging.info(
                    f'No such JSON schema "{schema}" mentioned in the file ' + 
                    f'"{event}". Correct the value ' + 
                    'with the key "event" or create a new schema.\n'
                )
                
            except json.JSONDecodeError as ex:
                ex = ex.args[0]
                if s is None:
                    what = f'File  "{event}"'
                else:
                    what = f'Schema "{schema}"'
                    invalide_schemas.add(schema)
                logging.info(f"{what} doesn`t match JSON encoding: {ex}.\n")
                
            except exceptions.ValidationError as ex:                
                ex = ex.args[0]
                logging.info(
                    f'While validating file "{event}" ' +
                    f'against schema "{schema}": {ex}.\n'
                )  

            except Exception as ex:
                schema_error = ''

                if schema is not None:
                    schema_error = f' or schema "{schema}"'

                logging.info(
                    'Some error occured while wirking with a file ' +
                    f'"{event}"{schema_error}.\n'
                )


if __name__ == "__main__":
    main()
