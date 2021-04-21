import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
import re
from bs4 import BeautifulSoup
import numpy as np


class performtext2word:
    """ Text pre-processing for nlp applications
	
	Attributes:
		None
			
	"""
    
    def __init__(self):
        
        pass
    
    def review_to_words(self, review):
        """Method to clean a unit text using 'nltk'. For ex. a restaurant review.
        - removes html tags
        - converts all to lowercase
        - applies word stemming
        - splits text string into individual words
        - removes stopwords (words that do not affect sentiment of the text)
				
		Args:
			review (string): a single review
		
		Returns:
			list of cleaned words out of the input text review
		"""
        
        nltk.download("stopwords", quiet=True)
        stemmer = PorterStemmer()
        text = BeautifulSoup(review, "html.parser").get_text() # Remove HTML tags
        text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower()) # Convert to lower case
        words = text.split() # Split string into words
        words = [w for w in words if w not in stopwords.words("english")] # Remove stopwords
        words = [PorterStemmer().stem(w) for w in words] # stem
    
        return words
        
    
    def preprocess_data(self, data_train, data_test):
        """Method to convert individual training and test text data into a list of cleaned
        words using the 'review_to_words', collectively stored in a list
				
		Args:
			data_train (list): training data (text strings) stored as a list
            data_test (list): test data (text strings) stored as a list
		
		Returns:
			words_train (list): each training data text converted to list of cleaned
            words using the 'review_to_words' function stored within a list
            words_test (list): each test data text converted to list of cleaned
            words using the 'review_to_words' function stored within a list
		"""
        
        words_train = [self.review_to_words(review) for review in data_train]
        words_test = [self.review_to_words(review) for review in data_test]
        
        return words_train, words_test
        
    
    def build_dict(self, data_train, vocab_size = 5000):
        """Method to Construct and return a dictionary mapping each of the most frequently appearing words to a unique integer.
				
		Args:
			data_train (string): training data list obtained using the preprocess_data() method
		
		Returns:
			word_dict (dictionary): Dictionary of words
            freqlist (list): List containing frequency of words in training data
		"""
        
        word_count = {} # A dict storing the words that appear in the reviews along with how often they occur
    
        wordlist = []
        [wordlist.append(word) for list in train_X for word in list]
        uniquewordlist = []
        freqlist = []
    
        for word in wordlist:
            if word not in uniquewordlist:
                uniquewordlist.append(word)
                freqlist.append(1)
            else:
                freqlist[uniquewordlist.index(word)] = freqlist[uniquewordlist.index(word)] + 1
    
        word_count["word"] = uniquewordlist
        word_count["freq"] = freqlist
    
    
    # TODO: Sort the words found in `data` so that sorted_words[0] is the most frequently appearing word and
    #       sorted_words[-1] is the least frequently appearing word.
    
        sorted_words = None
        sorted_freqlist, sorted_words = zip(*sorted(zip(freqlist, uniquewordlist), reverse=True))
    
        word_dict = {} # This is what we are building, a dictionary that translates words into integers
        for idx, word in enumerate(sorted_words[:vocab_size - 2]): # The -2 is so that we save room for the 'no word'
            word_dict[word] = idx + 2                              # 'infrequent' labels
        
        return word_dict, freqlist
        
    
    def extract_BoW_features(self, data_train, data_test, vocabulary_size=5000):
        """Method to Extract Bag-of-Words for a given set of documents, already preprocessed into words.
				
		Args:
			data_train (list): training data (text strings) stored as a list obtained using the preprocess_data() method
            data_test (list): test data (text strings) stored as a list obtained using the preprocess_data() method
            vocabulary_size (int): size of word vocabulary set. Default value = 5000
		
		Returns:
			features_train (list): output list of Bag of Words features function performed on training data
            features_test (list): output list of Bag of Words features function performed on test data
		"""
        
        # Fit a vectorizer to training documents and use it to transform them
        # NOTE: Training documents have already been preprocessed and tokenized into words;
        #       pass in dummy functions to skip those steps, e.g. preprocessor=lambda x: x
        vectorizer = CountVectorizer(max_features=vocabulary_size,
                preprocessor=lambda x: x, tokenizer=lambda x: x)  # already preprocessed
        features_train = vectorizer.fit_transform(words_train).toarray()

        # Apply the same vectorizer to transform the test documents (ignore unknown words)
        features_test = vectorizer.transform(words_test).toarray()
        
        # Return both the extracted features as well as the vocabulary
        return features_train, features_test, vocabulary
        
        
        