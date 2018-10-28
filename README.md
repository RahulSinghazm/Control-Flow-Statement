# Control Flow Statements
A program’s control flow is the order in which the program’s code executes. The control flow of
a Python program is regulated by conditional statements, loops, and function calls. This section
covers the if statement and for and while loops; functions are covered later in this chapter.
raising and handling exceptions also affects control flow
* Python supports two type of control flow statement:

* 1> Conditional Statement
* 2>Looping Statement

## 1> Conditional Statement:

 Conditional statement are used to decide whether block as to execute or skip the execution 
 of the block......
* If
* Else
* Elif

## If:-
Condition return true it execute the block otherwise skip the execution of the block.
        
* Syntax:-
<pre>
          if condition: statement
          
          OR
          
          if condition:
          statement 1
          statement 2
          .
          .
          .
          .
          statement n
</pre>

#### Example:-
<pre>
print('Begin')
a=input('Enter the Positive no.:')
b=int(a)
if b<10:
    print('Given no. is one digit no.')

</pre>
#### Output:
<pre>
Begin
Enter the Positive no.:5
Given no. is one digit no.
</pre>

## Else:-
*          Else block should be preceeded by if block or else-if block or while block or for block.          
*          If else block preceeding block condition is returning false then only else block will be executed.

* Syntax:-
<pre>
          if condition: 
                    statement-1
                    statement-2
                    .
                    .
                    .
                    .
                    statement-n
          else:
                    statement-1
                    statement-2
                    .
                    .
                    .
                    .
                    .
                    statement-n
    </pre>      
#### Example:-
<pre>
print('Begin')
a=input('Enter positive no.:')
b=int(a)
if b<10:
    print('Given no. is one digit no.')
else:
    print('Given no. is >= two digit no.')
print('End')

</pre>

#### Output-1:
<pre>
Begin
Enter positive no.:9
Given no. is one digit no.
End
</pre>

#### Output-2:
<pre>
Begin
Enter positive no.:10
Given no. is >= two digit no.
End
</pre>


## Elif:-
*         Elif should be proceeded by either if block or another elif block.
*         Elif block proceeding block condition returns false the control will comes to elif block.
*         After contro; is reaching elif if elif block condition return true then only it will execute elif block.

#### Example:-
<pre>
print('Begin')
a=input("Enter positive no.:")
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

</pre>


#### Output-1:
<pre>
Begin
Enter positive no.:5
Given no. is one digit no.
End
</pre>

#### Output-2:
<pre>
Begin
Enter positive no.:22
Given no. is two digit no.
End
</pre>

#### Output-3:
<pre>
Begin
Enter positive no.:22
Given no. is two digit no.
End
</pre>



# Looping Statement:

Looping statements are used to execute set of statements repeatedly.
                  
* Python supports two looping statements they are........

#### a>While loop
#### b>For loop

## While loop:-
While loop executes set of statement repeatedly untile condition become false.
              
#### Syntax:
             while condtion:
                   statement-1
                   statement-2
                   .
                   .
                   .
                   statement-n
                   
#### Example:1
<pre>
                  print('Begin')
a=1
while a<=5:
    print('Rahul Singh')
    a=a+1
print('End')
</pre>


#### Output:


<pre>
Begin
Rahul Singh
Rahul Singh
Rahul Singh
Rahul Singh
Rahul Singh
End

</pre>

#### Example:2

<pre>
print('Begin')
a=1
sum=0
while a<=100:
    print('Rahul Singh')
    sum=sum+a
    a=a+1
    print(sum)
print('End')

</pre>


#### Output:

<pre>
Begin
Rahul Singh
1
Rahul Singh
3
Rahul Singh
6
Rahul Singh
10
Rahul Singh
15
Rahul Singh
21
Rahul Singh
28
Rahul Singh
36
Rahul Singh
45
Rahul Singh
55
Rahul Singh
66
Rahul Singh
78
Rahul Singh
91
Rahul Singh
105
Rahul Singh
120
Rahul Singh
136
Rahul Singh
153
Rahul Singh
171
Rahul Singh
190
Rahul Singh
210
Rahul Singh
231
Rahul Singh
253
Rahul Singh
276
Rahul Singh
300
Rahul Singh
325
Rahul Singh
351
Rahul Singh
378
Rahul Singh
406
Rahul Singh
435
Rahul Singh
465
Rahul Singh
496
Rahul Singh
528
Rahul Singh
561
Rahul Singh
595
Rahul Singh
630
Rahul Singh
666
Rahul Singh
703
Rahul Singh
741
Rahul Singh
780
Rahul Singh
820
Rahul Singh
861
Rahul Singh
903
Rahul Singh
946
Rahul Singh
990
Rahul Singh
1035
Rahul Singh
1081
Rahul Singh
1128
Rahul Singh
1176
Rahul Singh
1225
Rahul Singh
1275
Rahul Singh
1326
Rahul Singh
1378
Rahul Singh
1431
Rahul Singh
1485
Rahul Singh
1540
Rahul Singh
1596
Rahul Singh
1653
Rahul Singh
1711
Rahul Singh
1770
Rahul Singh
1830
Rahul Singh
1891
Rahul Singh
1953
Rahul Singh
2016
Rahul Singh
2080
Rahul Singh
2145
Rahul Singh
2211
Rahul Singh
2278
Rahul Singh
2346
Rahul Singh
2415
Rahul Singh
2485
Rahul Singh
2556
Rahul Singh
2628
Rahul Singh
2701
Rahul Singh
2775
Rahul Singh
2850
Rahul Singh
2926
Rahul Singh
3003
Rahul Singh
3081
Rahul Singh
3160
Rahul Singh
3240
Rahul Singh
3321
Rahul Singh
3403
Rahul Singh
3486
Rahul Singh
3570
Rahul Singh
3655
Rahul Singh
3741
Rahul Singh
3828
Rahul Singh
3916
Rahul Singh
4005
Rahul Singh
4095
Rahul Singh
4186
Rahul Singh
4278
Rahul Singh
4371
Rahul Singh
4465
Rahul Singh
4560
Rahul Singh
4656
Rahul Singh
4753
Rahul Singh
4851
Rahul Singh
4950
Rahul Singh
5050
End
</pre>

#### Example:3

<pre>
print('Begin')
a=1
while a<=5:
    print('Welcome')
    a=a+1
else:
    print('In while else')
print('End')

</pre>

#### Output:

<pre>
Begin
Welcome
Welcome
Welcome
Welcome
Welcome
In while else
End
</pre>

### Break:-

 Break is a statement, which can be used in looping statement. whenever control reach to the break 
 statements of loops then without executing the loop, control will comes out from the loop.
          
#### Example:1

<pre>
print('Begin')
a=1
while a<=5:
    print('Welcome')
    if a==2:
        break
    a=a+1
else:
    print('In while else')
print('End')

</pre>

#### Output:

<pre>
Begin
Welcome
Welcome
End
</pre>


#### Example:2

<pre>
print('Begin')
a=1
while True:
    print("Welcome")
    if a==4:
        break
    a=a+1
print('End')

</pre>

#### Output:

<pre>
Begin
Welcome
Welcome
Welcome
Welcome
End
</pre>

### Continue:
* Continue is a statements, which can be used in looping statements.
* Whenever control reach to the continue statements of the looping statement then without 
  executing the remaining partof iteration, control will go to the next iteration.

#### Example:1

<pre>
print('Begin')
a=0
while a<5:
    a=a+1
    if a==3:
        continue
    print('Welcome',a)
print('End')

</pre>

#### Output:

<pre>
Begin
Welcome 1
Welcome 2
Welcome 4
Welcome 5
End
</pre>

#### Example:2

<pre>
while True:
    name=input('Enter user name:')
    if name !='Rahul':
        continue
    password=input('Hello , Rahul. What is the password?')
    if password !='Singh':
        break
    print('Access Granted')

</pre>

#### Output:1

<pre>
Enter user name:Rohit
Enter the correct User Name
Enter user name:Rahul
Hello , Rahul. What is the password?Shyam
</pre>

#### Output:2

<pre>
Enter user name:Rahul
Hello , Rahul. What is the password?Singh
Access Granted
Enter user name:
</pre>
