import psycopg2 as sql
import os
from const import DATA_DIR


class BaseDeDonnee:
    def __init__(self, dbname, user, password, host='localhost'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.conn = None
        self.cur = None


    def cree_dbname_si_non_existe(self):
        """
        Crée la base de données si elle n'existe pas.
        """
        conn = sql.connect(
            dbname='postgres',  # Connexion à la base de données par défaut
            user=self.user,
            password=self.password,
            host=self.host
        )
        conn.autocommit = True
        cur = conn.cursor()

        # Vérifiez si la base de données existe déjà
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{self.dbname}'")
        exists = cur.fetchone()

        if not exists:
            cur.execute(f'CREATE DATABASE {self.dbname}')

        cur.close()
        conn.close()

    def connect(self):
        """
        Pour se connecter à la base de donnée.
        """
        self.cree_dbname_si_non_existe()

        self.conn = sql.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host
        )
        self.cur = self.conn.cursor()

    def disconnect(self):
        """Pour se déconnecter de la base de donnée."""

        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def execute_requete(self, requete: str, valeurs: tuple = None):
        """Execute une requête SQL et retourne-le résulta.
        Args:
            requete: The SQL query to execute.

        Return:
            liste: une liste de tuples représentant le résulta de la requête.
        """

        self.connect()
        if valeurs:
            self.cur.execute(requete, valeurs)
        else:
            self.cur.execute(requete)
        

        # On va verifier si la requête commence par SELECT ou pas les autres méthodes(INSERT, UPDATE, DELETE)
        if requete.strip().upper().startswith('SELECT'):
            return self.cur.fetchall()
        else:
            # On ajoute commit() pour les méthodes CRUD.
            self.conn.commit()
            self.disconnect()
            return None

    def init_table(self):
        fichier_basse = os.path.join(DATA_DIR, "cree_table.sql")
        self.connect()
        self.cur.execute(open(fichier_basse, 'r').read())
        self.conn.commit()
        self.disconnect()