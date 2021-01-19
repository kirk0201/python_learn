# 기본출력

print('Hello python!')
print("Hello python!")
print("""Hello python!""")
print('''Hello python!''')

print()

# seperator 옵션 사용

print('T','E','S','T', sep='')
print('2021', '01', '07', sep='-')
print('niceman','google.com', sep='@')

# end 옵션 사용
print('welcome To', end=' ')
print('the black parade', end='')
print('piano notes')

# format 사용 [], {}, ()
print('{} and {}'.format('you', 'me'))
print("{0} and {1} and {0}".format('you','me'))
print("{a} are {b}".format(a='you', b='me'))

#%s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" % ('Eunki', 7)) 

print("test1: %5d, price: %3.2f" %(776, 6543.123))

print("test1: {0:5d}, price:{1: 4.2f}".format(776, 6543.123))
print("test1: {a:5d}, price:{b: 4.2f}".format(a=776, b=6543.123))

# escape 코드
print("'print'")
print('\'you\'')
print('"me"')
print("""'you'""")
print('\\you\\\n')
print('\t\ttest')