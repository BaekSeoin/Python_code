import sys

sys.stdin = open('input.txt','r')

dictionary = {'c=':'č', 'c-':'ć','dz=':'dž','d-':'đ','lj':'lj','nj':'nj','s=':'š','z=':'ž'}

sentence = [i for i in sys.stdin.readline().rstrip()]

length = len(sentence)

count = 0

index = 0

while index < length:

    word = sentence[index]

    try:
        x = dictionary[word]
        count +=1
        index+=1
    except:
        word = "".join(sentence[index:index+2])
        try:
            x = dictionary[word]
            count +=1
            index +=2
        except:

            word = "".join(sentence[index:index+3])
            try:
                x = dictionary[word]
                count+=1
                index += 3
            except:
                count +=1
                index+=1
print(count)


