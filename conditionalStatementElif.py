print('Begin')
a=input("Enter Positive no.:")
b=int(a)
if b<10:
    print('Given no. is one Digit no.')
elif b<100:
    print('Given no. is two Digit no.')
elif b<1000:
    print('Given no. is three Digit no.')
else:
    print('Given no. is >= four Digit no.')
print('End')
