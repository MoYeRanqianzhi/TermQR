import qrcode


class QRCode:
    def __init__(self, data, version=1, box=1, border=1):
        self.data = data
        self.version = version
        self.box = box
        self.border = border
        self.QR = None
        self.width = None
        self.height = None
        self.pixels = None

    def generate(self):
        qr = qrcode.QRCode(
            version=self.version,
            box_size=self.box,
            border=self.border
        )
        qr.add_data(self.data)
        qr.make(fit=True)
        self.QR = qr.make_image(fill_color="white", back_color="black").convert('L')

    def getSize(self):
        return self.QR.size

    def WH(self):
        self.width, self.height = self.getSize()

    def getPixels(self):
        return self.QR.load()

    def Pixels(self):
        self.pixels = self.getPixels()

    def configure(self, data=None, version=None, box=None, border=None):
        if data is not None:
            self.data = data
        if version is not None:
            self.version = version
        if box is not None:
            self.box = box
        if border is not None:
            self.border = border
        self.generate()
