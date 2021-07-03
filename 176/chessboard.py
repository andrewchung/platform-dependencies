WHITE, BLACK = ' ', '#'

odd = WHITE + BLACK
even = BLACK + WHITE

def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    
    for i in range(size // 2):
       if size % 2 == 0:
         print(odd * (size // 2))
         print(even * (size // 2))
