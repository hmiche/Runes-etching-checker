import requests

def convert_to_words(number):
    # Define a dictionary mapping digits to their word representations
    digit_to_word = {
        '0': 'ZERO',
        '1': 'ONE',
        '2': 'TWO',
        '3': 'THREE',
        '4': 'FOUR',
        '5': 'FIVE',
        '6': 'SIX',
        '7': 'SEVEN',
        '8': 'EIGHT',
        '9': 'NINE'
    }
    
    # Convert each digit to its word representation
    word_representation = [digit_to_word[digit] for digit in str(number)]
    
    # Join the word representations with "•" between each word
    return '•'.join(word_representation)
    
def checkEndPoint(punkId):
    url = f"https://ordinals.com/rune/BIRD•{punkId}"
    response = requests.get(url)
    if not response:
        print(f"BIRD•{punkId}")

 
def main():
    punkId = ''
    for counter in range(5200,5500):
        punkId = convert_to_words(counter)
        checkEndPoint(punkId)

main()

