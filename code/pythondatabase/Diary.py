# -*- coding: utf-8 -*-
"""
Created on Mon May 29 15:27:48 2017

@author: a93701011
"""

#! usr/bin/env python3
from collections import OrderedDict 
import datetime
import sys
import os

from peewee import *

db = SqliteDatabase("diary.db")


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default = datetime.datetime.now)
    
    class Mete:
        database = db 

def clear():
    os.system("cls" if os.name == 'nt' else "clear")

def initialize():
    """Create the database """
    db.connect()
    db.create_tables([Entry], safe = True)
    
def menu_loop():
    """ show the menu """
    choice = None

    while choice != "q":
        clear()
        print("Enter 'q' to leave")
        for key, value in menu.items():
            print("{}) {}".format(key, value.__doc__))
        choice = input("Action:").lower().strip()
    
        if choice in menu:
            clear()
            menu[choice]()

def add_entry():
    """ add a entry """
    print("Enter your entry! Enter ctrl-z when finished")
    data = sys.stdin.read().strip()
    
    if data:
        if input("Save entry? [Yn]").lower() != 'n':
            Entry.create(content = data)
            print("Saved successfully!")

    
def view_entries(search_query = None ):
    """ view the entries """
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query != None:
        entries = entries.where(Entry.content.contains(search_query))
    
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear()
        print(timestamp)
        print("="*len(timestamp))
        print(entry.content)
        print("\n\n"+"="*len(timestamp))
        print("n) next content")
        print("d) delete the entry")
        print("q) back to menu")
    
        next_action = input("Action: [Ndq] ").lower()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)
            
def delete_entry(entry):
    """ delete a entry """
    if input("Are you sure to delete? [Yn] ").lower() != "n":
        entry.delete_instance()
    print("Entry deleted!")
    
    
def search_entry():
     """ search entry with a string"""
     view_entries(input("Enter search query: ").lower())
    

menu = OrderedDict([
        ("a",add_entry),
        ("v",view_entries),
        ("s",search_entry)
        
    ])


if __name__ == "__main__":
    initialize()
    menu_loop()
