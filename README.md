# ABMSSS
Reinforcement Learning for Market Simulation

> * Group Name: Muti-armed Bandits
> * Group participants names: Ayush Garg, Virgile Troude, Simon Hasenfratz, Martin Fiebig


## General Introduction

* Our project tries to gain an insight in a hypothetical double auction scenario where there are different number of sellers and buyers who are trying to buy and sell a fictitious commodity of make price 80 units. 
* It is assumed that *no seller will ask for a price < 80 units* and that *no buyer will pay more than his/her budget=120 units*. Hence the whole auction happens between 80 < price < 120. At every time step each seller/buyer has the option of increasing/decreasing his previous price by atmost 10 units. Hence **previous_price-10 < current_price < previous_price + 10**
* The auction happens as follows:
 1. Every time step each seller has the information of the bid price put forward by all the buyers in the previous time step and based on this information the seller decides what his ask price will be in this time step.
 2. Each buyer also has the information of every seller's ask price in the previous time step, and the buyer makes his current decision based on this information.
 3. Once all the sellers and buyers have made their ask and bid prices, the match maker of the auction decides which buyer matches with which seller. This decision is taken as follows:
    1. First all the buyer prices are arranged in a list and shuffled.
    2. Then all the seller prices are arranged in a list and shuffled.
    3. Now the first seller in the shuffled list is selected and is matched with the first buyer that has a price greater than his price. 
    4. When a buyer and a seller are paired, the deal price is selected as a uniform number between the seller's ask and the buyer's bid. 
    5. This deal price is then used to calculate the seller's reward as (deal price- 80) and the buyer's reward as 10/(deal price -79)
    6. Once they are paired and matched, they are removed from the list and the next seller is taken up for pairing
 4. Whenever a buyer and a seller are paired they get a reward and that reward is used to train the Q-Learning neural network of that buyer/seller.    
 5. Finally after the matching process is over, whichever buyer and seller is still in the game, is punished by a punishment reward(*negative*)
    


## Dependencies



>To run the code you will need to install python3.x

Assuming the above you'll need to have the following libraries installed:
1. numpy 
   *pip install numpy
2. keras
   *pip install keras
3. tensorflow 
   *pip install --upgrade tensorflow
4. scikit-learn
   *pip install scikit-learn
5. matplotlib
   *python -m pip install -U matplotlib
   
 ## Procedure

Having installed all the dependencies, clone the git repository to a convenient location and open a terminal session in that directory.
Type **python3 Market.py** or **python Market.py**


## Expected Results

<img alt="General result of seller vs buyer" src="/images/Figure_2.png" style="align: center;"/>

Plots similar to the ones shown above should be shown automatically. 

## References 

1. Rowel Atienza, *Advanced Deep Learning with Keras* (2018)
2. Frank L. Lewis, Draguna L. Vrabie and Vassilis L. Syrmos, *Optimal Control* (Third Edition)
3. Richard S. Sutton and Andrew G. Barto, *Reinforcement Learning: An Introduction* (2018)

