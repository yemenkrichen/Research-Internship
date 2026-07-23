from mesa import Agent


class TwitterUser(Agent):

    def __init__(
        self,
        model,
        user_id,
        state="S",
        followers=0,
        emotion_score=0,
        political_bias=1.0
    ):

        super().__init__(model)

        self.user_id = user_id

        # SDPNRI compartment
        self.state = state

        # structural variables
        self.followers = followers

        # cognitive variables
        self.emotion_score = emotion_score
        self.political_bias = political_bias

        # simulation tracking
        self.time_in_state = 0
        self.tweet_history = []


    def calculate_retweet_probability(self):

        probability = (
            self.political_bias *
            self.emotion_score
        )

        return probability


    def step(self):

        self.time_in_state += 1
