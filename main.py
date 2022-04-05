class Product:

    def __init__(self, _id, name, price):
        self.id = _id
        self.name = name
        self.price = price

    def __str__(self):
        return f'#{idx} {name} {price}$'


products = (
    ('shirt', '21'),
    ('jacket', '32'),
    ('basket', '12'),
)


for idx, data in enumerate(products):
    _id = idx + 1
    name = data[0]
    price = data[1]
    globals()[f'obj_{_id}'] = Product(_id, name, price)