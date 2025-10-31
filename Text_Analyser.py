def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

def lexical_analysis(text):
    word_freq = {}
    for word in text.split():
        word = word.strip(",.?!;:(){}[]<>\"")
        if word.isalpha():
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    return word_freq

def analyze_statistics(word_freq):
    avg_length = 0
    most_used = []
    least_used = []
    palindromes = []
    max_freq = max(word_freq.values())
    min_freq = min(word_freq.values())
    for word, count in word_freq.items():
        if word == word[::-1]:
            palindromes.append(word)
        if count == max_freq:
            most_used.append(word)
        if count == min_freq:
            least_used.append(word)
        avg_length += count * len(word)
    avg_length /= sum(word_freq.values())
    return avg_length, most_used, least_used, palindromes

def analyze_sentences(text):
    sentences = text.split(".")
    punctuations = []
    for char in text:
        if not char.isalpha() and char != " " and char not in punctuations:
            punctuations.append(char)
    return sentences, punctuations

def top_frequent_words(word_freq, top_n=10):
    freq_values = sorted(set(word_freq.values()), reverse=True)
    top_words = []
    for val in freq_values[:top_n]:
        same_freq_words = [w for w, c in word_freq.items() if c == val]
        top_words.append(same_freq_words)
    return top_words

def sort_sentences_by_length(sentences):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(sentences) - 1):
            if len(sentences[i]) < len(sentences[i + 1]):
                sentences[i], sentences[i + 1] = sentences[i + 1], sentences[i]
                swapped = True
    return sentences


filename = input("Entrez le nom du fichier à analyser (ex: fichier.txt) : ")
text = read_file(filename)
word_freq = lexical_analysis(text)
avg_length, most_used, least_used, palindromes = analyze_statistics(word_freq)
sentences, punctuations = analyze_sentences(text)
top_words = top_frequent_words(word_freq)
sorted_sentences = sort_sentences_by_length(sentences)
print("\n--- ANALYSE LEXICALE ---")
print(word_freq)
print("Longueur moyenne des mots :", avg_length)
print("Mots les plus utilisés :", most_used)
print("Mots les moins utilisés :", least_used)
print("Mots palindromes :", palindromes)
print(f"Nombre de phrases : {len(sentences)}")
print("Ponctuations utilisées :", punctuations)
print("\nTop 10 des mots les plus fréquents :")
for i, group in enumerate(top_words, 1):
    print("-", i, group)
print("\nPhrases triées par longueur décroissante :")
for s in sorted_sentences:
    print(s.strip())