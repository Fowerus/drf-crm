class AuthRouter(object):

    def db_for_read(self, model, **hints):
  
        return ['marketplace' if model._meta.app_label == 'Marketplace' else 'default'][0]


    def db_for_write(self, model, **hints):
        return ['marketplace' if model._meta.app_label == 'Marketplace' else 'default'][0]


    def allow_relation(self, obj1, obj2, **hints):

        return True


    def allow_migrate(self, db, app_label, model=None, **hints):

        if app_label == 'Marketplace':
            return db == 'marketplace'

        else:
            return db == 'default'
        return None