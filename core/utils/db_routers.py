class DataBaseRouter:
    """
    A router to control if database should use
    primary database or mongo one.
    """

    nonrel_models = {'log'}
    marketplace_model = {'Marketplace'}

    def db_for_read(self, model, **hints):
        return ['mongo' if model._meta.app_label == 'Marketplace'
                or model._meta.model_name in self.nonrel_models else 'default'][0]

    def db_for_write(self, model, **hints):
        return ['mongo' if model._meta.app_label == 'Marketplace'
                or model._meta.model_name in self.nonrel_models else 'default'][0]

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label == 'Marketplace' or model_name == 'log':
            return db == 'mongo'

        else:
            return db == 'default'

    # def db_for_read(self, model, **_hints):
    #     if model._meta.model_name in self.nonrel_models or model._meta.model_name in self.marketplace_model :
    #         return 'mongo'
    #     return 'default'

    # def db_for_write(self, model, **_hints):
    #     if model._meta.model_name in self.nonrel_models or model._meta.model_name in self.marketplace_model:
    #         return 'mongo'
    #     return 'default'

    # def allow_migrate(self, _db, _app_label, model_name=None, **_hints):
    #     if _db == 'mongo' or model_name in self.nonrel_models or  model_name in self.marketplace_model:
    #         return False
    #     return True
