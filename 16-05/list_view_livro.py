import flet as ft
from flet import AppBar, Text, View, ListView
from models import *
from flet.core.colors import Colors
from sqlalchemy import select


def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Listas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []

    def salvar_livro(e):
        if input_nome_do_livro.value == "" or input_autor.value == "" or input_categoria.value == "" or input_descricao.value == "":
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
            return

        else:
            obj_livro = Livro(
                titulo=input_nome_do_livro.value,
                autor=input_autor.value,
                categoria=input_categoria.value,
                descricao=input_descricao.value,

            )
            obj_livro.save()
            input_nome_do_livro.value = ""
            input_autor.value = ""
            input_categoria.value = ""
            input_descricao.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()


    def exibir_lista(e):
        lv_livro.controls.clear()
        livro = select(Livro)
        livros = db_session.execute(livro).scalars().all()
        for l in livros:
            lv_livro.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.icons.BOOK_OUTLINED),
                    title=ft.Text(f"{l.titulo}"),
                    subtitle=ft.Text(f"{l.autor}"),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.INFO_OUTLINE,
                        items=[
                            ft.PopupMenuItem(text="Detalhes")
                            ],
                            on_select=lambda _, liv=l: exibir_informacoes(liv.titulo, liv.autor, liv.descricao, liv.categoria),
                            )
                    )

                )
        page.update()


    def exibir_informacoes(titulo, autor, categoria, descricao):
        text_resultado.value = (f"titulo: {titulo} - autor: {autor} - categoria: {categoria} - descricao: {descricao}")
        page.update()
        page.go('/terceira')


    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Livro"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome_do_livro,
                    input_autor,
                    input_categoria,
                    input_descricao,
                    ft.ElevatedButton(
                        text="Salvar",
                        on_click=lambda _: salvar_livro(e),
                    ),
                    ft.ElevatedButton(
                        text="Exibir Lista",
                        on_click=lambda _: page.go("/segunda"),
                    )
                ],
            )
        )
        if page.route == "/segunda" or page.route == "/terceira":
            exibir_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                       lv_livro
                    ],
                )
            )
        page.update()
        if page.route == "/terceira":
            page.views.append(
                View(
                    '/Terceira',
                    [
                        AppBar(title=Text("Terceira"), bgcolor=Colors.PRIMARY_CONTAINER),
                        text_resultado
                    ]
                )
            )


    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # Componentes
    msg_sucesso = ft.SnackBar(
        content=ft.Text("Nome salvo com sucesso"),
        bgcolor=Colors.GREEN
    )

    msg_error = ft.SnackBar(
        content=ft.Text("Nome não pode ser vazio "),
        bgcolor=Colors.RED
    )

    input_nome_do_livro = ft.TextField(label="nome")
    input_autor = ft.TextField(label="autor")
    input_descricao = ft.TextField(label="descricao")
    input_categoria = ft.TextField(label="categoria")

    lv_livro = ft.ListView(
        height=500,
        spacing=2,
        divider_thickness=3
    )
    text_resultado = ft.Text("")

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)

