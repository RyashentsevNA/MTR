from MaterialOrdersAdapter.MaterialOrdersProductPosition import MaterialOrdersProductPosition


class TestCreate(MaterialOrdersProductPosition):
    # Создает заявку на вкладке "Журнал заявок"
    def test_create_material_orders_product_position(self):
        self.create_material_orders_product_position()

