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

<img alt="Population relation diagram" src="https://github.com/mottetm/zombie_outbreak/blob/master/images/figure1.png?raw=true" style="align: center;"/>

For each state (microstate), we define a SZR model that evaluates the evolution of the different populations under studies: susceptibles (S), zombies (Z) and removed (R). Epidemological-like transfer of populations between the states (at the macrostate level) also occurs as defined above and models the refugees and zombie transfer across states. Those transfers are parameters dependants, which depend on the cost-hypothesis as defined by the Game-Theoretical paradigm implemented. The apparition of zombies in one state will start the game. Each state will then evolve on the domestic and international level. The domestic level will follow a standard SZR model, whereas the international level will introduce exchange in the population of suceptible and zombie between the states. These exchanges will be influenced by the state decisions on foreign policies such as humanitarian or military actions determined by our game theory framework. The Game-Theoretical framework is defined as the possibility of undertaking military action of foreign soil (exporting S) or changing the refugee politics by modifying the mu parameter (allowing more S to come into one's state, and with a collateral cost of having more zombies crossing as well). Each action will be defined with a specific payoff, which in turn will depend on the international cooperation system under scrutiny. For simplicity, we will only model homogenous systems, i.e. all the states will adopt the same international politics paradigm. Finally, we will also introduce a "feedback" loop on the payoff depending on the success of a previously undertaken action (positive or negative affectation of the payoffs). This effect models the psychological effect of a successful or unsuccessful action on future action, for example the effectiveness of a military attack. This effect will be made as to converge after a certain time to model the wearing out of the psychological effect over time. The system will be implemented as a step-based update. This implies the ignorance of the actors (the states) of the action of the other actors. This rationalisation comes as the idea that the outbreak would occur over a short period of time, forcing for rapid decision-making and therefore not allow a reaction-based decision-making process. 

## Fundamental Questions

Investigation of the application of the SIR model to a zombie outbreak has already been studied, raising the fear of dark days for humanity. However, we would like to deepen this investigation to a multi-state system to see how interactions between subpopulation may brighten the future of the human race. Moreover, we are interested in seeing to what extent the different paradigms of international politics, *Realpolitik*, Liberalism and Neoconservatism as defined by Daniel W. Drezner in *Theories of International Politics and zombies* may lead to different outcomes.

## Expected Results

As describe in Drezner's book, we except different equilibrium outcomes depending on the paradigm under consideration. He postulates the possibile appearance of zombie states under *Realpolitik* and Liberalism paradigms while Neoconservatism would not allow such an outcome.

## References 

1. Daniel W. Drezner, *Theories of International Politics and Zombies* (Princeton Univ. Press, 2011)
2. Philip Munz, Ioan Hudea, Joe Imad, Robert J. Smith?, *Infectious Disease Modelling Research Progress: 4 - When Zombies Attack!: Mathematical Modelling of an Outbreak of Zombie Infection* (Nova Science Publisher, 2009) 
3. Timothy C. Reluga, *An SIS epidemiology game with two subpopulations*, Journal of Biological Dynamics, **3**, 515-531 (2009)
4. Timothy C. Reluga, *Game Theory of Social Distancing in Response to an Epidemic*, PLOS Computational Biology, **6** (2010)
5. Sebastian Funk, MArcel Salathé, Vincent A. A. Jansen, *Modelling the Influence of Human Behaviour on the Spread of Infectious Diseases: A Review*, J. R. Soc. Interface, **7**, 1247-1256 (2010)
6. Duygu Baclan and Alessandro Vespigniani, *Phase Transitions in Contagion Processes Mediated by Recurrent Mobility Pattern*, Nature Physics, **7**, 581-586 (2011)
7. Peter G. Bennett, *Modelling Decisions in International Relations: Game Theory and Beyond*, Mershon Int. Studies Review, **39**, 19-52 (1995)

## Research Methods

We would like to tackle this question by using a two-level model. Intra-state populations would be modelled by a standard SIR (Kermack-McKendrick) model or an evolution of it that might include quarantined poplutions and more evolved parameters. On the next level, the inter-state relationships would be modelled using Game-Theory under different cost-hypothesis related to the main paradigms of international relationships as previously defined. 

## Other

The material necessary for defining our models of zombies and 'zombification' parameters will be extracted from the canon of the zombie popular culture such as *World War Z* (Brooks, 2006), *28 Days Later* (Boyle, 2002), *The Night of the Living Dead* (Romero, 1968), *Zombieland* (Fleischer, 2009), Resident Evil (Capcom, 1996), etc.

