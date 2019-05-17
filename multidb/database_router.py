class DataBaseRouter:

    def db_for_read(self, model, **hints):

        if model._meta.app_label == 'app2':
            return 'parsed_cvs'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label == 'app2':
            return 'parsed_cvs'
        return None

    def allow_relation(self, obj1, obj2, **hints):

        if obj1._meta.app_label == 'app2' or \
           obj2._meta.app_label == 'app2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label == 'app2':
            return db == 'parsed_cvs'
        return None
