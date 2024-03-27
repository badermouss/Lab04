import flet as ft


class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'LEFT'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch

        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here
        # Row 1
        def dropdown_changed_language(e):
            t_1.value = f"Language changed to {dd.value}"
            self.update()

        def dropdown_changed_search(e):
            t_2.value = f"Search changed to {dd_typeS.value}"
            self.update()

        def clear_page(e):
            lv.controls.clear()
            dd.value = None
            dd_typeS.value = None
            txtIn.value = ""
            t_1.value = ""
            t_2.value = ""
            self.update()

        def copiaInput(e):
            t_copia.value = e.control.value
            self.update()

        def stessaFrase(e):
            txtIn.value = t_copia.value
            self.update()

        def handleSpellCheck(e):
            if txtIn.value == "" or dd.value is None or dd_typeS.value is None:
                lv.controls.append(ft.Text(value="Errore, mancano dei dati", color="red", size=30))
            else:
                parole_sbagliate, tempo = self.__controller.handleSentence(txtIn.value.lower(), dd.value.lower(),
                                                                           dd_typeS.value)
                lv.controls.append(ft.Text(value=f"Frase inserita: {txtIn.value}", size=20))
                lv.controls.append(ft.Text(value=f"Parole errate: {parole_sbagliate}", size=20))
                lv.controls.append(
                    ft.Text(value=f"Tempo richiesto dalla ricerca: {tempo} ({dd_typeS.value} research)", size=20))
            txtIn.value = ""
            self.update()

        t_1 = ft.Text(size=15, italic=True)
        dd = ft.Dropdown(width=1000, label="Language", hint_text="choose the language you want",
                         on_change=dropdown_changed_language,
                         options=[ft.dropdown.Option("Italian"),
                                  ft.dropdown.Option("English"),
                                  ft.dropdown.Option("Spanish")])
        r1 = ft.Row([dd])

        # Row 2
        t_2 = ft.Text(size=15, italic=True)
        dd_typeS = ft.Dropdown(width=200, label="Search modality", hint_text="Choose how to search",
                               on_change=dropdown_changed_search,
                               options=[ft.dropdown.Option("Default"),
                                        ft.dropdown.Option("Linear"),
                                        ft.dropdown.Option("Dichotomic")])

        txtIn = ft.TextField(label="Frase da correggere", hint_text="scrivi una frase da correggere",
                             on_change=copiaInput)
        t_copia = ft.Text()

        btn = ft.ElevatedButton(text="submit", on_click=handleSpellCheck)
        lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        btn_clear = ft.ElevatedButton(text="clear", on_long_press=clear_page)
        r2 = ft.Row([dd_typeS, txtIn, btn, btn_clear])

        # Row 3
        btn_repeat = ft.ElevatedButton(text="repeat", on_click=stessaFrase)
        self.page.add(r1, t_1, r2, t_2, btn_repeat, lv)

        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
