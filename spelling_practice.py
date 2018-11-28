"""Help Ever practice his spelling words."""
from random import choice
from time import sleep

from say_something import say_something

def run_quiz():

    words = ['completed', 'deleted', 'shoulder']
    completed_words = []

    correct_msgs = ['correct', 'absolutely right', 'yes!', 'excellent']
    incorrect_msgs = ['oh no!', 'wrong', 'incorrect', "oh my, you'll have to try again"]

    say_something("I'm going to quiz you on your spelling words. Get ready.")
    sleep(5)
    while words:
        word = choice(words)
        say_something(f"Please spell the word: {word}")

        attempt = input("Spell the word: ")

        if attempt == word:
            say_something(choice(correct_msgs))
            words.remove(word)
        else:
            say_something(choice(incorrect_msgs))

    say_something("You got all the words correct!")