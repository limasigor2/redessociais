import os
import re
import sqlite3
import keys

def stopwords_files_to_list():
	lista = []
	for arquivo in os.listdir('stop-words'):
		with open('stop-words/{}'.format(arquivo), "r", encoding="ISO-8859-1") as file:
			lista.append((file.read().splitlines()))
	return lista

def remove_stop_words(tweet):
    new_words = ''
    for word in tweet.split(' '):
        if word not in stopwords_files_to_list():
            new_words += ' ' + word 
    return new_words

def remove_link(tweet):
	return re.sub(r"http\S+", "", tweet)

def remove_metions(tweet):
	new_tweet = ''
	for word in tweet.split(" "):
		if '@' not in word:
			new_tweet += " " + word
	return new_tweet

def pre_process_tweet(tweet):
	return remove_link(remove_stop_words(remove_metions(tweet)))

def conexao():
    return sqlite3.connect(keys.DB_PATH)

def persist_at(conn, id, text, user, retweet_status, original_user):
	if original_user == "":
		original_user = "' '"
	conn.cursor().execute("INSERT INTO tweets VALUES ('{}', '{}', {}, {}, {})".format(id, text, user, retweet_status, original_user))

	conn.commit()
