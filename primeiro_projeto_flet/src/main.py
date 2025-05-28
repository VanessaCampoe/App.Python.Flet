import flet as ft


def main(page: ft.Page):
    page.title = "hello World em Flet"
    page.add(
        ft.SafeArea(
            ft.Text(
                " Aló, mundo em Flet!!",
                size=50,
                weight="bold"
            )
        )
    )


ft.app(target=main)
