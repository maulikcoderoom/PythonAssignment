def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

input_sentence = "Hello, World! Welcome to Python programming."
output_sentence = reverse_sentence(input_sentence)
print("Input sentence:", input_sentence)
print("Output after reverse:", output_sentence)
