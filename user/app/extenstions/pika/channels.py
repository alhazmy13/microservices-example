from enum import Enum


class Queues(Enum):
    user_signup_queue = "user_signup_queue"
    user_login_queue = "user_login_queue"
    user_get_queue = "user_get_queue"
