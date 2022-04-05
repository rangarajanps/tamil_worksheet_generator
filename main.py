import random

desc = """
Choose one of the below option to generate the worksheet
1. Vary உயிர்
2. Vary மெய்
3. Vary both - Fixed order
4. Vary both - Random order \n
"""
choice = int(input(desc))
mei = ['க்','ங்','ச்','ஞ்','ட்','ண்','த்','ந்','ப்','ம்','ய்','ர்','ல்', 'வ்','ழ்','ள்','ற்','ன்']
uyir = [ 'அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ']

if choice == 1:
    mei_index = random.randint(1,len(mei))-1
    for i in range(0,len(uyir)):
        print(f'{mei[mei_index]} + {uyir[i]} = ')
elif choice == 2:
    uyir_index = random.randint(1, len(uyir)) - 1
    for i in range(0, len(mei)):
        print(f'{mei[i]} + {uyir[uyir_index]} = ')
elif choice == 3:
    uyir_index = 0
    for i in range(0, len(mei)):
        print(f'{mei[i]} + {uyir[uyir_index]} = ')
        uyir_index = (uyir_index + 1)%12
elif choice == 4:
    uyirs = random.sample(range(0, 12), 12) + random.sample(range(0, 12), 6)
    meis = random.sample(range(0, 18), 18)
    uyir_index = 0
    for i in range(0, len(meis)):
        print(f'{mei[i]} + {uyir[uyirs[uyir_index]]} = ')
        uyir_index = uyir_index + 1
