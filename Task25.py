# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def Find_and_del_str(source_txt, txt_for_find):
    split_txt = source_txt.split()
    result=""
    for i in split_txt:
        if find_text not in i:
            result+=(i+" ")
    return result

txt_str = ("adfghабвdgd67d gfdjабвkh67dds uigh47ty78 fh49ty9y tr94yt9абв7y")
print(f"\nИсходный текст: {txt_str}")
find_text = input ("Введите искомый элемент: ")

new_str = Find_and_del_str(txt_str, find_text)
print(f"Итоговый текст: {new_str}\n")