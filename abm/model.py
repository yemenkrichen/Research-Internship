from mesa import Model
from agent import TwitterUser

class RumorModel(Model):
    def __init__(self, user_timelines):

        super().__init__()
        self.current_time = 0
        self.num_users = len(user_timelines)
        for user_id, activities in user_timelines.items():

            TwitterUser(
                model=self,
                user_id=user_id,
                activities=activities
            )
    def step(self):
        self.agents.shuffle_do("step")
        self.current_time += 1
