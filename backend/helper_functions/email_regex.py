import re
from unidecode import unidecode

string_to_test = unidecode("C1 CYCLE GOLD ADVANCED  Test 3 - Laia Miguel (Andy) (Andy Nicoll)")
get_level = re.search(r'[A-Z+][1-6*]|TPET', string_to_test) # works for every level!
get_type = re.search(r'Test\s[0-9]?|EXAM|LISTENING|WRITING', string_to_test) # works!   
get_type_string = str(get_type.group())  
get_type_string = get_type_string.replace('LISTENING', 'EXAM').replace('WRITING', 'EXAM').replace('Test', 'TEST')
get_student_name = re.search(r'-\s[a-zA-Z]+\s+[a-zA-Z]*', string_to_test) #works!
get_teacher_name = re.search(r'\(([^)]+)\)$', string_to_test)

# debug
""" print(get_level.group())
print(get_type_string)
print(get_student_name.group())
print(get_teacher_name.group().replace('(', '').replace(')', '')) """