import flet as ft


def main(page: ft.Page):
    page.bgcolor="blue"
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))


ft.app(main)
