# Program to understand similarities between words, series of words and sentences
# importing spacy and advanced language model 'en_core_web_md'
import spacy

nlp = spacy.load('en_core_web_md')

# Getting similarity between the words using 'similarity' keyword
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Comparing series of words and getting the similarities between words
# looping through the series of words using for loop and then using 'Similarity' keyword
tokens = nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# My observations:
# cat and monkey seems to be similar as they both are animals
# banana and apple have maximum similarity as they both are fruits
# similarly monkey and banana have similarity as monkey eats banana
# cat does not have any similarity with any fruit
# also it shows the highest similarity when both are same

# Program to compare longer sentences and getting similarities between the sentences
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go", "Hello,there is my car", "I\'ve lost my car in my car", "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# Observations when simpler language model 'en_core_web_sm' is used for the same program
# The following warning appeared
# The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based
# on the tagger, parser and NER, which may not give useful similarity judgements.
# This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship
# with word vectors and only use context-sensitive tensors. You can always add your own word vectors,
# or use one of the larger models instead if available.
# I also understand from the output and warning message that the similarity values are not even close enough
# which suggests that the small model does not process with a satisfactory results
