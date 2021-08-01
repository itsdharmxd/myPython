sentence="my name is dharmesh and your name is lait and his name is buffelo"
sentence=sentence.replace(' is '," was ")
print(sentence)
place= sentence.find('was')
print(place)
place2=sentence.find('was',sentence.find('was')+1)
print(place2 )
place3=sentence.find('was',sentence.find('was',sentence.find('was')+1)+1)
print(place3)