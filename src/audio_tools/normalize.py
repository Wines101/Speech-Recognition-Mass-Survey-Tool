import string

def normalize(input_string):
    translator = str.maketrans('', '', string.punctuation)
    def process_char(char):
        if char.isalpha or char.isspace():
            return  char.translate(translator).lower()
        else:
            return ' '
    processed_chars = map(process_char, input_string)
    processed_string = ''.join(processed_chars)
    processed_string = ''.join(processed_string.split('\n'))
    processed_string = ''.join(processed_string.split('   '))
    processed_string = ' '.join(processed_string.split('\r'))

    return processed_string

if __name__ == "__main__":
    user_input = """Jolene, Jolene, Jolene, Jolene
    I'm beggin' of you, please don't take my man
    Jolene, Jolene, Jolene, Jolene
    Please don't take him just because you can
    Your beauty is beyond compare
    With flaming locks of auburn hair
    With ivory skin and eyes of emerald green
    Your smile is like a breath of spring
    Your voice is soft like summer rain
    And I cannot compete with you, Jolene
    He talks about you in his sleep
    And there's nothing I can do to keep
    From crying when he calls your name, Jolene
    And I can easily understand
    How you could easily take my man
    But you don't know what he means to me, Jolene
    Jolene, Jolene, Jolene, Jolene
    I'm begging of you, please don't take my man
    Jolene, Jolene, Jolene, Jolene
    Please don't take him just because you can
    You could have your choice of men
    But I could never love again
    He's the only one for me, Jolen
    I had to have this talk with you
    My happiness depends on you
    And whatever you decide to do, Jolene
    Jolene, Jolene, Jolene, Jolene
    I'm begging of you, please don't take my man
    Jolene, Jolene, Jolene, Jolene
    Please don't take him even though you can
    Jolene, Jolene"""
    
    print(normalize(user_input))