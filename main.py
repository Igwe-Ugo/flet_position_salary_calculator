import flet as ft
from predictions import predict_salaries, pos

# Constants for styling
LINK_STYLE = {
    "height": 46.47,
    "width": 301.56,
    "focused_border_color": '#e3e3e3',
    "border_radius": 3.54,
    "content_padding": 10,
    "border_width": 1.5,
    "text_size": 14,
    "label_style": ft.TextStyle(color='#a3a3a3')
}

BUTTON_STYLE = {
    "height": 46.06,
    "border_radius": 5,
    "bgcolor": "#DB0004",
    "padding": ft.padding.only(top=8.53, bottom=9.52)
}

CARD_STYLE = {
    "width": 340,
    "elevation": 5
}

def main(page: ft.Page):
    # Page setup
    page.title = "SMILES COOPERATION"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT

    # Create position options from the imported data
    position_options = [
        ft.dropdown.Option(position) for position in pos
    ]

    # Dropdown for positions
    position_dropdown = ft.Dropdown(
        label="POSITION",
        options=position_options,
        **LINK_STYLE
    )

    # Result card (initially hidden)
    result_position = ft.Text("", size=16)
    result_salary = ft.Text("", size=16)
    
    result_card = ft.Card(
        color=ft.Colors.WHITE,
        width=340,
        elevation=5,
        visible=False,
        content=ft.Container(
            padding=20,
            content=ft.Column(
                [
                    ft.Text("RESULT", size=18, weight=ft.FontWeight.BOLD),
                    ft.Divider(),
                    ft.Row([
                        ft.Text("POSITION: ", size=16, weight=ft.FontWeight.BOLD),
                        result_position
                    ]),
                    ft.Row([
                        ft.Text("PROSPECTIVE INCOME: ", size=16, weight=ft.FontWeight.BOLD),
                        result_salary
                    ])
                ],
                spacing=10
            )
        )
    )

    def submit_clicked(e):
        # Validate inputs
        if not name.value:
            name.error_text = "Please enter your name"
            page.update()
            return
        if not email.value:
            email.error_text = "Please enter your email"
            page.update()
            return
        if not position_dropdown.value:
            position_dropdown.error_text = "Please select a position"
            page.update()
            return
            
        # Clear any previous errors
        name.error_text = None
        email.error_text = None
        position_dropdown.error_text = None
        
        # Get the selected position level (index + 1 since levels start at 1)
        position_level = pos.tolist().index(position_dropdown.value) + 1
        
        # Predict salary
        predicted_salary = predict_salaries(position_level)[0]
        
        # Update result card
        result_position.value = position_dropdown.value
        result_salary.value = f"${predicted_salary:,.2f}"
        result_card.visible = True
        page.update()

    # Title components
    title = ft.Text(
        "SMILES COOPERATION",
        size=21.23,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    subtitle = ft.Text(
        "SALARY CALCULATOR",
        size=18,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.LEFT
    )

    # Form fields
    name = ft.TextField(label='NAME', **LINK_STYLE)
    email = ft.TextField(label='EMAIL', **LINK_STYLE)

    # Submit button
    submit_button = ft.Container(
        **BUTTON_STYLE,
        expand=True,
        content=ft.Text(
            'SUBMIT',
            color=ft.Colors.WHITE,
            size=18,
            text_align=ft.TextAlign.CENTER,
        ),
        on_click=submit_clicked,
    )

    # Form layout
    form_card = ft.Card(
        **CARD_STYLE,
        content=ft.Container(
            padding=ft.padding.only(left=25, right=25, top=30, bottom=30),
            content=ft.Column(
                controls=[
                    subtitle,
                    ft.Column(
                        spacing=30,
                        controls=[
                            name,
                            email,
                            position_dropdown,
                            ft.Row(
                                controls=[
                                submit_button
                                ],
                                alignment='center',
                                vertical_alignment='center'
                            ),
                        ]
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.START
            )
        )
    )

    # Title card
    title_card = ft.Card(
        **CARD_STYLE,
        content=ft.Container(
            padding=ft.padding.only(left=32, right=20, top=29, bottom=19),
            content=title,
        )
    )

    # Main page layout
    page.add(
        ft.Column(
            controls=[
                title_card,
                form_card,
                result_card  # Add result card to the form flow
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
