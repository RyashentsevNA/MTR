from MaterialOrdersAdapter.MaterialOrdersProductPosition import MaterialOrdersProductPosition


class TestMaterialOrdersProductPosition(MaterialOrdersProductPosition):
    def test_material_orders_product_position(self):
        MaterialOrdersProductPosition.create_material_orders_product_position(self)