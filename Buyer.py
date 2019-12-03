import Value
import Value2
import numpy as np

#each seller has 11 options,whether to increase price by +2 +4 +6 +8 +10 or decrease by -2 -4 -6 -8 -10
#or to stay at the same price

class Buyer:
    def __init__(self,id,n_sellers):
        self.id=id
        self.price=100
        self.epsilon=0.9
        self.epsilon_decay=0.01
        self.Qvalue=Value.Qvalue(n_sellers+2)
        self.is_in_game=True
        self.action=0
        self.gamma=0.9
        self.reward=0

    def reset(self):
        self.is_in_game=True

    def get_price(self):
        return self.price

    def get_status(self):
        return self.is_in_game

    def decay(self):
        self.epsilon=self.epsilon*(1-self.epsilon_decay)

    def bail_out(self):
        self.is_in_game=False

    def get_reward(self):
        return self.reward

    def update_qvalue(self,reward,opposite_bids):
        ob = np.zeros(np.shape(opposite_bids))
        for x in range(len(ob)):
            ob[x] = (ob[x] - 100) / 40
        self.reward=self.reward+reward
        action = [i for i in range(-10, 11) if i % 2 == 0]
        Qvals = []
        for x in action:
            Qvals.append(self.Qvalue.get_Qvalue(x/10, (self.price-100)/40, ob))

        max_Qval = np.amax(Qvals)
        target=reward+self.gamma*max_Qval

        # print(target)

        self.Qvalue.train(self.action/10,(self.price-self.action-100)/40,ob,target)

    def get_optimal_policy(self,previous_seller_bids):
        ob = np.zeros(np.shape(previous_seller_bids))
        for x in range(len(ob)):
            ob[x] = (ob[x] - 100) / 40
        action=[i for i in range(-10,11) if i%2==0]
        Qvals=[]

        for x in action:
            Qvals.append(self.Qvalue.get_Qvalue(x/10,(self.price-100)/40,ob))

        x=np.argmax(Qvals)
        print(Qvals)
        # print(action[x])
        return action[x]

    def bid(self,previous_seller_bids,round):

        if self.is_in_game:

            if round < 100:
                x = self.price
                self.action = 2 * np.random.randint(-5, 6)
                self.price = self.price + self.action
                if self.price >= 120:
                    self.price = 120
                    self.action = self.price - x
                elif self.price <= 80:
                    self.price = 80
                    self.action = self.price - x
            else:
                eps = np.random.uniform()
                if eps<self.epsilon:
                    x=self.price
                    self.action=2*np.random.randint(-5,6)
                    self.price = self.price + self.action
                    if self.price>=120:
                        self.price=120
                        self.action = self.price-x
                    elif self.price<=80:
                        self.price=80
                        self.action = self.price - x

                else:
                    x=self.price
                    self.action=self.get_optimal_policy(previous_seller_bids)
                    self.price = self.price + self.action

                    if self.price>=120:
                        self.price=120
                        self.action=self.price-x
                    elif self.price<=80:
                        self.price=80
                        self.action = self.price - x
                self.decay()


        else :
            self.action=0

