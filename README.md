# Control Flow Statements
A program’s control flow is the order in which the program’s code executes. The control flow of
a Python program is regulated by conditional statements, loops, and function calls. This section
covers the if statement and for and while loops; functions are covered later in this chapter.
raising and handling exceptions also affects control flow
* Python supports two type of control flow statement:

* 1> Conditional Statement
* 2>Looping Statement

### 1> Conditional Statement:

         Conditional statement are used to decide whether block as to execute or skip the execution 
         of the block......
* If
* Else
* Elif
<pre>

### If:-
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
Given no. is one digit no.</pre>

### Else:-
*          Else block should be preceeded by if block or else-if block or while block or for block.          
*          If else block preceeding block condition is returning false then only else block will be executed.

* Syntax:-
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




