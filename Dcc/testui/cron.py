from Dcc.testui.dcc import Selenium_PC
from core.core import Core


def uitest():
    DccPc=Selenium_PC()
    DccPc.runTest()

if __name__ == "__main__":
    DccPc = Selenium_PC()
    DccPc.runTest()

    pass