import click

from app import app
from app.data import cv_data
from app.helpers import format_key


@click.command()
def print_cv_data() -> None:
    try:
        for key, value in cv_data.items():
            click.echo(f"\n{format_key(key)}: \n")
            display_categories(value)
    except:
        click.echo("Wrong data format!")


def display_categories(category) -> None:
    for item in category:
        if isinstance(item, str):
            click.echo(f"{format_key(item)}: {category[item]}")
        else:
            display_categories(item)


app.cli.add_command(print_cv_data)
