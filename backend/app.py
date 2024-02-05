from datetime import datetime
from pathlib import Path
import re
import win32com.client
from helper_functions.testmarkers import mark_test_T3, mark_test_TPET
from helper_functions.sanitizefilename import sanitize_filename
from unidecode import unidecode
import json

output_dir = Path.cwd() / 'Output'
output_dir.mkdir(parents=True, exist_ok=True)

outlook = win32com.client.Dispatch('Outlook.Application').GetNamespace('MAPI')
inbox = outlook.Folders('testandexamresults2@cambridgeschool.com').Folders('Bandeja de entrada')

messages = inbox.Items

months_key = {
  'Jan': 1,
  'Feb': 2,
  'Mar': 3,
  'Apr': 4,
  'May': 5,
  'Jun': 6,
  'Jul': 7,
  'Aug': 8,
  'Sep': 9,
  'Oct': 10,
  'Nov': 11,
  'Dec': 12
}
sanitized_subject = ''
# this block gets mail starting from a certain date
# CHANGE start_date_string to only get emails from that point onwards
start_date_string = '2023-09-01'
start_date_number = datetime.strptime(start_date_string, '%Y-%m-%d')
start_date_milliseconds = int(start_date_number.timestamp() * 1000)

# put test emails as dict into this list
tests = []

for message in messages:
  try:
    creation_time = message.CreationTime
    subject = message.Subject
    body = message.body
    # change text after 'if' to whichever level, book and test number you want
    if 'T3 Thinking Space A2 Test' in subject:
      new_time = creation_time.strftime("%Y-%b-%d")
      get_date = re.search(r'[0-9]{4}-[a-zA-Z]{3}-[0-9]+', new_time)
      match = get_date.group()
      for key in months_key.keys():
        if key in match:
          match = match.replace(key, str(months_key[key]))
          match_start_date_number = datetime.strptime(match, '%Y-%m-%d')    
          match_start_date_milliseconds = int(match_start_date_number.timestamp() * 1000)     
      if match_start_date_milliseconds > start_date_milliseconds:
        # regex to get all email info from subject line
        get_level = re.search(r'[A-Z+][1-6*]|TPET', subject) # works for every level!
        get_type = re.search(r'Test\s[0-9]?|EXAM|LISTENING|WRITING', subject) # works!   
        get_type_string = str(get_type.group())  
        get_type_string = get_type_string.replace('LISTENING', 'EXAM').replace('WRITING', 'EXAM').replace('Test', 'TEST')
        get_student_name = re.search(r'-\s[a-zA-Z]+\s+[a-zA-Z]*', subject) #works!
        if str(get_student_name.group()).startswith('- '):
          get_student_name_string = str(get_student_name.group()).replace('- ', '')
        get_teacher_name = re.search(r'\(([^)]+)\)$', subject)
        # this puts all email content into a dict, which is then placed into the tests list
        email_test = {
          'Level': get_level.group(),
          'Type': get_type_string,
          'Student Name': get_student_name_string,
          'Teacher Name': get_teacher_name.group().replace('(', '').replace(')', '')
        }
        tests.append(email_test)
        # this downloads the email into a .txt file and saves it in the Output folder
        sanitized_subject = sanitize_filename(subject)
        Path(output_dir / f'{sanitized_subject}.txt').write_text(str(body))
      else:
        break  

  except Exception as e:
    print(e)

formatted_tests_data = json.dumps(tests, indent=2)
print(formatted_tests_data)

with open("testEmailData.js", "w", encoding='utf-8') as file:
    file.write("export const testEmailData = " + formatted_tests_data)


# GO BACK TO THIS LATER
""" tests = []
# this goes through the Output folder and marks the tests 
folder_path = Path('./Output')
for file_path in folder_path.glob("*.txt"):
  with file_path.open("r") as file:
    if 'T3' in str(file_path):
      tests.append(file_path)
      file_content = file.read()
      print(f"File: {file_path}")
      # change this function to mark other tests. function(file_content)
      mark_test_T3(file_content) 
      file.close()
      file_path.unlink()
 """
