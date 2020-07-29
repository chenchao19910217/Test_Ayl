from locust import HttpUser, task, between
import random
class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    # @task
    # def test_dcc_index(self):
    #     self.client.get("test.douchacha.com")

    @task(3)
    def view_item(self):
        # item_id = random.randint(1, 10000)
        self.client.get("/ad.html")

    # def on_start(self):
    #     #     self.client.get("test.douchacha.com")