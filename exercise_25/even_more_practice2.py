# importing another py file
import even_more_practice

# storing a sentence in a variable called sentence 
sentence = 'All good things come to those who wait.'


words = even_more_practice.break_words(sentence)
words
sorted_words = even_more_practice.sort_words(words)
sorted_words
even_more_practice.print_first_word(words)
even_more_practice.print_last_word(words)
words
even_more_practice.print_first_word(sorted_words)
even_more_practice.print_last_word(sorted_words)
sorted_words
sorted_words = even_more_practice.sort_sentence(sentence)
sorted_words
even_more_practice.print_first_and_last(sentence)
even_more_practice.print_first_and_last_sentence_sorted(sentence)