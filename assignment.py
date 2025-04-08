import flet as ft

def main(page: ft.Page):
    #This is just a comment
    def changeVisibility(e):
        helloText.visible = True
        page.update()
    showMessage = ft.ElevatedButton(text="Show Message", on_click=changeVisibility)
    helloText = ft.Text(value="Adios", visible=False)
    page.add(showMessage, helloText)

ft.app(main)