'''
                # Data Structures in Pandas : 
Pandas is an open-source library that uses for working with relational or labeled data both easily and intuitively.
It provides various data structures and operations for manipulating numerical data and time series. 
It offers a tool for cleaning and processes your data.
It is the most popular Python library that is used for data analysis. In this article, We are going to learn about Pandas Data structure.
'''

'''
                # Series
Pandas is a one-dimensional labeled array and capable of holding data of any type (integer, string, float, python objects, etc.)
Syntax: pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
'''

                # Example 1: Series holing the char data type.

import pandas as pd

# a simple char list
list = ['g', 'e', 'e', 'k', 's']
	
# create series form a char list
res = pd.Series(list)
print(res)

                  # Example 2: Series holding the Int data type.
                  
import pandas as pd

# a simple int list
list = [1,2,3,4,5]
	
# create series form a int list
res = pd.Series(list)
print(res)

##############################################################################################################################


                # Using the Pandas read_csv() and .to_csv() Functions : 
                
    # Write a CSV File
    >>> df.to_csv('data.csv')
      
    # Read a CSV File
    >>> df = pd.read_csv('data.csv', index_col=0)
    >>> df    
           
                # Using Pandas to Write and Read Excel Files : 
                
    # Write an Excel File : 
    >>> df.to_excel('data.xlsx')
          
   # Read an Excel File : 
   >>> df = pd.read_excel('data.xlsx', index_col=0)
   >>> df
   
       COUNTRY      POP      AREA       GDP       CONT     IND_DAY
CHN       China  1398.72   9596.96  12234.78       Asia         NaN
IND       India  1351.16   3287.26   2575.67       Asia  1947-08-15
USA          US   329.74   9833.52  19485.39  N.America  1776-07-04
IDN   Indonesia   268.07   1910.93   1015.54       Asia  1945-08-17
BRA      Brazil   210.32   8515.77   2055.51  S.America  1822-09-07
PAK    Pakistan   205.71    881.91    302.14       Asia  1947-08-14
NGA     Nigeria   200.96    923.77    375.77     Africa  1960-10-01
BGD  Bangladesh   167.09    147.57    245.63       Asia  1971-03-26
RUS      Russia   146.79  17098.25   1530.75        NaN  1992-06-12
MEX      Mexico   126.58   1964.38   1158.23  N.America  1810-09-16
JPN       Japan   126.22    377.97   4872.42       Asia         NaN
DEU     Germany    83.02    357.11   3693.20     Europe         NaN
FRA      France    67.02    640.68   2582.49     Europe  1789-07-14
GBR          UK    66.44    242.50   2631.23     Europe         NaN
ITA       Italy    60.36    301.34   1943.84     Europe         NaN
ARG   Argentina    44.94   2780.40    637.49  S.America  1816-07-09
DZA     Algeria    43.38   2381.74    167.56     Africa  1962-07-05
CAN      Canada    37.59   9984.67   1647.12  N.America  1867-07-01
AUS   Australia    25.47   7692.02   1408.68    Oceania         NaN
KAZ  Kazakhstan    18.53   2724.90    159.41       Asia  1991-12-16

###################################################################################################################################

'''
                # Indexing and selecting data
The axis labeling information in pandas objects serves many purposes:

Identifies data (i.e. provides metadata) using known indicators, important for analysis, visualization, and interactive console display.
Enables automatic and explicit data alignment.
Allows intuitive getting and setting of subsets of the data set.
'''

                # Different choices for indexing : 

In : dates = pd.date_range('1/1/2000', periods=8)

In : df = pd.DataFrame(np.random.randn(8, 4),
   ...:                   index=dates, columns=['A', 'B', 'C', 'D'])
   ...: 

In : df
Out : 
                   A         B         C         D
2000-01-01  0.469112 -0.282863 -1.509059 -1.135632
2000-01-02  1.212112 -0.173215  0.119209 -1.044236
2000-01-03 -0.861849 -2.104569 -0.494929  1.071804
2000-01-04  0.721555 -0.706771 -1.039575  0.271860
2000-01-05 -0.424972  0.567020  0.276232 -1.087401
2000-01-06 -0.673690  0.113648 -1.478427  0.524988
2000-01-07  0.404705  0.577046 -1.715002 -1.039268
2000-01-08 -0.370647 -1.157892 -1.344312  0.844885

                    
                    # Slicing ranges : 
                   
In : s[:5]
Out : 
2000-01-01    0.469112
2000-01-02    1.212112
2000-01-03   -0.861849
2000-01-04    0.721555
2000-01-05   -0.424972
Freq: D, Name: A, dtype: float64

In : s[::2]
Out : 
2000-01-01    0.469112
2000-01-03   -0.861849
2000-01-05   -0.424972
2000-01-07    0.404705
Freq: 2D, Name: A, dtype: float64

In : s[::-1]
Out : 
2000-01-08   -0.370647
2000-01-07    0.404705
2000-01-06   -0.673690
2000-01-05   -0.424972
2000-01-04    0.721555
2000-01-03   -0.861849
2000-01-02    1.212112
2000-01-01    0.469112
Freq: -1D, Name: A, dtype: float64


                # Selection by label : 
                
In : s1 = pd.Series(np.random.randn(6), index=list('abcdef'))

In : s1
Out : 
a    1.431256
b    1.340309
c   -1.170299
d   -0.226169
e    0.410835
f    0.813850
dtype: float64

In : s1.loc['c':]
Out : 
c   -1.170299
d   -0.226169
e    0.410835
f    0.813850
dtype: float64

In : s1.loc['b']

Out : 1.3403088497993827

 # Note that setting works as well:

In : s1.loc['c':] = 0

In : s1
Out : 
a    1.431256
b    1.340309
c    0.000000
d    0.000000
e    0.000000
f    0.000000
dtype: float64

#######################################################################################################################################
'''
                # Pythonic Data Cleaning With Pandas and NumPy : 
               
It is an important part of a data scientist's job to handle messy data including missing values, inconsistent formatting, and data types.
The process of data cleaning is roughly covered in the following steps: Dropping irrelevant columns. 
Renaming column names to meaningful names.
'''             

                # Dropping Columns in a DataFrame : 
                
          >>> df = pd.read_csv('Datasets/BL-Flickr-Images-Book.csv')
          >>> df.head()

    Identifier             Edition Statement      Place of Publication  \
0         206                           NaN                    London
1         216                           NaN  London; Virtue & Yorston
2         218                           NaN                    London
3         472                           NaN                    London
4         480  A new edition, revised, etc.                    London

  Date of Publication              Publisher  \
0         1879 [1878]       S. Tinsley & Co.
1                1868           Virtue & Co.
2                1869  Bradbury, Evans & Co.
3                1851          James Darling
4                1857   Wertheim & Macintosh

                                               Title     Author  \
0                  Walter Forbes. [A novel.] By A. A      A. A.
1  All for Greed. [A novel. The dedication signed...  A., A. A.
2  Love the Avenger. By the author of “All for Gr...  A., A. A.
3  Welsh Sketches, chiefly ecclesiastical, to the...  A., E. S.
4  [The World in which I live, and my place in it...  A., E. S.

                                   Contributors  Corporate Author  \
0                               FORBES, Walter.               NaN
1  BLAZE DE BURY, Marie Pauline Rose - Baroness               NaN
2  BLAZE DE BURY, Marie Pauline Rose - Baroness               NaN
3                   Appleyard, Ernest Silvanus.               NaN
4                           BROOME, John Henry.               NaN

   Corporate Contributors Former owner  Engraver Issuance type  \
0                     NaN          NaN       NaN   monographic
1                     NaN          NaN       NaN   monographic
2                     NaN          NaN       NaN   monographic
3                     NaN          NaN       NaN   monographic
4                     NaN          NaN       NaN   monographic

                                          Flickr URL  \
0  http://www.flickr.com/photos/britishlibrary/ta...
1  http://www.flickr.com/photos/britishlibrary/ta...
2  http://www.flickr.com/photos/britishlibrary/ta...
3  http://www.flickr.com/photos/britishlibrary/ta...
4  http://www.flickr.com/photos/britishlibrary/ta...

                            Shelfmarks
0    British Library HMNTS 12641.b.30.
1    British Library HMNTS 12626.cc.2.
2    British Library HMNTS 12625.dd.1.
3    British Library HMNTS 10369.bbb.15.
4    British Library HMNTS 9007.d.28.

        #  We can drop these columns in the following way:

>>> to_drop = ['Edition Statement',
...            'Corporate Author',
...            'Corporate Contributors',
...            'Former owner',
...            'Engraver',
...            'Contributors',
...            'Issuance type',
...            'Shelfmarks']

>>> df.drop(to_drop, inplace=True, axis=1)


                #  When we inspect the DataFrame again, we’ll see that the unwanted columns have been removed:

>>> df.head()
   Identifier      Place of Publication Date of Publication  \
0         206                    London         1879 [1878]
1         216  London; Virtue & Yorston                1868
2         218                    London                1869
3         472                    London                1851
4         480                    London                1857

               Publisher                                              Title  \
0       S. Tinsley & Co.                  Walter Forbes. [A novel.] By A. A
1           Virtue & Co.  All for Greed. [A novel. The dedication signed...
2  Bradbury, Evans & Co.  Love the Avenger. By the author of “All for Gr...
3          James Darling  Welsh Sketches, chiefly ecclesiastical, to the...
4   Wertheim & Macintosh  [The World in which I live, and my place in it...

      Author                                         Flickr URL
0      A. A.  http://www.flickr.com/photos/britishlibrary/ta...
1  A., A. A.  http://www.flickr.com/photos/britishlibrary/ta...
2  A., A. A.  http://www.flickr.com/photos/britishlibrary/ta...
3  A., E. S.  http://www.flickr.com/photos/britishlibrary/ta...
4  A., E. S.  http://www.flickr.com/photos/britishlibrary/ta...

###########################################################################################################################################

                    # Applying Aggregations on DataFrame : 
                    
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])

print df

r = df.rolling(window=3,min_periods=1)
print r

        # output : 
                    A           B           C           D
2000-01-01   1.088512   -0.650942   -2.547450   -0.566858
2000-01-02   0.790670   -0.387854   -0.668132    0.267283
2000-01-03  -0.575523   -0.965025    0.060427   -2.179780
2000-01-04   1.669653    1.211759   -0.254695    1.429166
2000-01-05   0.100568   -0.236184    0.491646   -0.466081
2000-01-06   0.155172    0.992975   -1.205134    0.320958
2000-01-07   0.309468   -0.724053   -1.412446    0.627919
2000-01-08   0.099489   -1.028040    0.163206   -1.274331
2000-01-09   1.639500   -0.068443    0.714008   -0.565969
2000-01-10   0.326761    1.479841    0.664282   -1.361169

Rolling [window=3,min_periods=1,center=False,axis=0]    

                # Apply Aggregation on a Whole Dataframe
                
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print df

r = df.rolling(window=3,min_periods=1)
print r.aggregate(np.sum)

        # Output : 
                    A           B           C           D
2000-01-01   1.088512   -0.650942   -2.547450   -0.566858
2000-01-02   1.879182   -1.038796   -3.215581   -0.299575
2000-01-03   1.303660   -2.003821   -3.155154   -2.479355
2000-01-04   1.884801   -0.141119   -0.862400   -0.483331
2000-01-05   1.194699    0.010551    0.297378   -1.216695
2000-01-06   1.925393    1.968551   -0.968183    1.284044
2000-01-07   0.565208    0.032738   -2.125934    0.482797
2000-01-08   0.564129   -0.759118   -2.454374   -0.325454
2000-01-0
9   2.048458   -1.820537   -0.535232   -1.212381
2000-01-10   2.065750    0.383357    1.541496   -3.201469

                    A           B           C           D
2000-01-01   1.088512   -0.650942   -2.547450   -0.566858
2000-01-02   1.879182   -1.038796   -3.215581   -0.299575
2000-01-03   1.303660   -2.003821   -3.155154   -2.479355
2000-01-04   1.884801   -0.141119   -0.862400   -0.483331
2000-01-05   1.194699    0.010551    0.297378   -1.216695
2000-01-06   1.925393    1.968551   -0.968183    1.284044
2000-01-07   0.565208    0.032738   -2.125934    0.482797
2000-01-08   0.564129   -0.759118   -2.454374   -0.325454
2000-01-09   2.048458   -1.820537   -0.535232   -1.212381
2000-01-10   2.065750    0.383357    1.541496   -3.201469


                    
                    # Apply Aggregation on Multiple Columns of a DataFrame
                    
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print df
r = df.rolling(window=3,min_periods=1)
print r[['A','B']].aggregate(np.sum)

Output : 

                 A           B           C           D
2000-01-01   1.088512   -0.650942   -2.547450   -0.566858
2000-01-02   1.879182   -1.038796   -3.215581   -0.299575
2000-01-03   1.303660   -2.003821   -3.155154   -2.479355
2000-01-04   1.884801   -0.141119   -0.862400   -0.483331
2000-01-05   1.194699    0.010551    0.297378   -1.216695
2000-01-06   1.925393    1.968551   -0.968183    1.284044
2000-01-07   0.565208    0.032738   -2.125934    0.482797
2000-01-08   0.564129   -0.759118   -2.454374   -0.325454
2000-01-09   2.048458   -1.820537   -0.535232   -1.212381
2000-01-10   2.065750    0.383357    1.541496   -3.201469
                    A           B
2000-01-01   1.088512   -0.650942
2000-01-02   1.879182   -1.038796
2000-01-03   1.303660   -2.003821
2000-01-04   1.884801   -0.141119
2000-01-05   1.194699    0.010551Let us now create two different DataFrames and perform the merging operations on it.

Live Demo
# import the pandas library
import pandas as pd
left = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
   {'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print left
print right
Its output is as follows −

    Name  id   subject_id
0   Alex   1         sub1
1    Amy   2         sub2
2  Allen   3         sub4
3  Alice   4         sub6
4  Ayoung  5         sub5

    Name  id   subject_id
0  Billy   1         sub2
1  Brian   2         sub4
2  Bran    3         sub3
3  Bryce   4         sub6
4  Betty   5         sub5

2000-01-06   1.925393    1.968551
2000-01-07   0.565208    0.032738
2000-01-08   0.564129   -0.759118
2000-01-09   2.048458   -1.820537
2000-01-10   2.065750    0.383357

############################################################################################################################################

                    # Python Pandas - Merging/Joining : 

Pandas has full-featured, high performance in-memory join operations idiomatically very similar to relational databases like SQL.

Create two different DataFrames and perform the merging operations on it : 

# import the pandas library
import pandas as pd
left = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
   {'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print left
print right
Its output is as follows −

    Name  id   subject_id
0   Alex   1         sub1
1    Amy   2         sub2
2  Allen   3         sub4
3  Alice   4         sub6
4  Ayoung  5         sub5

    Name  id   subject_id
0  Billy   1         sub2
1  Brian   2         sub4
2  Bran    3         sub3
3  Bryce   4         sub6
4  Betty   5         sub5


                    # Merge Two DataFrames on a Key : 

import pandas as pd
left = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame({
	'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print pd.merge(left,right,on='id')
Its output is as follows −

   Name_x   id  subject_id_x   Name_y   subject_id_y
0  Alex      1          sub1    Billy           sub2
1  Amy       2          sub2    Brian           sub4
2  Allen     3          sub4     Bran           sub3
3  Alice     4          sub6    Bryce           sub6
4  Ayoung    5          sub5    Betty           sub5

                
                # Merge Two DataFrames on Multiple Keys : 

import pandas as pd
left = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame({
	'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print pd.merge(left,right,on=['id','subject_id'])
Its output is as follows −

    Name_x   id   subject_id   Name_y
0    Alice    4         sub6    Bryce
1   Ayoung    5         sub5    Betty


