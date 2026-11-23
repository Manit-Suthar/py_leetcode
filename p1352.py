class ProductOfNumbers:
    def __init__(self):
        # Dummy '1' at index 0 makes prefix division work cleanly
        self.arrProduct = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Reset the prefix product list whenever a 0 appears
            self.arrProduct = [1]
        else:
            # Multiply current number with the last stored prefix product
            self.arrProduct.append(num * self.arrProduct[-1])

    def getProduct(self, k: int) -> int:
        # If k reaches past the last reset (0), the product is guaranteed to be 0
        if k >= len(self.arrProduct):
            return 0
        
        # Otherwise, divide the latest product by the product k steps back
        return self.arrProduct[-1] // self.arrProduct[-k - 1]

if __name__ == "__main__":
    obj = ProductOfNumbers()
    obj.add(3)
    obj.add(5)
    obj.add(0)
    obj.add(2)
    obj.add(4)
    print(obj.getProduct(2))  
    print(obj.getProduct(3)) 
    print(obj.getProduct(4)) 