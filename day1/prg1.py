dictionary = {
    "serendipity": "The occurrence and development of events by chance in a happy or beneficial way.",
    "ephemeral": "Lasting for a very short time; transient or fleeting.",
    "resilience": "The ability to withstand or recover from difficult conditions or setbacks.",
    "voracious": "Having a very eager approach to an activity or pursuit; consuming or eager to consume large amounts of something.",
    "ubiquitous": "Present, appearing, or found everywhere.",
    "ephemeral": "Lasting for a very short time; transient or fleeting.",
    "paradox": "A statement or proposition that, despite sound reasoning from acceptable premises, leads to a conclusion that seems senseless, logically ,unacceptable, or self-contradictory.",
    "veracity": "Conformity to facts; accuracy; truthfulness.",
    "quixotic": "Exceedingly idealistic; unrealistic and impractical.",
    "nepotism": "The practice among those with power or influence of favoring relatives or friends, especially by giving them jobs.",
}

def find_definition(word):
    
    return dictionary.get(word, "Word not found in the dictionary.")

while True:
    print("")
    user_input = input("Enter a word to look up (x): ")
    
    if user_input.lower() == 'x':
        break
    
    definition = find_definition(user_input.lower())
    
    print(definition)