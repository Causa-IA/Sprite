import flet as ft

from funciones import (
    binario_a_hexadecimal,
    hexadecimal_a_binario,
    hexadecimal_valido
)


def main(page: ft.Page):

    # ==================================================
    # CONFIGURACIÓN DE LA VENTANA
    # ==================================================

    page.title = "Matriz LED 8x8"
    page.theme_mode = ft.ThemeMode.DARK

    page.window.width = 700
    page.window.height = 850
    page.window.resizable = False


    # ==================================================
    # COLORES DE LOS PÍXELES
    # ==================================================

    COLOR_APAGADO = "#1E293B"
    COLOR_ENCENDIDO = "#39FF14"


    # ==================================================
    # TÍTULO
    # ==================================================

    titulo = ft.Text(
        "Matriz LED 8 × 8",
        size=30,
        weight=ft.FontWeight.BOLD
    )


    # ==================================================
    # MATRIZ 8 × 8
    # ==================================================

    grid = ft.GridView(
        runs_count=8,
        max_extent=48,
        spacing=4,
        run_spacing=4,
        width=410,
        height=410
    )


    # Lista que almacenará los 64 píxeles
    pixeles = []


    # ==================================================
    # TEXTO BINARIO
    # ==================================================

    etiqueta_binario = ft.Text(
        "BINARIO (64 bits)",
        size=17,
        weight=ft.FontWeight.BOLD
    )

    binario_texto = ft.Text(
        "0" * 64,
        size=12,
        selectable=True
    )


    # ==================================================
    # TEXTO HEXADECIMAL
    # ==================================================

    etiqueta_hexadecimal = ft.Text(
        "HEXADECIMAL (16 caracteres)",
        size=17,
        weight=ft.FontWeight.BOLD
    )

    hex_texto = ft.Text(
        "0000000000000000",
        size=23,
        weight=ft.FontWeight.BOLD
    )


    # ==================================================
    # MENSAJE
    # ==================================================

    mensaje = ft.Text(
        "",
        size=14
    )


    # ==================================================
    # FUNCIÓN PARA ACTUALIZAR BINARIO Y HEXADECIMAL
    # ==================================================

    def actualizar_valores():

        binario = ""

        # Recorrer los 64 píxeles
        for pixel in pixeles:

            if pixel.bgcolor == COLOR_ENCENDIDO:
                binario += "1"

            else:
                binario += "0"


        # Convertir binario → hexadecimal
        hexadecimal = binario_a_hexadecimal(binario)


        # Actualizar interfaz
        binario_texto.value = binario
        hex_texto.value = hexadecimal


    # ==================================================
    # EVENTO DE LOS PÍXELES
    # ==================================================

    def cambiar_pixel(e):

        pixel = e.control

        # Si está apagado → encender
        if pixel.bgcolor == COLOR_APAGADO:

            pixel.bgcolor = COLOR_ENCENDIDO

        # Si está encendido → apagar
        else:

            pixel.bgcolor = COLOR_APAGADO


        # Actualizar valores
        actualizar_valores()

        # Actualizar pantalla
        page.update()


    # ==================================================
    # CREAR LOS 64 PÍXELES
    # ==================================================

    for fila in range(8):

        for columna in range(8):

            pixel = ft.Container(
                width=45,
                height=45,
                bgcolor=COLOR_APAGADO,
                border_radius=5,
                on_click=cambiar_pixel
            )

            # Guardar píxel
            pixeles.append(pixel)

            # Agregarlo a la cuadrícula
            grid.controls.append(pixel)


    # ==================================================
    # CAMPO PARA HEXADECIMAL
    # ==================================================

    hex_input = ft.TextField(
        label="Código hexadecimal",
        hint_text="Ej: FFFFFFFFFFFFFFFF",
        width=300,
        max_length=16
    )


    # ==================================================
    # FUNCIÓN CARGAR HEX
    # ==================================================

    def cargar_hex(e):

        # Obtener texto
        hexadecimal = hex_input.value.strip().upper()


        # ------------------------------------------------
        # VALIDAR HEXADECIMAL
        # ------------------------------------------------

        if not hexadecimal_valido(hexadecimal):

            mensaje.value = (
                "Error: hexadecimal inválido. "
                "Use de 1 a 16 caracteres: 0-9, A-F."
            )

            page.update()

            return


        # ------------------------------------------------
        # HEXADECIMAL → BINARIO
        # ------------------------------------------------

        binario = hexadecimal_a_binario(hexadecimal)


        # ------------------------------------------------
        # ACTUALIZAR LOS 64 PÍXELES
        # ------------------------------------------------

        for i in range(64):

            if binario[i] == "1":

                pixeles[i].bgcolor = COLOR_ENCENDIDO

            else:

                pixeles[i].bgcolor = COLOR_APAGADO


        # ------------------------------------------------
        # ACTUALIZAR LOS VALORES
        # ------------------------------------------------

        binario_texto.value = binario

        hex_texto.value = hexadecimal.zfill(16)


        # Limpiar mensaje
        mensaje.value = ""


        # Actualizar pantalla
        page.update()


    # ==================================================
    # BOTÓN CARGAR HEX
    # ==================================================

    boton_cargar = ft.FilledButton(
        content=ft.Text("Cargar Hex"),
        on_click=cargar_hex
    )


    # ==================================================
    # PANEL DE ENTRADA
    # ==================================================

    entrada = ft.Row(
        controls=[
            hex_input,
            boton_cargar
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )


    # ==================================================
    # INFORMACIÓN DE LOS VALORES
    # ==================================================

    informacion = ft.Column(
        controls=[
            etiqueta_binario,
            binario_texto,

            etiqueta_hexadecimal,
            hex_texto,

            mensaje
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=6
    )


    # ==================================================
    # AGREGAR TODO A LA VENTANA
    # ==================================================

    page.add(

        ft.Column(
            controls=[
                titulo,

                entrada,

                informacion,

                grid
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
    )


# ======================================================
# EJECUTAR LA APLICACIÓN
# ======================================================

ft.run(main)