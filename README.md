# ds4se
> Data Science for Software Engieering (ds4se) is an academic initiative to perform exploratory analysis on software engineering artifacts and metadata. Data Management, Analysis, and Benchmarking for DL and Traceability.


This file will become your README and also the index of your documentation.

## Install

`pip install ds4se`

## How to use

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

```python
facade.TraceLinkValue("source_string","target_string","techinque")
```




    0.73



## Analysis

### Usage of ds4se model to calculate the number of documents of either source or target class

    The method takes in two parameters, source artifacts and target artifacts, and it will do calculation for both classes.
    
    The method returns a list of 4 integers:
    1: number of documents for source artifacts;
    2: number of documents for target artifacts;
    3: source difference;
    4: target difference.

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
    

### Usage of ds4se model to calculate the vocabulary size of either source or target class

    The method takes in two parameters, source artifacts and target artifacts, and it will do calculation for both classes.
    
    The method returns a list of 4 integers:
    1: vocabulary size for source artifacts;
    2: vocabulary size for target artifacts;
    3: source difference;
    4: target difference.

```python
vocab_result = facade.VocabSize("source", "target")
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
token_result = facade.AverageToken("source", "target")
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
facade.VocabShared("source","target")
```




    {'est': [160, 0.16], 'http': [136, 0.136], 'frequnecy': [124, 0.124]}



If we only need the term frequency of one of two classes, we can use Vocab() function

**The filename should be the path to the file**

```python
facade.Vocab("filename")
```




    {'est': [141, 0.141], 'http': [136, 0.136], 'frequnecy': [156, 0.156]}



### For Shared Metrics

Using the following metrics to compute using both source and target artifacts, use the following funtions. 

They all require two parameters: source and target artifacts. 

And return one int value

Shared vocabulary size

```python
facade.SharedVocabSize("source", "target")
```




    112



Mutual information

```python
facade.MutualInformation("source", "target")
```




    127



Corss Entropy

```python
facade.CrossEntropy("source", "target")
```




    171



KL Divergence

```python
facade.KLDivergence("source", "target")
```




    152


