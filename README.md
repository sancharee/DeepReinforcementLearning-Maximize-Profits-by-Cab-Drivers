# DeepReinforcementLearning-Maximize-Profits-by-Cab-Drivers
![6f8a3f85fd8f26f0b2b3c47b9ab80479a89ebe5c](https://user-images.githubusercontent.com/16771458/224551523-55fb1e0e-b0e4-42a2-ad61-841b5d858e78.jpg)


Cab drivers, like most people, are incentivised by a healthy growth in income. The goal of this project is to build an Deep RL-based algorithm which can help cab drivers maximise their profits by improving their decision-making process on the field.
Taking long-term profit as the goal,  a method based on reinforcement learning has been proposed to optimize taxi driving strategies for profit maximization. This optimisation problem is formulated as a Markov Decision Process.

## The Need for Choosing the "Right" Requests in order to maximize Profit
Most drivers get a healthy number of ride requests from customers throughout the day. But with the recent hikes in electricity prices (all cabs are electric), many drivers complain that although their revenues are gradually increasing, their profits are almost flat. Thus, it is important that drivers choose the 'right' rides, i.e. choose the rides which are likely to maximise the total profit earned by the driver that day.  

For example, say a driver gets three ride requests at 5 PM. The first one is a long-distance ride guaranteeing high fare, but it will take him to a location which is unlikely to get him another ride for the next few hours. The second one ends in a better location, but it requires him to take a slight detour to pick the customer up, adding to fuel costs. Perhaps the best choice is to choose the third one, which although is medium-distance, it will likely get him another ride subsequently and avoid most of the traffic. 

There are some basic rules governing the ride-allocation system. If the cab is already in use, then the driver won’t get any requests. Otherwise, he may get multiple request(s). He can either decide to take any one of these requests or can go ‘offline’, i.e., not accept any request at all. 

