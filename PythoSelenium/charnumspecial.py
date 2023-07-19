def segregate_char_num_special(string):
    Chars=[]
    Nums=[]
    Specials=[]
    for char in string:
        if char.isalpha():
            Chars.append(char)
        elif char.isdigit():
            Nums.append(char)
        else:
            Specials.append(char)
    return Chars,Nums,Specials

input_string="welcome123!@#"
Char_list,Nums_list,Special_list=segregate_char_num_special(input_string)
print("Characters:",''.join(Char_list))
print("Numbers:",''.join(Nums_list))
print("Special Char:",''.join(Special_list))
