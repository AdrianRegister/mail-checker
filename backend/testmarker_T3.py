import re

# function to mark test
def mark_test_T3(test):
  correct_answers = 0
  lines = test.split('\n')
  for line in lines:
    for number in range(1, 11):
      if line.startswith(f'{number}.'):
        answer_finder = re.search(r'[ABCD]\s+[0-9\.]*\s*[abcd]', line)
        if answer_finder:
          answer_check = answer_finder.group()
          if answer_check[0].casefold() == answer_check[-1]:
            correct_answers += 1
  print(f'Total: {correct_answers}/10')
  
