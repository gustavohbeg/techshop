"""
Testes unitários para a classe ShoppingCart.
"""

from src.models import Product
from src.cart import ShoppingCart


def test_add_item_success() -> None:
    """
    Testa se a adição de um novo produto ao carrinho funciona corretamente.
    """
    # Arrange
    cart = ShoppingCart()
    product = Product(id=1, name="Smartphone", price=1500.0)

    # Act
    cart.add_item(product, 1)

    # Assert
    assert len(cart.items) == 1
    assert cart.items[0].product.id == 1
    assert cart.items[0].quantity == 1


def test_add_existing_item_updates_quantity() -> None:
    """
    Testa se a adição de um produto que já está no carrinho
    atualiza a quantidade corretamente em vez de adicionar um novo item.
    """
    # Arrange
    cart = ShoppingCart()
    product = Product(id=1, name="Smartphone", price=1500.0)
    cart.add_item(product, 1)

    # Act
    cart.add_item(product, 2)

    # Assert
    assert len(cart.items) == 1
    assert cart.items[0].quantity == 3


def test_remove_item_success() -> None:
    """
    Testa se um item é removido corretamente do carrinho.
    """
    # Arrange
    cart = ShoppingCart()
    product1 = Product(id=1, name="Smartphone", price=1500.0)
    product2 = Product(id=2, name="Case", price=50.0)
    cart.add_item(product1, 1)
    cart.add_item(product2, 1)

    # Act
    cart.remove_item(1)

    # Assert
    assert len(cart.items) == 1
    assert cart.items[0].product.id == 2


def test_calculate_total_success() -> None:
    """
    Testa o cálculo do valor total do carrinho sem descontos.
    """
    # Arrange
    cart = ShoppingCart()
    product1 = Product(id=1, name="Smartphone", price=100.0)
    product2 = Product(id=2, name="Case", price=50.0)
    cart.add_item(product1, 2)
    cart.add_item(product2, 1)

    # Act
    total = cart.calculate_total()

    # Assert
    assert total == 250.0


def test_calculate_total_with_10_percent_discount() -> None:
    """
    Testa o cálculo com desconto de 10% para compras acima de R$ 500.
    """
    # Arrange
    cart = ShoppingCart()
    product = Product(id=1, name="Smartphone", price=600.0)
    cart.add_item(product, 1)

    # Act
    total_with_discount = cart.calculate_total_with_discount()

    # Assert
    assert total_with_discount == 540.0


def test_calculate_total_with_20_percent_discount() -> None:
    """
    Testa o cálculo com desconto de 20% para compras acima de R$ 1000.
    """
    # Arrange
    cart = ShoppingCart()
    product = Product(id=1, name="Notebook", price=1500.0)
    cart.add_item(product, 1)

    # Act
    total_with_discount = cart.calculate_total_with_discount()

    # Assert
    assert total_with_discount == 1200.0

<<<<<<< HEAD
def test_add_multiple_different_items_success() -> None:
    """
    Testa a adição de vários produtos diferentes ao carrinho.
    """
    # Arrange
    cart = ShoppingCart()
    product1 = Product(id=1, name="Mouse", price=100.0)
    product2 = Product(id=2, name="Teclado", price=200.0)
    product3 = Product(id=3, name="Monitor", price=1000.0)
    
    # Act
    cart.add_item(product1, 1)
    cart.add_item(product2, 2)
    cart.add_item(product3, 1)
    
    # Assert
    assert len(cart.items) == 3
    assert cart.items[0].product.id == 1
    assert cart.items[1].quantity == 2
    assert cart.items[2].product.name == "Monitor"

def test_remove_item_preserves_other_items() -> None:
    """
    Testa se a remoção de um item específico não afeta os demais itens no carrinho.
    """
    # Arrange
    cart = ShoppingCart()
    product1 = Product(id=1, name="Mouse", price=100.0)
    product2 = Product(id=2, name="Teclado", price=200.0)
    cart.add_item(product1, 1)
    cart.add_item(product2, 2)
    
    # Act
    cart.remove_item(1)
    
    # Assert
    assert len(cart.items) == 1
    assert cart.items[0].product.id == 2
    assert cart.items[0].quantity == 2

def test_calculate_total_with_multiple_quantities() -> None:
    """
    Testa se o cálculo total lida corretamente com múltiplas quantidades de diferentes itens,
    sem aplicar descontos.
    """
    # Arrange
    cart = ShoppingCart()
    product1 = Product(id=1, name="Cabo USB", price=20.0)
    product2 = Product(id=2, name="Pendrive", price=50.0)
    
    # Act
    cart.add_item(product1, 3) # 60.0
    cart.add_item(product2, 2) # 100.0
    total = cart.calculate_total()
    
    # Assert
    assert total == 160.0
=======
>>>>>>> main

# --- Edge Cases ---


def test_calculate_total_empty_cart() -> None:
    """
    Testa o caso de borda: carrinho vazio.
    O total deve ser 0.0 tanto para o valor normal quanto com desconto.
    """
    # Arrange
    cart = ShoppingCart()

    # Act
    total = cart.calculate_total()
    total_with_discount = cart.calculate_total_with_discount()

    # Assert
    assert total == 0.0
    assert total_with_discount == 0.0


def test_calculate_total_exact_discount_threshold_500() -> None:
    """
    Testa o caso de borda: total exatamente igual a R$ 500.
    Nenhum desconto deve ser aplicado, pois o limite é > 500.
    """
    # Arrange
    cart = ShoppingCart()
    product = Product(id=1, name="Product", price=500.0)
    cart.add_item(product, 1)

    # Act
    total_with_discount = cart.calculate_total_with_discount()

    # Assert
    assert total_with_discount == 500.0


def test_calculate_total_exact_discount_threshold_1000() -> None:
    """
    Testa o caso de borda: total exatamente igual a R$ 1000.
    Deve ser aplicado o desconto de 10%, pois o limite para 20% é > 1000.
    """
    # Arrange
    cart = ShoppingCart()
    product = Product(id=1, name="Product", price=1000.0)
    cart.add_item(product, 1)

    # Act
    total_with_discount = cart.calculate_total_with_discount()

    # Assert
    assert total_with_discount == 900.0


def test_remove_non_existent_item() -> None:
    """
    Testa o caso de borda: remover um item que não existe no carrinho.
    O carrinho não deve ser alterado.
    """
    # Arrange
    cart = ShoppingCart()
    product = Product(id=1, name="Product", price=500.0)
    cart.add_item(product, 1)

    # Act
    cart.remove_item(999)

    # Assert
    assert len(cart.items) == 1
