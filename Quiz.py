import flet as ft

# Lista de perguntas e respostas
questions = [
    {
        "question": "Qual é a capital da França?",
        "options": ["Londres", "Paris", "Roma", "Berlim"],
        "answer": "Paris"
    },
    {
        "question": "Qual é o maior planeta do sistema solar?",
        "options": ["Terra", "Marte", "Júpiter", "Saturno"],
        "answer": "Júpiter"
    },
    {
        "question": "Quem desenvolveu a teoria da relatividade?",
        "options": ["Newton", "Einstein", "Galileu", "Tesla"],
        "answer": "Einstein"
    },
    {
        "question": "Qual é a moeda do Japão?",
        "options": ["Dólar", "Yuan", "Iene", "Euro"],
        "answer": "Iene"
    },
    {
        "question": "Qual é o continente mais populoso?",
        "options": ["África", "América", "Ásia", "Europa"],
        "answer": "Ásia"
    },
    {
        "question": "Qual é a fórmula da água?",
        "options": ["H2O", "CO2", "O2", "NaCl"],
        "answer": "H2O"
    },
    {
        "question": "Quem pintou a Mona Lisa?",
        "options": ["Van Gogh", "Picasso", "Da Vinci", "Michelangelo"],
        "answer": "Da Vinci"
    },
    {
        "question": "Qual é o elemento químico com o símbolo O?",
        "options": ["Ouro", "Oxigênio", "Osmônio", "Ósmio"],
        "answer": "Oxigênio"
    },
    {
        "question": "Qual é o rio mais longo do mundo?",
        "options": ["Nilo", "Amazonas", "Yangtze", "Mississippi"],
        "answer": "Amazonas"
    },
    {
        "question": "Qual é a montanha mais alta do mundo?",
        "options": ["K2", "Kilimanjaro", "Everest", "Makalu"],
        "answer": "Everest"
    },
    {
        "question": "Qual é a língua mais falada do mundo?",
        "options": ["Inglês", "Chinês", "Espanhol", "Árabe"],
        "answer": "Inglês"
    },
    {
        "question": "Qual país é conhecido como a terra do sol nascente?",
        "options": ["China", "Coreia do Sul", "Japão", "Tailândia"],
        "answer": "Japão"
    },
    {
        "question": "Qual é o maior oceano do mundo?",
        "options": ["Atlântico", "Índico", "Ártico", "Pacífico"],
        "answer": "Pacífico"
    },
    {
        "question": "Qual é o metal mais leve?",
        "options": ["Alumínio", "Lítio", "Ferro", "Cobre"],
        "answer": "Lítio"
    },
    {
        "question": "Em que ano o homem pisou na Lua pela primeira vez?",
        "options": ["1965", "1969", "1971", "1975"],
        "answer": "1969"
    },
    {
        "question": "Qual é a capital da Austrália?",
        "options": ["Sydney", "Canberra", "Melbourne", "Brisbane"],
        "answer": "Canberra"
    },
    {
        "question": "Qual é o maior animal terrestre?",
        "options": ["Elefante", "Girafa", "Urso", "Rinoceronte"],
        "answer": "Girafa"
    },
    {
        "question": "Qual é a principal fonte de energia da Terra?",
        "options": ["Carvão", "Petróleo", "Sol", "Água"],
        "answer": "Sol"
    },
    {
        "question": "Quem é o autor de 'Dom Casmurro'?",
        "options": ["Machado de Assis", "José de Alencar", "Graciliano Ramos", "Jorge Amado"],
        "answer": "Machado de Assis"
    },
    {
        "question": "Qual é o país mais extenso do mundo?",
        "options": ["Estados Unidos", "China", "Rússia", "Brasil"],
        "answer": "Rússia"
    },
    {
        "question": "Quem foi o primeiro presidente do Brasil?",
        "options": ["Getúlio Vargas", "Deodoro da Fonseca", "Juscelino Kubitschek", "Fernando Henrique Cardoso"],
        "answer": "Deodoro da Fonseca"
    }
]

def main(page: ft.Page):
    page.title = "Quiz Estilo Kahoot com Login"
    page.window_width = 1920
    page.window_height = 1080
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Função para criar a tela de login
    def login_screen():
        page.controls.clear()

        # Função para iniciar o quiz
        def start_quiz(e):
            user_name = name_field.value
            user_class = class_field.value
            if user_name and user_class:
                quiz_screen(user_name, user_class)  # Passa o nome e a turma para a tela do quiz
            else:
                error_text.value = "Por favor, preencha todos os campos!"
                error_text.update()

        # Campos de nome e turma
        name_field = ft.TextField(label="Nome", width=400)
        class_field = ft.TextField(label="Turma", width=400)
        error_text = ft.Text("", size=18, color="red")
        
        # Botão de iniciar
        start_button = ft.ElevatedButton(text="Iniciar Quiz", on_click=start_quiz)

        # Adiciona os elementos à tela de login
        page.add(
            ft.Column([
                ft.Text("Bem-vindo ao Quiz", size=30, weight="bold", color="blue"),
                name_field,
                class_field,
                error_text,
                start_button
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )

        page.update()

    # Função para criar a tela do quiz
    def quiz_screen(user_name, user_class):
        current_question = 0
        score = 0

        page.controls.clear()

        question_text = ft.Text(questions[current_question]["question"], size=24, weight="bold", color="blue")
        options_buttons = []

        # Função para verificar a resposta
        def check_answer(selected_option):
            nonlocal current_question, score
            if selected_option == questions[current_question]["answer"]:
                score += 1
                result_text.value = "Você acertou!"
                result_text.color = "green"
            else:
                result_text.value = "Resposta incorreta!"
                result_text.color = "red"

            result_text.update()

            # Carrega a próxima pergunta ou exibe a pontuação final
            current_question += 1
            if current_question < len(questions):
                load_question()
            else:
                question_text.value = f"Quiz terminado, {user_name}! Sua pontuação: {score}/{len(questions)}"
                question_text.update()
                for button in options_buttons:
                    button.visible = False

        # Função para carregar uma nova pergunta
        def load_question():
            question_text.value = questions[current_question]["question"]
            for idx, option in enumerate(questions[current_question]["options"]):
                options_buttons[idx].text = option
                options_buttons[idx].on_click = lambda e, opt=option: check_answer(opt)
                options_buttons[idx].update()
            result_text.value = ""
            result_text.update()
            question_text.update()

        # Adiciona os elementos à interface do quiz
        page.add(ft.Text(f"Nome: {user_name} | Turma: {user_class}", size=18, color="gray", italic=True))
        page.add(question_text)
        for option in questions[0]["options"]:
            button = ft.ElevatedButton(text=option, width=400)
            options_buttons.append(button)
            page.add(button)

        result_text = ft.Text("", size=20, color="black")
        page.add(result_text)

        # Carrega a primeira pergunta
        load_question()

    # Inicializa com a tela de login
    login_screen()

# Executa o aplicativo Flet
ft.app(target=main)