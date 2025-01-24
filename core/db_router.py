class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'users':
            return 'users_db'
        elif model._meta.db_table == 'products':
            return 'products_db'
        elif model._meta.db_table == 'orders':
            return 'orders_db'
        return None

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
