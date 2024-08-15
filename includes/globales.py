import os.path

# RUTAS -------------------------------------
RUTA_CARPETA = os.getcwd()
RUTA_SRC = os.path.join(RUTA_CARPETA, 'src')
RUTA_IMG = os.path.join(RUTA_SRC, 'img')
RUTA_IMG_USUARIOS = os.path.join(RUTA_IMG, 'usuarios')

# FUENTES -----------------------------------
FONT_LOGIN_H1 = ("Poppins Medium", 20)
FONT_LOGIN_H2 = ("Poppins Light", 12)
FONT_LOGIN_P = ("Poppins Light", 10)

FONT_APP_H1 = ('Helvetica', 18, "bold")
FONT_APP_H2 = ('Helvetica', 15, "bold")
FONT_APP_H3 = ('Helvetica', 12, "bold")
FONT_APP_H4 = ('Helvetica', 12)
FONT_APP_H5 = ('Helvetica', 10, 'bold')
FONT_APP_P = ('Helvetica', 10)
FONT_APP_PG = ('Helvetica', 15)

# COLORES -----------------------------------
COLOR_AZUL_PRIMARIO = '#1269CD'
COLOR_AZUL_OSCURO = '#3055A0'
COLOR_AZUL_1 = '#3e61a6'
COLOR_AZUL_2 = '#84a4cc'
COLOR_AZUL_3 = '#7697c7'
COLOR_ROJO_PRIMARIO = '#ED1D24'
COLOR_ROJO_OSCURO = '#CB2128'
COLOR_ROJO_1 = '#d1383e'
COLOR_ROJO_2 = '#da6065'
COLOR_ROJO_3 = '#e3888b'

COLOR_DANGER = '#d7191c'
COLOR_SUCCESS = '#28a745'

# TAMAÑO --------------------------------------
W_LOGIN = 950
H_LOGIN = 550


def centrarVentana(root, width, height):
    X_VENTANA_LOGIN = root.winfo_screenwidth() // 2 - width // 2
    Y_VENTANA_LOGIN = root.winfo_screenheight() // 2 - height // 2
    POSICION_LOGIN = str(width) + 'x' + str(height) + '+' + str(X_VENTANA_LOGIN) + '+' + str(Y_VENTANA_LOGIN)
    
    return POSICION_LOGIN