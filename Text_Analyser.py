def sentence_frequency(file_name):
    with open(f'{file_name}.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        sentences = content.split(';')
        return [s.strip() for s in sentences if s.strip()]


def word_frequency(file_name):
    sentences = sentence_frequency(file_name)
    unflattened_words = [sentence.split(" ") for sentence in sentences]
    words = [word for group in unflattened_words for word in group]
    return [w for w in words if w]


def word_mean_length(file_name):
    words = word_frequency(file_name)
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)


def calculate_word_occurrence(words):
    occurrences = {}
    for word in words:
        occurrences[word] = occurrences.get(word, 0) + 1
    return occurrences


def most_used_words(file_name):
    words = word_frequency(file_name)
    occurrences = calculate_word_occurrence(words)
    if not occurrences:
        return []
    max_occ = max(occurrences.values())
    return [word for word, count in occurrences.items() if count == max_occ]


def less_used_words(file_name):
    words = word_frequency(file_name)
    occurrences = calculate_word_occurrence(words)
    if not occurrences:
        return []
    min_occ = min(occurrences.values())
    return [word for word, count in occurrences.items() if count == min_occ]


def palindrome_list(file_name):
    words = word_frequency(file_name)
    return [word for word in words if word == word[::-1]]


def words_per_sentence(file_name):
    sentences = sentence_frequency(file_name)
    return [(sentence, len(sentence.split())) for sentence in sentences]


def punctuation_types(file_name):
    with open(f'{file_name}.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        punctuations = sorted({char for char in text if not char.isalpha() and char not in [' ', '\n']})
    return punctuations


def analyze_text_file(file_name):
    print(f"\n=== Analyse du fichier '{file_name}.txt' ===\n")

    sentences = sentence_frequency(file_name)
    words = word_frequency(file_name)

    print(f"Nombre total de phrases : {len(sentences)}")
    print(f"Nombre total de mots : {len(words)}")
    print(f"Longueur moyenne des mots : {round(word_mean_length(file_name), 2)}\n")

    print(f"Mots les plus utilisés : {most_used_words(file_name)}")
    print(f"Mots les moins utilisés : {less_used_words(file_name)}")
    print(f"Mots palindromes : {palindrome_list(file_name)}\n")

    print("=== Longueur des phrases (en mots) ===")
    for sentence, count in words_per_sentence(file_name):
        print(f'"{sentence}" → {count} mots')

    print(f"\nPonctuations utilisées : {punctuation_types(file_name)}")




file_name = input("Donner le nom du fichier (sans .txt): ")
try:
    analyze_text_file(file_name)
except FileNotFoundError:
    print("Le fichier spécifié n'existe pas.")