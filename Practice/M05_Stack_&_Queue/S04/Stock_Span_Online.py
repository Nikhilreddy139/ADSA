#901:Problem
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
            
        self.stack.append((price, span))
        return span
input1 = ["StockSpanner", "next", "next", "next", "next", "next", "next"]
price = [100, 80, 60, 70, 60, 75, 85]
obj = StockSpanner()
param_1 = [obj.next(p) for p in price]
print(param_1)

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)