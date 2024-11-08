from praktikum.bun import Bun

def test_bun_name():
    bun = Bun(name="Classic", price=3.5)
    assert bun.get_name() == "Classic"

def test_bun_price():
    bun = Bun(name="Classic", price=3.5)
    assert bun.get_price() == 3.5