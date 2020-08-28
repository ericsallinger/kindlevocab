from django.contrib import admin
from .models import Vocab

import requests
import sqlite3
import time
import datetime
import random
import os

@admin.register(Vocab)
class VocabAdmin(admin.ModelAdmin):
    list_display = (['word','usage','definition','book','prevent_cull'])

    def print_db(self, request, queryset):
        conn = sqlite3.connect('./vocab.db')
        cursor = conn.cursor()
        cursor.execute('SELECT word_key,usage,title FROM lookups INNER JOIN BOOK_INFO ON lookups.book_key=BOOK_INFO.id;')
        data = cursor.fetchall()
        
        dict_items = []
        for row in data:
            dict_items.append 
            vocobj = Vocab.objects.create_word(row[0],row[1],row[2])
            # print(row[0])


    def get_definition(self, request, queryset):
        headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': "2f5c082e28msh1f6864866fdf779p18bc78jsne87ebfa1e851"
        }
        for Vocab in queryset:
            url = "https://wordsapiv1.p.rapidapi.com/words/"+Vocab.word+"/definitions"
        
            response = requests.request("GET", url, headers=headers)
            response_json = response.json()
            defs_and_partsofspeech = ""
            if(response.ok):
                break_at_three_counter = 0
                for definition in response_json["definitions"]:
                    if break_at_three_counter == 3:
                        break
                    defs_and_partsofspeech = defs_and_partsofspeech + "Part of Speech: " + str(definition["partOfSpeech"]) + ", definition: " + str(definition["definition"]+"\n")
                    break_at_three_counter += 1
                print(defs_and_partsofspeech)
                Vocab.definition = defs_and_partsofspeech
                Vocab.save()
            else:
                print("failure")

        
        #wordapi definitions    
    


    def keep_word(self, request, queryset):
        # will become send to anki
        for Vocab in queryset:
            Vocab.prevent_cull = True
            Vocab.save()
            

    actions = [print_db,get_definition,keep_word]


