# Initialize a list variable with 100 words suitable for a hangman game
words_list = [
    'apple', 'banana', 'cherry', 'date', 'elderberry',
    'fig', 'grape', 'honeydew', 'iceberg', 'jujube',
    'kiwi', 'lemon', 'mango', 'nectarine', 'orange',
    'papaya', 'quince', 'raspberry', 'strawberry', 'tomato',
    'avocado', 'blueberry', 'cranberry', 'durian', 'elderflower',
    'feijoa', 'gooseberry', 'huckleberry', 'imbue', 'sabbatical',
    'kumquat', 'lychee', 'mulberry', 'nutmeg', 'olive',
    'pomegranate', 'quango', 'raisin', 'tangerine',
    'bilberry', 'boysenberry', 'currant', 'dewberry', 'awaken',
    'finger', 'grapefruit', 'hack', 'lama', 'jackfruit',
    'long', 'pedlar', 'noni', 'optician', 'prickly',
    'quarantine', 'rambutan', 'soursop', 'tamarind',
    'blackberry', 'buffalo', 'damson', 'elder', 'figleaf',
    'guava', 'hawthorn', 'sabbatical', 'pineapple', 'loganberry',
    'maypole', 'nance', 'relator', 'siting', 'quartile',
    'riberry', 'sarsaparilla', 'uglifier',
    'bloodline', 'calamining', 'dragonfruit', 'egg', 'huckleberry',
    'genie', 'plum', 'ital', 'jambalaya', 'loquat',
    'mulberry', 'northern', 'gooseberry', 'pique', 'quarantine',
    'rowan', 'spite', 'white',
    'factoid', 'rangefinders', 'huckleberry', 'bilberry',
    'wine'
]
# Create a list of English letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
