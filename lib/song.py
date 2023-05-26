from config import CONN, CURSOR

import sqlite3

import sqlite3

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        conn = sqlite3.connect('music.db')
        cursor = conn.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            album TEXT
        );
        """
        cursor.execute(sql)

        conn.commit()
        conn.close()

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)  # Create a Song instance
        song.save()  # Save the song to the database
        return song

    def save(self):
        conn = sqlite3.connect('music.db')
        cursor = conn.cursor()

        sql = """
        INSERT INTO songs (name, album)
        VALUES (?, ?)
        """
        cursor.execute(sql, (self.name, self.album))

        self.id = cursor.lastrowid

        conn.commit()
        conn.close()

        
song = Song("my baby", "umm on track ")
song.save()

print(f"name:{song.name} album: {song.album}")
