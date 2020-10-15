# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/6.2_desc.metrics.main.ipynb (unless otherwise specified).

__all__ = ['get_unicode', 'add_mccabe_metrics', 'calculate_lcom5', 'add_lcom5', 'flatten_lol',
           'display_numeric_col_stats', 'display_numeric_col_hist']

# Cell
# Imports
import pandas as pd
from numpy import mean, std
from statistics import median
from scipy.stats import sem, t
import lizard
import matplotlib.pyplot as plt
from tree_sitter import Language, Parser, Node
#Decoding files
import chardet
from bs4 import UnicodeDammit


# TODO: Remove when mongo call is implemented
import os


from desc_metrics_parser_java import ParserJava
from desc_metrics_parser_cpp import ParserCPP
from desc_metrics_parser_python import ParserPython

# Cell
def get_unicode(file_path):
    """Detects file encoding and returns unicode. Inspired by http://reinvantveer.github.io/2017/05/19/unicode-dammit.html"""
    with open(file_path, 'rb') as f:
        detection = chardet.detect(f.read())

    enc = detection["encoding"]
    if detection["encoding"] == "ascii":
        with open(file_path, encoding="ascii") as f:
            data = f.read()
    elif detection["encoding"] == "ISO-8859-9":
        with open(file_path, encoding="utf-8") as f:
            enc = "utf-8"
            data = f.read()
    else:
        try:
            # Try to open as non unicode file
            with open(file_path, encoding=detection["encoding"]) as f:
                data = f.read()
        except Exception as e:
            raise ValueError(f"Cannot return dictionary from empty or invalid csv file {file_path} due to {e}")

    if not data:
        raise ValueError(f"Cannot return dictionary from empty or invalid csv file {file_path}")

    return UnicodeDammit(data).unicode_markup, enc

# Cell
def add_mccabe_metrics(df, data_col, name_col):
    """Adds information about function length and cyclomatic complexity for classes to a dataframe"""
    num_funcs = []
    class_ccn = []
    avg_func_ccn = []
    avg_func_nloc = []
    for i in range(len(df)):
        file_num_funcs = []
        file_class_ccn = []
        file_avg_func_ccn = []
        file_avg_func_nloc = []
        metrics = lizard.analyze_file.analyze_source_code(df[name_col][i], df[data_col][i])
        class_dict = {}
        for func in metrics.function_list:
            class_name = '::'.join(func.name.split("::")[:-1])
            if class_name in class_dict:
                class_dict[class_name].append(func)
            else:
                class_dict[class_name] = [func]
        for class_key in class_dict:
            total_class_ccn = 0
            total_class_nloc = 0
            for func in class_dict[class_key]:
                total_class_ccn += func.cyclomatic_complexity
                total_class_nloc += func.length
            file_num_funcs.append(len(class_dict[class_key]))
            file_class_ccn.append(total_class_ccn)
            file_avg_func_ccn.append(total_class_ccn/len(class_dict[class_key]))
            file_avg_func_nloc.append(total_class_nloc/len(class_dict[class_key]))

        num_funcs.append(file_num_funcs)
        class_ccn.append(file_class_ccn)
        avg_func_ccn.append(file_avg_func_ccn)
        avg_func_nloc.append(file_avg_func_nloc)

    df["num_funcs"] = num_funcs
    df["class_ccn"] = class_ccn
    df["avg_func_ccn"] = avg_func_ccn
    df["avg_func_nloc"] = avg_func_nloc
    return df

# Cell
def calculate_lcom5(tree, extension, file_bytes, name):
    """Parses the syntax tree of code to calculate the LCOM5 of its classes"""
    parser = lcom5_parser(extension)
    if not parser:
        return ["Undefined"]

    root_node = tree.root_node
    class_nodes = parser.find_class_nodes(root_node)
    class_method_names = []
    class_field_names = []
    class_dfc = [] # Distinct field calls, as per the definition of LCOM5
    for node in enumerate(class_nodes):
        class_method_names.append(parser.find_method_names(node[1], file_bytes))
        class_field_names.append(parser.find_field_names(node[1], class_method_names[node[0]], file_bytes))
        class_dfc.append(parser.distinct_field_calls(node[1], class_field_names[node[0]], file_bytes))
    lcom5_list = []
    for j in range(len(class_nodes)):
        num_fields = len(class_field_names[j])
        num_meths = len(class_method_names[j])
        num_dac = class_dfc[j]
        numerator = num_dac - (num_meths*num_fields)
        denominator = num_fields - (num_meths*num_fields)
        if denominator == 0:
            lcom5_list.append("Undefined")
        else:
            lcom5_list.append(numerator/denominator)
    return lcom5_list

# Cell
def add_lcom5(df, col):
    """Adds a column with the LCOM5 of each class of each file to a dataframe"""
    lang_builds = create_parser_builds()
    parser = Parser()
    class_lcom5 = []

    for i in range(len(df)):
        ext = df["name"][i].split('.')[-1]
        parser.set_language(lang_builds[ext])
        enc = df["encoding"][i]
        tree = parser.parse(bytes(df["contents"][i], df["encoding"][i]))
        class_lcom5.append(calculate_lcom5(tree, ext, bytes(df["contents"][i], df["encoding"][i]), df["name"][i]))
    df["class_lcom5"] = class_lcom5

    return df

# Cell
def flatten_lol(list_list):
    """Takes in a list of lists and flattens it, returning a list of each entry"""
    flattened_list = []
    for sublist in list_list:
        for entry in sublist:
            flattened_list.append(entry)
    return flattened_list

# Cell
def display_numeric_col_stats(col, conf = 0.95, sig_figs = 4, clean=True, verbose_clean=False):
    """Computes statistical metrics about the entries in a dataframe column or list"""
    previous_length = len(col)
    numeric_types = [int, float, complex]
    if clean: col = [x for x in col if type(x) in numeric_types]
    if verbose_clean: print(f"Cleaning removed {previous_length - len(col)} non-numeric entries")

    if len(col) < 1:
        print("Error, data must contain at least one valid entry to display statistics")
        return

    print("Min =", round(min(col), sig_figs))
    print("Max =", round(max(col), sig_figs))
    print("Average =", round(mean(col), sig_figs))
    print("Median =", round(median(col), sig_figs))
    print("Standard Deviation =", round(std(col), sig_figs))

    n = len(col)
    m = mean(col)
    std_err = sem(col)
    h = std_err * t.ppf((1 + conf) / 2, n - 1)

    start = m - h
    end = m + h
    print(f"{conf} of data points fall between {round(start, sig_figs)} and {round(end, sig_figs)}")

# Cell
def display_numeric_col_hist(col, col_name="Metric", num_bins=20, clean=True, verbose_clean=False):
    """Displays a histogram with a customized number of bins for the data in a specified dataframe column or list"""
    previous_length = len(col)
    numeric_types = [int, float, complex]
    if clean: col = [x for x in col if type(x) in numeric_types]
    if verbose_clean: print(f"Cleaning removed {previous_length - len(col)} non-numeric entries")

    if len(col) < 1:
        print("Error, data must contain at least one valid entry to display histogram")
        return

    rng = max(col) - min(col)
    num = len(col)
    stnd_dev = std(col)

    plt.hist(col, num_bins, color="blue", alpha=0.5, edgecolor="black", linewidth=1.0)
    plt.title(col_name + " Histogram")
    plt.ylabel("Value  Range  Occurrences")
    plt.xlabel(col_name)
    plt.show()