# Text2Word package


Summary of the package
- Text pre-processing methods for nlp applications


performtext2word class
	Methods:
    1. review_to_words()
    	Method to clean a unit text using 'nltk'. For ex. a restaurant review.
        - removes html tags
        - converts all to lowercase
        - applies word stemming
        - splits text string into individual words
        - removes stopwords (words that do not affect sentiment of the text)
    2. preprocess_data()
    	Method to convert individual training and test text data into a list of cleaned.
        words using the 'review_to_words', collectively stored in a list 
    3. build_dict()
    	Method to Construct and return a dictionary mapping each of the most frequently appearing words to a unique integer. 
    4. extract_BoW_features()
    	Method to Extract Bag-of-Words for a given set of documents, already preprocessed into words. 
    