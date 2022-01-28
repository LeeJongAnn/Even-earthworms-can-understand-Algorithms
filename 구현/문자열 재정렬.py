import sys
import time
start = time.time()
sys.stdin = open("in13.txt",'rt')
data = input()
print(data)
int_result = 0
string_result = []
for x in data:
    if x.isalpha():
        string_result.append(x)
    else:
        int_result +=int(x)
string_result.sort()
if int_result != 0:
    string_result.append(str(int_result))
print(''.join(string_result))