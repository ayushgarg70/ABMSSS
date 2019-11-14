import Value
import numpy as np

#each seller has 11 options,whether to increase price by +2 +4 +6 +8 +10 or decrease by -2 -4 -6 -8 -10
#or to stay at the same price

class Seller:
    def __init__(self,id,n_buyers):
        self.id=id
        self.price=100
        self.epsilon=0.9
        self.epsilon_decay=0.01
        self.Qvalue=Value.Qvalue(n_buyers+2)
        self.is_in_game=True
        self.action=0
        self.gamma=0.9

    def reset(self):
        self.epsilon=0.9
        self.is_in_game=True

    def get_price(self):
        return self.price

    def get_status(self):
        return self.is_in_game

    def decay(self):
        self.epsilon=self.epsilon*(1-self.epsilon_decay)

    def bail_out(self):
        self.is_in_game=False

    def update_qvalue(self,reward,opposite_bids):
        action = [i for i in range(-10, 11) if i % 2 == 0]
        Qvals = []
        for x in action:
            Qvals.append(self.Qvalue.get_Qvalue(x, self.price, opposite_bids))

        max_Qval = np.max(Qvals)
        target=reward+self.gamma*max_Qval

        self.Qvalue.train(self.action,self.price,opposite_bids,target)

    def get_optimal_policy(self,previous_buyers_bids):
        action=[i for i in range(-10,11) if i%2==0]
        Qvals=[]

        for x in action:
            Qvals.append(self.Qvalue.get_Qvalue(x,self.price,previous_buyers_bids))

        # print(Qvals)

        x=np.argmax(Qvals)

        # print(x)
        return action[x]

    def bid(self,previous_buyers_bids):

        if self.is_in_game:
            eps=np.random.uniform()

            if eps<self.epsilon:
                self.action=2*np.random.randint(-5,6)
                self.price = self.price + self.action
            else:
                self.action=self.get_optimal_policy(previous_buyers_bids)
                self.price = self.price + self.action

            self.decay()
        else :
            pass

