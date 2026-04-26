class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, value=None):
        if hasattr(self, "_initialized") and self._initialized:
            return

        self.value = value
        self._initialized = True

obj1 = Singleton("Pierwsza wartość")
obj2 = Singleton("Druga wartość")

print(obj1.value)
print(obj2.value)

print(obj1 is obj2)