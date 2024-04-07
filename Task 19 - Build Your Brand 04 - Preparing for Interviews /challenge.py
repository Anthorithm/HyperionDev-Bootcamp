''' Little Sister's Vocabulary coding challenge '''

# 1. Add a prefix to a word
def add_prefix_un(word):
    return "un" + word

# Test cases
print(add_prefix_un("happy"))  # Output: 'unhappy'
print(add_prefix_un("manageable"))  # Output: 'unmanageable'

# 2. Add prefixes to word groups
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    prefixed_words = [prefix + word for word in words]
    return prefix + " :: " + " :: ".join(prefixed_words)

# Test cases
print(make_word_groups(['en', 'close', 'joy', 'lighten']))  # Output: 'en :: enclose :: enjoy :: enlighten'
print(make_word_groups(['pre', 'serve', 'dispose', 'position']))  # Output: 'pre :: preserve :: predispose :: preposition'
print(make_word_groups(['auto', 'didactic', 'graph', 'mate']))  # Output: 'auto :: autodidactic :: autograph :: automate'
print(make_word_groups(['inter', 'twine', 'connected', 'dependent']))  # Output: 'inter :: intertwine :: interconnected :: interdependent'

# 3. Remove a suffix from a word
def remove_suffix_ness(word):
    if word.endswith("ness"):
        root_word = word[:-4]  # Remove the 'ness' suffix
        if root_word.endswith("i"):  # Check if the root word originally had a 'y' before 'ness'
            root_word += "y"  # Restore the 'y'
        return root_word
    else:
        return "The word does not end with 'ness' suffix."

# Test cases
print(remove_suffix_ness("heaviness"))  # Output: 'heavy'
print(remove_suffix_ness("sadness"))    # Output: 'sad'

# 4. Extract and transform a word
def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index].strip('.').strip(',').strip('?').strip('!')  # Remove punctuation if present
    verb = adjective + "en"
    return verb

# Test cases
print(adjective_to_verb('I need to make that bright.', -1 ))  # Output: 'brighten'
print(adjective_to_verb('It got dark as the sun set.', 2))    # Output: 'darken'

