from datetime import datetime
from pathlib import Path
import re
import win32com.client
from testmarker_T3 import mark_test_T3
from sanitizefilename import sanitize_filename

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

for message in messages:
  # this block gets mail starting from a certain date
  # CHANGE start_date_string to only get emails from that point onwards
  start_date_string = '2023-09-01'
  start_date_number = datetime.strptime(start_date_string, '%Y-%m-%d')
  start_date_milliseconds = int(start_date_number.timestamp() * 1000)
  try:
    creation_time = message.CreationTime
    subject = message.Subject
    body = message.body
    # change text after 'if' to whichever level, book and test number you want
    if 'T3 Thinking Space A2 Test' in subject:
      test_email = body   
      new_time = creation_time.strftime("%Y-%b-%d")
      get_date = re.search(r'[0-9]{4}-[a-zA-Z]{3}-[0-9]+', new_time)
      match = get_date.group()
      for key in months_key.keys():
        if key in match:
          match = match.replace(key, str(months_key[key]))
          match_start_date_number = datetime.strptime(match, '%Y-%m-%d')    
          match_start_date_milliseconds = int(match_start_date_number.timestamp() * 1000)     
      if match_start_date_milliseconds > start_date_milliseconds:
        # this downloads the email into a .txt file and saves it in the Output folder
        sanitized_subject = sanitize_filename(subject)
        Path(output_dir / f'{sanitized_subject}.txt').write_text(str(body))

  except Exception as e:
    print(e)

tests = []
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
      file_path.close()
      file_path.unlink()

with open("testEmailData.js", "w", encoding='utf-8') as file:
    file.write("const testEmailData = " + sanitized_subject + ";\n")