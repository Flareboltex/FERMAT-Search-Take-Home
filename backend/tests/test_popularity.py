from app.services.popularity_service import calculate_product_popularity


def test_calculate_product_popularity():
    orders = [
        {
            "orderId": "1",
            "items": [
                {"productId": "A", "quantity": 2},
                {"productId": "B", "quantity": 1},
            ],
        },
        {
            "orderId": "2",
            "items": [
                {"productId": "A", "quantity": 3},
            ],
        },
    ]

    popularity = calculate_product_popularity(orders)

    assert popularity["A"] == 5
    assert popularity["B"] == 1
