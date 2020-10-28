# ds4se
> Data Science for Software Engieering (ds4se) is an academic initiative to perform exploratory analysis on software engineering artifacts and metadata. Data Management, Analysis, and Benchmarking for DL and Traceability.


```python
pip install ds4se
```

    Requirement already satisfied: ds4se in c:\users\admin\desktop\fall2020\software engineering\project\github desktop\ds4se (0.0.7)
    Note: you may need to restart the kernel to use updated packages.
    

    WARNING: You are using pip version 20.2.3; however, version 20.2.4 is available.
    You should consider upgrading via the 'C:\Users\admin\anaconda3\python.exe -m pip install --upgrade pip' command.
    

This file will become your README and also the index of your documentation.

## Install

`pip install ds4se`

## How to use

```python
import ds4se.facade as facade
```

## Traceability

To use the ds4se library to calculate trace link value of proposed trace link with given.The function will takes in two strings for contents for source file and target file, feed two strings into a model that user specifies, and return traceability value.

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
facade.TraceLinkValue("source_string is a string of entire content of one source file","target_string is a string of entire content of one targetfile","word2vec")
```

    2020-10-27 23:03:35,138 : INFO : adding document #0 to Dictionary(0 unique tokens: [])
    2020-10-27 23:03:35,147 : INFO : built Dictionary(1815 unique tokens: ['@return', 'Converts', 'The', 'a', 'and']...) from 153 documents (total 5769 corpus positions)
    2020-10-27 23:03:35,147 : INFO : loading Word2Vec object from c:\users\admin\desktop\fall2020\software engineering\project\github desktop\ds4se\ds4se\model\[word2vec-Java-Py-SK-500-20E-128k-1594873397.267055].model
    2020-10-27 23:03:35,263 : INFO : loading wv recursively from c:\users\admin\desktop\fall2020\software engineering\project\github desktop\ds4se\ds4se\model\[word2vec-Java-Py-SK-500-20E-128k-1594873397.267055].model.wv.* with mmap=None
    2020-10-27 23:03:35,265 : INFO : loading vectors from c:\users\admin\desktop\fall2020\software engineering\project\github desktop\ds4se\ds4se\model\[word2vec-Java-Py-SK-500-20E-128k-1594873397.267055].model.wv.vectors.npy with mmap=None
    2020-10-27 23:03:35,295 : INFO : setting ignored attribute vectors_norm to None
    2020-10-27 23:03:35,296 : INFO : loading vocabulary recursively from c:\users\admin\desktop\fall2020\software engineering\project\github desktop\ds4se\ds4se\model\[word2vec-Java-Py-SK-500-20E-128k-1594873397.267055].model.vocabulary.* with mmap=None
    2020-10-27 23:03:35,298 : INFO : loading trainables recursively from c:\users\admin\desktop\fall2020\software engineering\project\github desktop\ds4se\ds4se\model\[word2vec-Java-Py-SK-500-20E-128k-1594873397.267055].model.trainables.* with mmap=None
    2020-10-27 23:03:35,299 : INFO : loading syn1neg from c:\users\admin\desktop\fall2020\software engineering\project\github desktop\ds4se\ds4se\model\[word2vec-Java-Py-SK-500-20E-128k-1594873397.267055].model.trainables.syn1neg.npy with mmap=None
    2020-10-27 23:03:35,330 : INFO : setting ignored attribute cum_table to None
    2020-10-27 23:03:35,331 : INFO : loaded c:\users\admin\desktop\fall2020\software engineering\project\github desktop\ds4se\ds4se\model\[word2vec-Java-Py-SK-500-20E-128k-1594873397.267055].model
    2020-10-27 23:03:35,402 : INFO : precomputing L2-norms of word weight vectors
    2020-10-27 23:03:35,454 : INFO : constructing a sparse term similarity matrix using <gensim.models.keyedvectors.WordEmbeddingSimilarityIndex object at 0x000001C608E797F0>
    2020-10-27 23:03:35,455 : INFO : iterating over columns in dictionary order
    2020-10-27 23:03:35,460 : INFO : PROGRESS: at 0.06% columns (1 / 1815, 0.055096% density, 0.055096% projected density)
    2020-10-27 23:03:37,412 : INFO : PROGRESS: at 55.15% columns (1001 / 1815, 0.347548% density, 0.585365% projected density)
    2020-10-27 23:03:38,271 : INFO : constructed a sparse term similarity matrix with 0.418460% density
    2020-10-27 23:03:38,290 : INFO : Removed 1 and 2 OOV words from document 1 and 2 (respectively).
    2020-10-27 23:03:38,292 : INFO : adding document #0 to Dictionary(0 unique tokens: [])
    2020-10-27 23:03:38,293 : INFO : built Dictionary(9 unique tokens: ['a', 'content', 'entire', 'file', 'is']...) from 2 documents (total 18 corpus positions)
    2020-10-27 23:03:38,305 : INFO : Computed distances or similarities ('source', 'target')[[0.25430019797963815, 0.7972573085858937]]
    




    (0.25430019797963815, 0.7972573085858937)



word2vec_metric is an optional parameter when using word2vec as technique, available metrics are: 
   <br> WMD
  <br>  SCM

## Analysis

This is the data analysis part of ds4se library, users can use the library to conduct analysis on artifacts with information theory and statistical analysis

For all functions in analysis part, input should be pandas dataframe with following structure

```python
d = {'contents': ["hello world", "this is a content of another file"]}
df = pd.DataFrame(data=d)
print(df)
```

                                contents
    0                        hello world
    1  this is a content of another file
    

### Usage of ds4se model to calculate the number of documents of either source or target class

    The method can process dataframes for artifacts contents and return the number of documents each artifacts class contains. 
    It takes in two parameters, a pandas dataframe for source artifacts and a pandas data frame for target artifacts, and it will do calculation for both classes.
    
    The method returns a list of 4 integers:
    1: number of documents for source artifacts;
    2: number of documents for target artifacts;
    3: source difference (difference between previous two results);
    4: target difference (same as above, but opposite sign).

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

    The method can process dataframes for artifacts contents and return the total number of vocab contained in each artifact class. 
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


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-17-0a0a1023f2fc> in <module>
    ----> 1 vocab_result = facade.VocabSize(source_df, target_df)
          2 source = vocab_result[0]
          3 target = vocab_result[1]
          4 difference_source = vocab_result[2]
          5 difference_target = vocab_result[3]
    

    NameError: name 'source_df' is not defined


### Usage of ds4se model to calculate the average number of token of either source or target class

    The method can process dataframes for artifacts contents and return the average number of tokens in each artifact class. 
    It does calculation by first finding the total number of token for each artifact class, and then divide each of them by the number of documents present in each artifacts.
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

    The method can process dataframes for artifacts contents and return the top three most frequent terms that appears in artifact class. It employs bpe model to precess the contents in each dataframe

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



If user only need the term frequency of one of two classes, they can choose to use Vocab() function, which is exactly the same except Vocab only processes one dataframe for one artifact class

```python
facade.Vocab(artifacts_df)
```




    {'est': [141, 0.141], 'http': [136, 0.136], 'frequnecy': [156, 0.156]}



### For Shared Metrics

Using the following metrics to compute using both source and target artifacts, use the following funtions. 

They all require two parameters: source and target artifacts. 

And return one integer value

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


