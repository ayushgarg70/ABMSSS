import Seller
import Buyer
import Match
import numpy as np
import matplotlib.pyplot as plt


n_sellers=50
n_buyers=50
n_rounds=5
n_games=100
Sellers=[]
Buyers=[]
matched_sellers=dict()
matched_buyers=dict()
match_maker=Match.Match(n_sellers,n_buyers)
previous_buyers_bids=[]
previous_sellers_bids=[]
prices=[]


def initialize():
    global Sellers
    global Buyers
    global previous_sellers_bids
    global previous_buyers_bids

    for i in range(n_sellers):
        x=Seller.Seller(i,n_buyers)
        Sellers.append(x)

    for i in range(n_buyers):
        x = Buyer.Buyer(i,n_sellers)
        Buyers.append(x)

    previous_buyers_bids = np.random.normal(100, 5, (n_buyers))
    previous_sellers_bids = np.random.normal(100, 5, (n_sellers))


def bid_r(previous_buyers_bids,previous_sellers_bids,round):
    global Sellers
    global Buyers

    for x in Sellers:
        x.bid(previous_buyers_bids,round)

    for x in Buyers:
        x.bid(previous_sellers_bids,round)

def reset():
    global Sellers
    global Buyers

    for seller in Sellers:
        seller.reset()

    for buyer in Buyers:
        buyer.reset()

    global previous_sellers_bids
    global previous_buyers_bids

    previous_buyers_bids = np.random.normal(100, 5, (n_buyers))
    previous_sellers_bids = np.random.normal(100, 5, (n_sellers))



if __name__=="__main__":

    initialize()
    average_deal = []
    average_seller_price=[]
    average_buyer_price = []
    number_of_deals = []
    particular_seller=[]
    particular_buyer=[]
    particular_seller_reward= []
    particular_buyer_reward= []

    for j in range(n_games):
        reset()

        for i in range(n_rounds):

            print('Game {}: Round {}'.format(j,i))

            bid_r(previous_buyers_bids,previous_sellers_bids,j)


            #match_maker returns updated list of sellers and buyers in the game and a
            #dictionary for matched sellers and buyers containing their ids and rewards
            (deal,number)=match_maker.make_matches(Sellers,Buyers,previous_buyers_bids,previous_sellers_bids)
            #matched_dict=[(ids),(rewards)]

            previous_buyers_bids = []
            previous_sellers_bids = []

            for x in Buyers:
                previous_buyers_bids.append(x.get_price())


            for x in Sellers:
                previous_sellers_bids.append(x.get_price())


            if j>10:
                for x in Sellers:
                    if x.id == 10:
                        particular_seller.append(x.get_price())
                        particular_seller_reward.append(x.get_reward())

                for x in Buyers:
                    if x.id == 20:
                        particular_buyer.append(x.get_price())
                        particular_buyer_reward.append(x.get_reward())

                avg_deal = deal
                avg_seller = np.sum(previous_sellers_bids) / n_sellers
                avg_buyer = np.sum(previous_buyers_bids) / n_buyers

                if avg_deal != 0:
                    average_deal.append(avg_deal)
                average_seller_price.append(avg_seller)
                average_buyer_price.append(avg_buyer)
                if number != 0:
                    number_of_deals.append(number)

        for x in Sellers:
            if x.id == 10:
                action = [i for i in range(-10, 11) if i % 2 == 0]
                Qvals = []

                for y in action:
                    Qvals.append(x.Qvalue.get_Qvalue(y, x.price, previous_buyers_bids))

                print(Qvals)



    plt.figure()
    plt.title('average_deal')
    plt.plot(average_deal)
    plt.figure()
    plt.title('average_seller_price')
    plt.plot(average_seller_price)
    plt.figure()
    plt.title('average_buyer_price')
    plt.plot(average_buyer_price)
    plt.figure()
    plt.title('number_of_deals')
    plt.plot(number_of_deals)
    plt.figure()
    plt.title('Buyer number 20')
    plt.plot(particular_buyer)
    plt.figure()
    plt.title('Seller number 10')
    plt.plot(particular_seller)
    plt.figure()
    plt.title('Buyer number 20 reward')
    plt.plot(particular_buyer_reward)
    plt.figure()
    plt.title('Seller number 10 reward')
    plt.plot(particular_seller_reward)
    plt.show()
