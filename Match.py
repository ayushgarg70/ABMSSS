import numpy as np



class Match:
    def __init__(self,n_sellers,n_buyers):
        self.n_sellers=n_sellers
        self.n_buyers =n_buyers


    def make_matches(self,Sellers,Buyers,previous_buyers_bids,previous_sellers_bids):

        seller_perm=np.random.permutation(self.n_sellers)
        buyer_perm =np.random.permutation(self.n_buyers)
        punishment=0
        sum=0
        count=0

        for seller_id in seller_perm:
            if Sellers[seller_id].get_status()==True:
                for buyer_id in buyer_perm:
                    if Buyers[buyer_id].get_status() == True:
                        # and Buyers[buyer_id].get_price() - Sellers[seller_id].get_price() <= 2
                        if Sellers[seller_id].get_price()<=Buyers[buyer_id].get_price():
                            deal_price=np.random.randint(Sellers[seller_id].get_price(),Buyers[buyer_id].get_price()+1)
                            seller_reward=deal_price-80
                            # buyer_reward=10/(deal_price-80+1)
                            # seller_reward=0
                            buyer_reward = 120-deal_price
                            # deal_price=Sellers[seller_id].get_price()

                            Sellers[seller_id].update_qvalue(seller_reward,previous_buyers_bids)
                            Buyers[buyer_id].update_qvalue(buyer_reward,previous_sellers_bids)

                            Sellers[seller_id].bail_out()
                            Buyers[buyer_id].bail_out()

                            print("Deal made between seller {} and buyer {}".format(seller_id,buyer_id))
                            print("Deal made at {} for seller_price {} and buyer_price {}".format(deal_price,Sellers[seller_id].get_price(),Buyers[buyer_id].get_price()))

                            sum=sum+deal_price
                            count=count+1

                            break

        for seller_id in seller_perm:
            if Sellers[seller_id].get_status()==True:
                Sellers[seller_id].update_qvalue(punishment, previous_buyers_bids)

        for buyer_id in buyer_perm:
            if Buyers[buyer_id].get_status()==True:
                Buyers[buyer_id].update_qvalue(punishment, previous_sellers_bids)

        if count:
            return (sum/count,count)
        else:
            return (0,0)










