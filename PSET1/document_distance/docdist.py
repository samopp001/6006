#!/usr/bin/python
import math, string

### implement the following three functions ###

def get_counts(sorted_data):
  # Problem 1-7 Part (a)
  counts = [(sorted_data[0],0)]
  for word in sorted_data:
    if counts[-1][0] == word:
      newC = counts[-1][1] + 1
      counts[-1] = (word, newC)
    else:
      counts.append((word,1))
  return counts

def get_inner_product(counts1, counts2):
  # Problem 1-7 Part (b)
  i = 0
  j = 0
  len1 = len(counts1)
  len2 = len(counts2)
  total = 0.0
  while i<len1 and j<len2:
    if counts1[i][0] > counts2[j][0]:
      j+=1
    elif counts1[i][0] < counts2[j][0]:
      i+= 1
    else:
      total += counts1[i][1]*counts2[j][1]
      j+=1
      i+=1
  return total
  # raise NotImplementedError()

def get_pairs(words):
  # Problem 1-7 Part (c)
  counts = []
  for i in range(len(words)-1):
    counts.append((words[i], words[i+1]))
  return counts
  #raise NotImplementedError()

### do no modify the following coding ###

translation_table =\
  string.maketrans(string.punctuation + string.uppercase,
                   " " * len(string.punctuation) + string.lowercase)

def main(path1, path2, use_pairs):
  theta = docdist(path1, path2, use_pairs)
  print "Angle between document vectors is %.3f radians.\n" % theta

def docdist(path1, path2, use_pairs):
  sorted_data1 = get_sorted_data(path1, use_pairs)
  sorted_data2 = get_sorted_data(path2, use_pairs)
  counts1 = get_counts(sorted_data1)
  counts2 = get_counts(sorted_data2)
  inner_product = get_inner_product(counts1, counts2)
  norm1 = get_inner_product(counts1, counts1)
  norm2 = get_inner_product(counts2, counts2)
  numerator = inner_product
  denominator = math.sqrt(norm1 * norm2)
  return math.acos(numerator / denominator)

def get_sorted_data(path, use_pairs):
  text = open(path).read()
  normalized_text = text.translate(translation_table)
  words = normalized_text.split()
  sorted_data = sorted(get_pairs(words) if use_pairs else words)
  return sorted_data


if __name__ == '__main__':
  import argparse, cProfile
  parser = argparse.ArgumentParser()
  parser.add_argument("--pairs", help="use pairs instead of words",
                      action="store_true")
  parser.add_argument("file1")
  parser.add_argument("file2")
  args = parser.parse_args()
  use_pairs = args.pairs
  cProfile.run("main(args.file1, args.file2, args.pairs)")
