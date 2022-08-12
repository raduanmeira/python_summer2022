################################################################################
#
# Raduan van Velthem Meira
# Python summer course 2022 -- Homework 1
# August 15, 2022
#
################################################################################

import random as rd

# Creating the Portfolio class

class Portfolio:
  def __init__(self, cash = 0):
    self.cash = cash
    self.myStocks = {}
    self.myFunds = {}
    self.historical = ["Transaction history:\n"]
  
  # Function to add cash
  
  def addCash(self, newCash):
    self.cash = self.cash + newCash
    self.historical.append("Add $ %.2f " % newCash + "\n")

  # Function to withdraw cash 
  
  def withdrawCash(self, withdraw):
    self.cash = self.cash - withdraw
    self.historical.append("Withdraw $ %.2f " % withdraw + "\n")
    
  # Function to add stock 
  
  def buyStock(self, quantity, stock):
    if stock.stock not in self.myStocks: #check if the key for the stock already exists
      self.myStocks[stock.stock] = quantity #add stock to the dictionary
    else:
      self.myStocks[self.stock] += quantity
    self.cash = self.cash - quantity*stock.price
    self.historical.append( f"Bought {quantity} stocks of " + stock.stock + "\n")
    
  # Function to sell stock
  
  def sellStock(self, stock, quantity):
    self.stock = stock
    self.quantity = quantity
    self.myStocks[self.stock] += -self.quantity
    self.cash = self.cash + self.quantity*rd.uniform(0.5,1.5)*s.price
    self.historical.append(f"Sell {quantity} stocks of " + stock + "\n")

  # Function to add mutual fund
  
  def buyMutualFund(self, quantity, fund):
    if fund.fund not in self.myFunds: #check if the key for the fund already exists
      self.myFunds[fund.fund] = quantity #add fund to the dictionary
    else:
      self.myFunds[fund.fund] += quantity
    self.cash = self.cash - quantity*1
    self.historical.append(f"Bought {quantity} mutual funds of " + fund.fund + "\n")
    
  # Function to sell sel mutual fund
  
  def sellMutualFund(self, fund, quantity):
    self.myFunds[fund] += -quantity
    self.cash = self.cash + quantity*rd.uniform(0.9,1.2)
    self.historical.append(f"Sell {quantity} mutual funds of " + fund + "\n")
    
  def __str__(self):
    output = "Prints portfolio"
    output += '\n'
    output += "cash: $ %.2f " % self.cash
    output += '\n'
    output += "Stock: " 
    for k, v in portfolio.myStocks.items(): output += str(f"{v} {k}\n") 
    output += "Mutual funds: " 
    for k, v in portfolio.myFunds.items(): output += str(f"{v} {k}\n") 
    return output
  
  def history(self):
    print(''.join(self.historical))



#
#
#

# Creating the stock class

class Stock:
  def __init__(self, price, stock):
    self.price = price
    self.stock = stock


# Creating the mutual fund class

class MutualFund:
  def __init__(self, fund):
    self.fund = fund

### Testing the required functions

portfolio = Portfolio()
portfolio.addCash(300.50)
s = Stock(20, "HFH")
portfolio.buyStock(5, s)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)
print(portfolio)
portfolio.sellMutualFund("BRT", 3)
portfolio.sellStock("HFH", 1)
portfolio.withdrawCash(50)
portfolio.history()
