<h1 align="center">BIT MANUPULATION</h1>

### check number is odd or even

<pre>
any number can be made by the 1 2 4 8 64 ------
2<sup>i</sup> where i goes to 0 to n

if number is odd then last bit is 1 else it will be 0
so take and operation with 1
ex1:
11 -->  1 0 1 1
      & 0 0 0 1
    -------------
        0 0 0 1
             this is odd number
10 -->   1 0 1 0
       & 0 0 0 1
    ---------------
         0 0 0 0
             this number is even
</pre>

```python
def is_even(n):
  return n&1==0

```

### Remove last set bit or remove last 1 in a number

<pre>
example
11 -->  1 0 1 1
              ^
              this is last 1 so remove this and place 0
        1 0 1 0 ---> Answer
12 --> 1 1 0 0
         ^
         this is last 1 so replace with 0
       1 0 0 0
<b>How to solve this</b>
take And operation of number with number-1
ex:
11 --> 11 & (11-1)
       1 0 1 1
     & 1 0 1 0
  ---------------
       1 0 1 0   ---> Answer

12 --> 12&(12-1)
       1 1 0 0
     & 1 0 1 1
  --------------
       1 0 0 0  ---> Answer
</pre>

```python
def remove_last_set-bit(n):
  return n&(n-1)
```

### Count set bits or count 1 in a number

<pre>
Count 1 in a number

There are two method to solve this as i discussed above

<b>Method1</b>
Take And with 1
and right shift number with 1 position
repeat this process until number not become zero(0)
Example:
12 -->  1 1 0 0   >>1    0 1 1 0   >>1    0 0 1 1   >>1    0 0 0 1   >>1  0 0 0 0
      & 0 0 0 1        & 0 0 0 1        & 0 0 0 1        & 0 0 0 1        number become 0
    -------------     -----------      -----------      -----------
        0 0 0 0          0 0 0 0          0 0 0 1          0 0 0 1      ---> sum these result
    -------------     -----------      -----------      -----------
    12>>1 or (1 1 0 0 >> 1) ==  0 1 1 0

0000 --> 0
0001 --> 1
0+0+1+1=2 Answer     
</pre>

```python
def count_set_bit(n):
  count=0
  while n:
    count+=(n&1)
    n>>=1
  return count
```

<b>Method1</b>
remove last set bit as i discussed above
until number  not become

```python
def count_set_bit(n):
  count=0
  while n:
    n&=n-1
    count+=1
  return count
```
