import Seller
import Buyer
import Match
import numpy as np
import matplotlib.pyplot as plt


n_sellers=50
n_buyers=50
n_rounds=5
n_games=1000
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


def bid_r(previous_buyers_bids,previous_sellers_bids):
    global Sellers
    global Buyers

    for x in Sellers:
        x.bid(previous_buyers_bids)

    for x in Buyers:
        x.bid(previous_sellers_bids)

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

    for j in range(n_games):
        reset()
        avg_deal=0
        avg_seller=0
        avg_buyer = 0

        for i in range(n_rounds):

            print('Game {}: Round {}'.format(j,i))

            bid_r(previous_buyers_bids,previous_sellers_bids)

            #match_maker returns updated list of sellers and buyers in the game and a
            #dictionary for matched sellers and buyers containing their ids and rewards
            deal=match_maker.make_matches(Sellers,Buyers,previous_buyers_bids,previous_sellers_bids)
            #matched_dict=[(ids),(rewards)]

            previous_buyers_bids = []
            previous_sellers_bids = []
            for x in Buyers:
                previous_buyers_bids.append(x.get_price())

            for x in Sellers:
                previous_sellers_bids.append(x.get_price())

            avg_deal=deal+avg_deal
            avg_seller= avg_seller+np.sum(previous_sellers_bids)/n_sellers
            avg_buyer = avg_buyer + np.sum(previous_buyers_bids)/n_buyers


        average_deal.append(avg_deal/n_rounds)
        average_seller_price.append(avg_seller / n_rounds)
        average_buyer_price.append(avg_buyer / n_rounds)


    plt.figure()
    plt.title('average_deal')
    plt.plot(average_deal)
    plt.figure()
    plt.title('average_seller_price')
    plt.plot(average_seller_price)
    plt.figure()
    plt.title('average_buyer_price')
    plt.plot(average_buyer_price)
    plt.show()