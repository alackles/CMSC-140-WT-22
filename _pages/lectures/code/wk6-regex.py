import re

email_regex = r'[a-z]+\.[a-z]+@lawrence\.edu'
compiled_regex = re.compile(email_regex)
if re.match(email_regex, "acacia.ackles@lawrence.edu"):
    print("match found")
print(re.match(email_regex, "acacia.ackles@lawrence.edu"))