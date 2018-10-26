print('Begin')
a=input("Enter Positive no.:")
b=int(a)
if b<10:
    print('Given no. is one digit no.')
elif b<100:
    print('Given no. is two digit no.')
elif b<1000:
    print('Given no. is three digit no.')
else:
    print('Given no. is >= four digit no.')
print('End')
