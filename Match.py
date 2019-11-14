import numpy as np



class Match:
    def __init__(self,n_sellers,n_buyers):
        self.n_sellers=n_sellers
        self.n_buyers =n_buyers

    def make_matches(self,Sellers,Buyers,previous_buyers_bids,previous_sellers_bids):

        seller_perm=np.random.permutation(self.n_sellers)
        buyer_perm =np.random.permutation(self.n_buyers)

        for seller_id in seller_perm:
            if Sellers[seller_id].get_status()==True:
                for buyer_id in buyer_perm:
                    if Buyers[buyer_id].get_status() == True:
                        if Sellers[seller_id].get_price()<=Buyers[buyer_id].get_price():
                            deal_price=np.random.randint(Sellers[seller_id].get_price(),Buyers[buyer_id].get_price()+1)
                            seller_reward=deal_price-Sellers[seller_id].get_price()
                            buyer_reward=1/(deal_price-Sellers[seller_id].get_price()+1)

                            Sellers[seller_id].update_qvalue(seller_reward,previous_buyers_bids)
                            Buyers[buyer_id].update_qvalue(buyer_reward,previous_sellers_bids)

                            Sellers[seller_id].bail_out()
                            Buyers[buyer_id].bail_out()

                            print("Deal made between seller {} and buyer {}".format(seller_id,buyer_id))
                            print("Deal made at {} for seller_price {} and buyer_price{}".format(deal_price,Sellers[seller_id].get_price(),Buyers[buyer_id].get_price()))
                            break













