class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.customer = n
        self.counter = 0
        self.discount = discount
        self.map_dict = {}
        for i in range(len(products)):
            self.map_dict[products[i]] = prices[i] 

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.counter+=1
        total_sum = sum([self.map_dict[product[i]]*amount[i] for i in range(len(product))])
        if self.counter == self.customer:
            self.counter = 0
            total_sum = ((100-self.discount)/100)*total_sum
        return total_sum
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)