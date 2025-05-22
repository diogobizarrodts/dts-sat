
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS os;

CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT
);

CREATE TABLE os (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    description TEXT,
    status TEXT,
    FOREIGN KEY (client_id) REFERENCES clients (id)
);
