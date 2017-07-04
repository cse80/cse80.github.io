---
---

cal
-------

`cal`  is used to _display_ the calendar of the current, past, and future month of any year. By default, it displays the month of the current month, current year.

~~~ bash
$ cal
     March 2016       
Su Mo Tu We Th Fr Sa  
       1  2  3  4  5  
 6  7  8  9 10 11 12  
13 14 15 16 17 18 19  
20 21 22 23 24 25 26  
27 28 29 30 31
~~~

<!--more-->

### Useful Options / Examples

#### `-m [MONTH]`
~~~ bash
$ cal -m 4
     April 2016       
Su Mo Tu We Th Fr Sa  
                1  2  
 3  4  5  6  7  8  9  
10 11 12 13 14 15 16  
17 18 19 20 21 22 23  
24 25 26 27 28 29 30 
~~~

##### Break it down

`-m [MONTH]` option takes in a month as input(in number), displays the calendar of the given input month of the current year.

-----------------------

#### `-y [YEAR]`
~~~ bash
$ cal -y 2016
                            2016
      January               February               March          
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  
                1  2      1  2  3  4  5  6         1  2  3  4  5  
 3  4  5  6  7  8  9   7  8  9 10 11 12 13   6  7  8  9 10 11 12  
10 11 12 13 14 15 16  14 15 16 17 18 19 20  13 14 15 16 17 18 19  
17 18 19 20 21 22 23  21 22 23 24 25 26 27  20 21 22 23 24 25 26  
24 25 26 27 28 29 30  28 29                 27 28 29 30 31        
31                                                                

       April                  May                   June          
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  
                1  2   1  2  3  4  5  6  7            1  2  3  4  
 3  4  5  6  7  8  9   8  9 10 11 12 13 14   5  6  7  8  9 10 11  
10 11 12 13 14 15 16  15 16 17 18 19 20 21  12 13 14 15 16 17 18  
17 18 19 20 21 22 23  22 23 24 25 26 27 28  19 20 21 22 23 24 25  
24 25 26 27 28 29 30  29 30 31              26 27 28 29 30        
                                                                  

        July                 August              September        
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  
                1  2      1  2  3  4  5  6               1  2  3  
 3  4  5  6  7  8  9   7  8  9 10 11 12 13   4  5  6  7  8  9 10  
10 11 12 13 14 15 16  14 15 16 17 18 19 20  11 12 13 14 15 16 17  
17 18 19 20 21 22 23  21 22 23 24 25 26 27  18 19 20 21 22 23 24  
24 25 26 27 28 29 30  28 29 30 31           25 26 27 28 29 30     
31                                                                

      October               November              December        
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  
                   1         1  2  3  4  5               1  2  3  
 2  3  4  5  6  7  8   6  7  8  9 10 11 12   4  5  6  7  8  9 10  
 9 10 11 12 13 14 15  13 14 15 16 17 18 19  11 12 13 14 15 16 17  
16 17 18 19 20 21 22  20 21 22 23 24 25 26  18 19 20 21 22 23 24  
23 24 25 26 27 28 29  27 28 29 30           25 26 27 28 29 30 31  
30 31                                                             
~~~

##### Break it down

`-y [YEAR]` option takes in a year as input, displays the calendar of all twelve months of the input year.

-----------------------

#### `-3`
~~~ bash
$ cal -3
   February 2016           March 2016            April 2016       
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  
    1  2  3  4  5  6         1  2  3  4  5                  1  2  
 7  8  9 10 11 12 13   6  7  8  9 10 11 12   3  4  5  6  7  8  9  
14 15 16 17 18 19 20  13 14 15 16 17 18 19  10 11 12 13 14 15 16  
21 22 23 24 25 26 27  20 21 22 23 24 25 26  17 18 19 20 21 22 23  
28 29                 27 28 29 30 31        24 25 26 27 28 29 30  
~~~

##### Break it down

`-3` option displays the calendar of previous, current, and next month surrounding today.
