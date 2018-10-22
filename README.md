# Control Flow Statements
A program’s control flow is the order in which the program’s code executes. The control flow of
a Python program is regulated by conditional statements, loops, and function calls. This section
covers the if statement and for and while loops; functions are covered later in this chapter.
Raising and handling exceptions also affects control flow
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
* Syntax:
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
Condition return true it execute the block otherwise skip the execution of the block.
#### Example:
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
