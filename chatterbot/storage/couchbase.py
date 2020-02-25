import re
from chatterbot.storage import StorageAdapter


class CouchbaseDatabaseAdapter(StorageAdapter):
    """
    The CouchbaseDatabaseAdapter is an interface that allows
    ChatterBot to store statements in a Couchbase database.

    :keyword database_uri: The URI of a remote instance of Couchbase.
                           This can be any valid
                           `Couchbase connection string <https://docs.couchbase.com/python-sdk/current/start-using-sdk.html>`_
    :type database_uri: str

    .. code-block:: python

       database_uri='couchbase://localhost/'
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        from couchbase.cluster import Cluster
        from couchbase.cluster import PasswordAuthenticator

        #from pymongo import MongoClient
        #from pymongo.errors import OperationFailure

        self.database_uri = kwargs.get(
            'database_uri', 'couchbase://localhost'
        )
        self.cluster = Cluster(self.database_uri)
        self.authenticator = PasswordAuthenticator('username', 'password')
        self.cluster.authenticate(self.authenticator)
        self.bucket = self.cluster.open_bucket('chatterbot-database')