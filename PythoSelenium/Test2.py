def reverse_string(input_string):
    words=input_string.split()
    reverse_word =[word[::-1] for word in words]
    reverse_string= ' '.join(reverse_word)
    return reverse_string

input_string="Hellow World"

reversed_string=reverse_string(input_string)

print(reversed_string)








