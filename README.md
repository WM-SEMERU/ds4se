# ds4se
> Data Science for Software Engieering (ds4se) is an academic initiative to perform exploratory analysis on software engineering artifacts and metadata. Data Management, Analysis, and Benchmarking for DL and Traceability.


This file will become your README and also the index of your documentation.

## Install

`pip install ds4se`

## How to use

```python
import ds4se.facade as facade
```

## Traceability

To use the ds4se library to calculate trace link value of proposed trace link with given.

    Supported technique model:
        VSM
        LDA
        orthogonal 
        LSA
        JS
        word2vec
        doc2vec

The function returns a tuple of two integers, with the first element as distance between two artifacts and the second element be the similarity between two artifacts, which is the traceability value.

```python
facade.TraceLinkValue("source_string","target_string","LDA")
```




    0.01



word2vec_metric is an optional parameter when using word2vec as technique, available metrics are: 
   <br> WMD
  <br>  SCM

## Analysis

### Usage of ds4se model to calculate the number of documents of either source or target class

    The method takes in two parameters, a pandas dataframe for source artifacts and a pandas data frame for target artifacts, and it will do calculation for both classes.
    
    The method returns a list of 4 integers:
    1: number of documents for source artifacts;
    2: number of documents for target artifacts;
    3: source difference (difference between previous two results);
    4: target difference (same as above, but opposite).

```python
result = facade.NumDoc("source","target")
source_doc = result[0]
target_doc = result[1]
difference_source = result[2]
difference_target = result[3]
print("The number of documents for source is {} , with {} source difference".format(source_doc, difference_source))
print("The number of documents for target is {} , with {} target difference".format(target_doc, difference_target))
```

    The number of documents for source is 160 , with 32 source difference
    The number of documents for target is 128 , with -32 target difference
    

For all functions in analysis part, input should be pandas dataframe with following structure

```python
d = {'contents': ["hello world", "this is a content of another file"]}
df = pd.DataFrame(data=d)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>contents</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>hello world</td>
    </tr>
    <tr>
      <th>1</th>
      <td>this is a content of another file</td>
    </tr>
  </tbody>
</table>
</div>



### Usage of ds4se model to calculate the vocabulary size of either source or target class

    The method takes in two parameters, source artifacts and target artifacts, and it will do calculation for both classes.
    
    The method returns a list of 4 integers:
    1: vocabulary size for source artifacts;
    2: vocabulary size for target artifacts;
    3: source difference;
    4: target difference.

```python
vocab_result = facade.VocabSize(source_df, target_df)
source = vocab_result[0]
target = vocab_result[1]
difference_source = vocab_result[2]
difference_target = vocab_result[3]
print("The vocabulary size for source is {} , with {} target difference".format(source, difference_source))
print("The vocabulary size for target is {} , with {} target difference".format(target, difference_target))
```

    The vocabulary size for source is 179 , with 35 target difference
    The vocabulary size for target is 144 , with -35 target difference
    

### Usage of ds4se model to calculate the average number of token of either source or target class

    The method takes in two parameters, source artifacts and target artifacts, and it will do calculation for both classes.
    
    The method returns a list of 4 integers:
    1: average number of token for source artifacts;
    2: average number of token for target artifacts;
    3: source difference;
    4: target difference.

```python
token_result = facade.AverageToken(source_df, target_df)
source = token_result[0]
target = token_result[1]
difference_source = vocab_result[2]
difference_target = vocab_result[3]
print("The number of average token for source is {} , with {} source difference".format(source, difference_source))
print("The number of average token for target is {} , with {} target difference".format(target, difference_target))
```

    The number of average token for source is 107 , with 35 source difference
    The number of average token for target is 143 , with -35 target difference
    

### Usage of ds4se model to retriev term frequency

    The method takes in two parameters, 
    1: source artifacts,
    2: target artifacts, 
    and it will do calculation for both classes.
    
    The method returns a dictonary with 
    key: token
    value: a list of count and frequency

```python
facade.VocabShared(source_df,target_df)
```




    {'est': [160, 0.16], 'http': [136, 0.136], 'frequnecy': [124, 0.124]}



If we only need the term frequency of one of two classes, we can use Vocab() function

**The filename should be the path to the file**

```python
facade.Vocab(artifacts_df)
```




    {'est': [141, 0.141], 'http': [136, 0.136], 'frequnecy': [156, 0.156]}



### For Shared Metrics

Using the following metrics to compute using both source and target artifacts, use the following funtions. 

They all require two parameters: source and target artifacts. 

And return one int value

Shared vocabulary size

```python
facade.SharedVocabSize(source_df, target_df)
```




    112



Mutual information

```python
facade.MutualInformation(source_df, target_df)
```




    127



Corss Entropy

```python
facade.CrossEntropy(source_df, target_df)
```




    171



KL Divergence

```python
facade.KLDivergence(source_df, target_df)
```




    152


