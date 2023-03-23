#!/usr/bin/python3
""" create textvariable """

db.execute('CREATE TABLE IF NOT EXISTS "customer" ("id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"name" TEXT NOT NULL, "contact"	TEXT NOT NULL,  " created_at" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP)')
db.execute('CREATE TABLE IF NOT EXISTS "tech" ("id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,	"name"	TEXT NOT NULL,	"contact"	TEXT NOT NULL, "title"	TEXT NOT NULL,	"year"	TEXT NOT NULL)')
db.execute('CREATE TABLE IF NOT EXISTS "cust_concern" ("concern_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,	"job" TEXT NOT NULL, "note" INTEGER NOT NULL, "type" TEXT NOT NULL, "car_id" INTEGER NOT NULL, FOREIGN KEY(`car_id`) REFERENCES `vehicles`(`car_id`))')
db.execute('CREATE TABLE IF NOT EXISTS "vehicles" ("car_id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,  "vin" TEXT NOT NULL,"reg" TEXT NOT NULL,"maker" INTEGER NOT NULL,"year" TEXT NOT NULL,"job_id" INTEGER NOT NULL,  "cost" TEXT NOT NULL, "status"TEXT NOT NULL,FOREIGN KEY(`job_id`) REFERENCES `Customer`(`id`))')
conn.commit()
