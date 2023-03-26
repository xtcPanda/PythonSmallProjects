#Mad Libs game
# This code prompts the user to enter several words
# (a noun, verb, adjective, and three more nouns) and then inserts
# those words into a Mad Libs-style story.

#Asking the user for inputs and inserting it into a string

#Asking for a noun
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
noun3 = input("Enter one more noun: ")

#Asking for a verb
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")

#Asking for an adjective
adj = input("Enter an adjective: ")

#Creating the story
story = f"The {noun1} {verb1} through the {adj} house, holding a {noun2} in one hand and {verb2} {noun3} in the other."

#printing the story
print(story)

# you can make your Mad Libs game more complex
# by adding more prompts for different types of words
# (such as adverbs, prepositions, or proper nouns),
# creating a larger story with multiple paragraphs,
# or adding more interactivity for the user.
