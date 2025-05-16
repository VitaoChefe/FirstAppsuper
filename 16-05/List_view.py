import flet as ft
from flet import AppBar, Text, View
from flet.auth import user
from flet.core.colors import Colors

class User():
    def __init__(self, nome, salario,cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo


def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Listas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []

    def salvar_nome(e):
        if input_nome.value == "":
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()

        else:
            obj_User = User(
                nome=input_nome.value,
                salario=input_salario.value,
                cargo=input_cargo.value,
            )
            lista.append(obj_User)
            input_nome.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()


    def exibir_lista(e):
        lv_nome.controls.clear()
        for user in lista:
            lv_nome.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.icons.PERSON),
                    title=ft.Text(f"Nome - {user.nome}"),

                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text="Detalhes",
                                             on_click=lambda _: page.go('/terceira')
                                             ),

                        ],
                    )

                )
            )
        page.update()


    def exibir_informacoes(e):
        lv_nome.controls.clear()
        for user in lista:
            lv_nome.controls.append(
                ft.Text(f"Nome - {user.nome}\n" f'Profissão - {user.cargo}\n'f'Salário - {user.salario}\n',
                            ),

            )


    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    input_cargo,
                    input_salario,
                    ft.Button(
                        text="Salvar",
                        on_click=lambda _: salvar_nome(e)
                    ),
                    ft.Button(
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
                       lv_nome
                    ],
                )
            )
            if page.route == "/terceira":
                exibir_informacoes(e)
                page.views.append(
                    View(
                         '/Terceira',
                        [
                            AppBar(title=Text("Terceira"), bgcolor=Colors.PRIMARY_CONTAINER),
                            lv_nome

                        ]

                    )
                )
        page.update()


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

    input_nome = ft.TextField(label="nome")
    input_salario = ft.TextField(label="salario")
    input_cargo = ft.TextField(label="cargo")

    lv_nome = ft.ListView(height=500)
    page.add(
        ft.Column(
            [
                input_nome,
                input_salario,
                input_cargo,
                lv_nome,

            ]
        )
    )

    text_resultado = ft.Text("sou um texto")

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)
