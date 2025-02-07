import os
from app.extensions.mongodb import mongo_con
from app.utils.file import FileUitl

def applyMigrations():
    folderpath = os.path.join(os.path.dirname(__file__), 'scripts')
    migration_scripts = [f for f in os.listdir(folderpath)]
    executed_migrations = set([m.get('name') for m in list(mongo_con.getDb().get_collection('migrations').find())])
    db = mongo_con.getDb()
    for script in migration_scripts:
        module_path = os.path.join(folderpath, script)
        if not os.path.isfile(module_path):
            continue

        if not script in executed_migrations:
            module = FileUitl.load_module_by_path(module_path)
            module.migrate_up(mongo_con)
            db.get_collection('migrations').insert_one({"name" : script})
            




