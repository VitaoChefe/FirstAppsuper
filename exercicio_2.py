import flet as ft


def main(page: ft.Page):
     # Configuração da página
     page.title = "Minha Aplicação Flet"
     page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
     page.window.width = 375
     page.window.height = 667

    #Definição de funções
     def mostrar_numero(e):
         txt_resultado.value = input_numero.value
         page.update()
     def par_impar(e):
         valor = input_numero.value
         if int(valor) % 2 == 0:
             txt_resultado.value = "Par"
             page.update()
         else:
             txt_resultado.value = "Impar"
             page.update()


    #Criação de componentes
     input_numero = ft.TextField(label="Número", hint_text="Digita o número")
     btn_enviar = ft.FilledButton(
         text="Enviar",
         width=page.window.width,
         on_click=par_impar,
     )
     txt_resultado = ft.Text(value="")
    #Construir o layout
     page.add(
          ft.Column(
               [
                    input_numero,
                    btn_enviar,
                    txt_resultado,

               ]
          )
     )
ft.app(main)