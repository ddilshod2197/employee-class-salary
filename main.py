class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.brand} {self.model} started.")
        else:
            print(f"{self.brand} {self.model} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} stopped.")
        else:
            print(f"{self.brand} {self.model} is already stopped.")
```

```python
# Misol uchun:
car = Car("Toyota", "Camry", 2020)
car.start()  # Toyota Camry started.
car.stop()   # Toyota Camry stopped.
car.start()  # Toyota Camry started.
car.stop()   # Toyota Camry stopped.
