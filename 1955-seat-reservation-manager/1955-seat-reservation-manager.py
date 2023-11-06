class SeatManager:
    def __init__(self, n: int):
        self.q = [i for i in range(1, n + 1)]

    def reserve(self) -> int:
        return heappop(self.q)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.q, seatNumber)