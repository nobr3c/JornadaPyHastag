
# pip install flet -> no terminal 

# Titulo Hashzap
# Botão de iniciar o chat 
    # Popup
        # Bem vindo ao Hashzap
        # Escreva seu nome 
        # Entrar no chat 
# Chat
    # Fulano entrou no chat
    # Mensagens do usuário 
# Campo para enviar mensagem
# Botão de enviar


import flet as ft

def main(pagina):
    titulo  = ft.Text("Hashzap")  

    nome_usuario = ft.TextField(label="Escreva seu nome")

    chat = ft.Column()

    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update

    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        # Colocar o nome do usuário na mensagem 
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"      
        pagina.pubsub.send_all(texto_campo_mensagem)
        # Limpar o campo_mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    

    def entrar_chat(evento):
        # feche o popup
         popup.open = False
        # tire o botão "Iniciar chat" da tela
         pagina.remove(botao_iniciar)
        # Adicionar o nosso chat
         pagina.add(chat)
        # criar o campo de enviar mensagem
         linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
         )
         
        # botao de enviar mensagem
         pagina.add(linha_mensagem) 
        # botao de enviar mensagem
         texto = f"{nome_usuario.value} entrou no chat"
         pagina.pubsub.send_all(texto)
         pagina.update()

    popup = ft.AlertDialog(
        open = False, 
        modal = True,
        title = ft.Text("Bem vindo ao Hashzap"),
        content = nome_usuario,
        actions=[ft.ElevatedButton("Entrar,", on_click=entrar_chat)]
        )

    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click= iniciar_chat)

    pagina.add(titulo)
    pagina.add(botao_iniciar)

#ft.app(main)
ft.app(main, view=ft.WEB_BROWSER )