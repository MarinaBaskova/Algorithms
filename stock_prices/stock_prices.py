#!/usr/bin/python

import argparse

def find_max_profit(prices):

    max_profit_so_far = prices[1] - prices[0]
    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > max_profit_so_far:
                max_profit_so_far = prices[j] - prices[i]

    return max_profit_so_far

def find_max_profit(prices):

  max_profit_so_far = []
  for i in range(0, len(prices)):
      for j in range(i+1, len(prices)):
          max_profit_so_far.append(prices[j] - prices[i]) 
  return max(max_profit_so_far)

def find_max_profit(prices):
    current_min = prices[0]
    max_difference = prices[1] - prices[0] 
    for i in range(1, len(prices)):
        if prices[i] - current_min > max_difference:
            max_difference = prices[i] - current_min 
        if prices[i] < current_min:
            current_min = prices[i]
    return max_difference


def find_max_profit(prices):
    max_profit_so_far = 0

    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            current_profit_price = prices[j] - prices[i]
            if current_profit_price > max_profit_so_far:
                max_profit_so_far = current_profit_price
    return max_profit_so_far            

print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))