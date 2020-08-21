#2a
def to_camel_case(text):
    return ''.join([t[0].upper()+  t[1:] for t in text.lower().split()])

test = ['SdS ssd JOQERH', 'hello world', 'My sRriNg', 'tHis Is A tesT string']
testb = []
for t in test:
    print(to_camel_case(t))
    testb.append(to_camel_case(t))

print('######2B#########')
# #2b
import re
def to_snake_case(text):
    if(re.search(r'\s', text) != []):
        return '_'.join(re.findall(r"[A-Z][a-z]*", text)).lower()    
    raise Exception("wrong format dude! Try again")
       
for t in testb:
    print(to_snake_case(t))