import unittest
from uuid import uuid4

from src.models import Asset

uuid = str(uuid4())
asset_id = str(uuid4())
class TestAsset(unittest.TestCase):
    def test_get_value(self):
        asset = Asset(uid=uuid, asset_id=asset_id, price=100000, depreciation_rate=0.05, age=10)
        self.assertEqual(asset.get_value(), 59873.69392383787)

    def test_get_uuid(self):
        asset = Asset(uid=uuid, asset_id=asset_id, price=30000, depreciation_rate=0.10, age=5)
        self.assertEqual(asset.get_uid(), uuid)

    def test_get_price(self):
        asset = Asset(uid=uuid, asset_id=asset_id, price=1000, depreciation_rate=0.20, age=1)
        self.assertEqual(asset.get_price(), 1000)

    def test_get_depreciation_rate(self):
        asset = Asset(uid=uuid, asset_id=asset_id, price=500, depreciation_rate=0.25, age=0)
        self.assertEqual(asset.get_depreciation_rate(), 0.25)

    def test_set_price(self):
        asset = Asset(uid=uuid, asset_id=asset_id, price=800, depreciation_rate=0.35, age=2)
        asset.set_price(900)
        self.assertEqual(asset.get_price(), 900)

    def test_set_depreciation_rate(self):
        asset = Asset(uid=uuid, asset_id=asset_id, price=200, depreciation_rate=0.40, age=1)
        asset.set_depreciation_rate(0.45)
        self.assertEqual(asset.get_depreciation_rate(), 0.45)

    def test_get_available(self):
        asset = Asset(uid=uuid, asset_id=asset_id, price=1000, depreciation_rate=0.45, age=0)
        self.assertEqual(asset.get_available(), True)

    def test_set_available(self):
        asset = Asset(uid=uuid, asset_id=asset_id, price=1000, depreciation_rate=0.45, age=0)
        asset.set_available(False)
        self.assertEqual(asset.get_available(), False)


if __name__ == '__main__':
    unittest.main()

