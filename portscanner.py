from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

from socket import (
    socket,
    AF_INET,
    SOCK_STREAM
)
import time

class Colors:
    WHITE:     str = '\033[38;2;255;255;255m'
    PINK:      str = '\033[38;2;255;50;75m'
    LIME:      str = '\033[38;2;0;255;152m'
    RED:       str = '\033[38;2;255;0;0m'
    LIGHTRED:  str = '\033[38;2;255;25;50m'
    LIGHTPINK: str = '\033[38;2;255;150;255m'

class Scanner:
    prange: dict = {
        number for number in range(10000) if number not in 
        (21, 22, 23, 25, 53, 69, 80, 443, 3074, 3306, 5060, 9307)
    }
    

    def __init__(self: Scanner, addr: str = '127.0.0.1') -> None:
        self.results: list = []
        self._addr:   str  = addr


    @property
    def addr(self: Scanner) -> str:
        return self._addr
    

    @addr.setter
    def addr(self: Scanner, addr: str) -> None:        
        if not isinstance(addr, str):
            raise TypeError
        
        if addr.count('.') != 3:
            raise ValueError

        self._addr: str = addr


    def get_results(self: Scanner) -> list:
        self.results.clear()

        with ThreadPoolExecutor(max_workers=800) as executor:
            for port in self.prange:
                executor.submit(self.__connect, port)


    def __connect(self: Scanner, port: int) -> None:
    
        with socket(AF_INET, SOCK_STREAM) as sock:
        
            sock.settimeout(2.0)

            try:
                sock.connect((self.addr, port))
                self.results.append(port)
            except ConnectionRefusedError or TimeoutError:
                pass
                
if __name__ == '__main__':
    handler: Scanner = Scanner()
    while 1:
        print(f'{Colors.LIGHTPINK}Scanning for services...{Colors.WHITE}')
        handler.addr: str = input(f'{Colors.PINK}ADDR:{Colors.WHITE} ')
        start:        int = time.time()
        handler.get_results()
        if not handler.results:
            print(f'{Colors.RED}Failed to find services.{Colors.WHITE}\n')
        else:
            print(f'{Colors.WHITE}{handler.addr}: {f"{Colors.WHITE}, ".join(f"{Colors.LIGHTRED}{str(port)}" for port in handler.results)}\n')
        end: int = time.time()
        print(f'{Colors.RED}Execution time: {Colors.PINK}{end - start} {Colors.RED}seconds.')
