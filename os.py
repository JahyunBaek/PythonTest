try:
    # Windows용 코드
    import msvcrt

    def getkey():
        """단일키 누르는 것을 받아옴"""
        return msvcrt.getch()

except ImportError:
    # Linux & Mac 용 코드
    import sys
    import tty
    import termios

    def getkey():
        """단일키 누르는 것을 받아옴"""
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        return ch