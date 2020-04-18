class RecentCounter:

    def __init__(self):
        self.queue = list()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        right = 0
        while right < len(self.queue):
            if t - self.queue[right] > 3000:
                self.queue.pop(0)
            else:
                break
        return len(self.queue)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)