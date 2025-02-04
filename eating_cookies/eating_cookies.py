#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache=None):
  
  if n < 0:
    return 0
  if n == 0:
    return 1
  if n == 1:
    return 1
  if n == 2:
    return 2
  return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)  

def eating_cookies(n, cache=None):

  cache = {}
  result = None

  if n in cache:
    return cache[n]

  if n < 0:
    result = 0

  if n == 0:
    result = 1

  if n == 1:
    result = 1

  if n == 2:
    result = 2

  if n > 2:
    result = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache) 
    cache[n] = result

  return result




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')