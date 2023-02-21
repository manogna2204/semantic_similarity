# Program that tells what to watch next based on the word vector similarity of description of movies

# importing spacy and advanced language model 'en_core_web_md'
import spacy
nlp = spacy.load('en_core_web_md')


# Created a Movie class with title,description as parameters
class Movie():
    title = ""
    description = ""
    similarity = 0.0

    def __init__(self, title, description):
        self.title = title
        self.description = description

    # Defining Get and set methods for attributes
    def setSimilarity(self,value):
        self.similarity = value

    def getDescription(self):
        return self.description

    def getSimilarity(self):
        return self.similarity

    def getTitle(self):
        return self.title

    def __str__(self):
        output = f'Title : {self.title} ; Description : {self.description} ; Similarity : {self.similarity}'
        return output


# Defining a function that takes in the description as input parameter and returns the title of the most similar movie
def findMovieTitle(hulk_description):
    movie_file = open("movies.txt", 'r')
    hulk_nlp = nlp(hulk_description)
    movie_objects = []
    similar_movie = None
    # looping through the lines in the text file and
    # used similarity method to check the similarity between the descriptions,
    # then identifying the object with most similarity
    for index, line in enumerate(movie_file.readlines()):
        line_values = line.strip('\n').split(':')
        movie_object = Movie(line_values[0].strip(), line_values[1].strip())
        movie_nlp = nlp(movie_object.getDescription())
        similarity_value = hulk_nlp.similarity(movie_nlp)
        movie_object.setSimilarity(similarity_value)
        movie_objects.append(movie_object)
        if index == 0:
            similar_movie = movie_object
        else:
            if movie_object.getSimilarity() > similar_movie.getSimilarity():
                similar_movie = movie_object
    movie_file.close()
    return similar_movie.getTitle()


hulk_dict = {
    "Planet Hulk": "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, "
                   "the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can "
                   "live in peace.Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and "
                   "trained as a gladiator. "
}

movie_title = findMovieTitle(hulk_dict["Planet Hulk"])

print(f'Your next movie to watch based on your previous movie - {movie_title}')


