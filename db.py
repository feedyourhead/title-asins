def mongosession():
    from pylons import config
    return config['pylons.app_globals'].db


class Globals(object):
    """Globals acts as a container for objects available throughout the
    life of the application
    """
    
    def __init__(self, config):
        from mongokit import Connection
        
        self.connection = Connection(
            host=config['mongodb.url'],
            replicaset=config.get('mongodb.replica_set_name', '')
        )

        self.db = self.connection[config['mongodb.dbname']]
        if config['mongodb.username']:
            # For the sake of dev environment managed by puppet it's much
            # easier to allow connecting to the mongodb with disabled
            # authentication. This can be accomplished by leaving
            # empty credentials in the config file.
            self.db.authenticate(
                config['mongodb.username'], config['mongodb.password'])


        self.connection.register(register_models)
