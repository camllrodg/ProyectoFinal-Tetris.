#Para colocarle color a las piezas.
class Colors: 
    dark_grey=(26, 31,40)
    green=(47, 230, 23)
    red=(232, 18, 18)
    orange=(226, 116, 17)
    yellow=(237, 234, 4)
    purple=(166, 0, 247)
    cyan=(21, 204, 209)
    dark_blue=(13, 64, 216)
    brown=(147,81,22)
    pink=(234,15,108)
    white=(255,255,255)
    blue=(44,44,127)
    light_blue=(59,85,162)
    dark=(0,0,0)
    b=(23,32,42)
    e=(41, 128, 185) 
    f=(39, 55, 70)
    d=(40, 116, 166)
    
    @classmethod 
    def get_cells_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.dark_blue,cls.brown,cls.pink]