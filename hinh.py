class ChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def chu_vi(self):
        return self.dai + self.rong * 2
    def dien_tich(self):
        return self.dai * self.rong
    def xuat(self):
        print(f"chiều dài:(self.dai): - hinh.py:11")
        print(f"Chiều rộng: {self.rong} - hinh.py:12")
        print(f"Diện tích: {self.get_dien_tich()} - hinh.py:13")
        print(f"Chu vi: {self.get_chu_vi()} - hinh.py:14")

class Vuong(ChuNhat):
    def __init__(self, canh):
        self.canh=canh
        super().__init__(self.canh, self.canh)

    def xuat(self):
        print(f"cạnh hình vuông:{self.dai} - hinh.py:22")
        print(f"chu vi hình vuômg:{self.chu_vi()} - hinh.py:23")
        print(f"diện tích hình vuông:{self.dien_tich()} - hinh.py:24")