from colorama import init

from .QR import QRCode

__WHITE__ = '\033[107m  \033[0m'
__BLACK__ = '\033[40m  \033[0m'
__NONE__ = '  '


def initialize():
    init(autoreset=True)


def MakeQR(data, color, on_color, version=1, box=1, border=1):
    qr = QRCode(data=data, version=version, box=box, border=border)
    qr.generate()
    qr.WH()
    qr.Pixels()

    output = ''
    for y in range(qr.height):
        for x in range(qr.width):
            pixel = qr.pixels[x, y]
            if pixel == 0:
                output += on_color
            else:
                output += color
        output += '\n'

    return output


def simpleQR(data, version=1, box=1, border=1):
    return MakeQR(data=data, color=__WHITE__, on_color=__BLACK__, version=version, box=box, border=border)


if __name__ == '__main__':
    print(simpleQR('https://www.google.com'))
