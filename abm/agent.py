from mesa import Agent


class TwitterUser(Agent):

    def __init__(
        self,
        model,
        user_id,
        activities,
        initial_state="S",
        political_bias=1.0
    ):

        super().__init__(model)
        self.user_id = user_id
        self.state = initial_state
        self.time_in_state = 0
        self.activities = activities
        self.current_activity = 0
