"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

color_button_style = {
    "position": "fixed",
    "right": "2em",
    "top": "2em",
    "background": "transparent",
    "color": rx.color("gray", 12),
}

link_style = {
    "border": "0.1em solid",
    "padding": "0.5em",
    "border_radius": "0.5em",
    "_hover": {"color": rx.color("accent", 9)},
}


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(rx.color_mode.icon(), style=color_button_style),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text("Get started by editing ", rx.code(filename), size="5"),
            rx.link("Check out our docs!", href=docs_url, style=link_style),
            spacing="5",
            justify="center",
            min_height="90vh",
        ),
        rx.logo(),
    )


# Create app instance and add index page.
app = rx.App()
app.add_page(index)
