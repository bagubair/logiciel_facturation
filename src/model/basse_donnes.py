import psycopg2 as sql
import os
from consts import DATA_DIR


class BaseDeDonnee:
    def init(self, dbname, user, password, host='localhost'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.conn = None
        self.cur = None

    def connect(self):
        """
        Pour se connecter à la base de donnée.

        ----------------------------------------------------------

        """

        self.conn = sql.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host
        )
        self.cur = self.conn.cursor()

    def disconnect(self):
        """
        Pour se déconnecter de la base de donnée.

        ----------------------------------------------------------

        """

        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def execute_requete(self, requete: str):
        """
        Execute une requête SQL et retourne-le résulta.

        ----------------------------------------------------------

        Args:
            requete: The SQL query to execute.

        Return:
            liste: une liste de tuples représentant le résulta de la requête.
        """

        self.cur.execute(requete)

        # On va verifier si la requête commence par SELECT ou pas les autres méthodes(INSERT, UPDATE, DELETE)
        if requete.strip().upper().startswith('SELECT'):
            return self.cur.fetchall()
        else:
            # On ajoute commit() pour les méthodes CRUD.
            self.conn.commit()
            return None

    def init_table(self):
        fichier_basse = os.path.join(DATA_DIR, "cree_table.sql")
        self.cur.execute(open(fichier_basse, 'r').read())
        self.conn.commit()