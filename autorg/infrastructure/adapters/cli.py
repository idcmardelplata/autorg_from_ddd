import click

from autorg.application.input import AppInput
from autorg.infrastructure.adapters.csvrepository import CsvRepository

@click.group
def autorg():
    pass

@click.command(name="input")
@click.argument("body")
def cmd_input(body: str):
    try:
        app = AppInput(CsvRepository())
        app.add_input(body)
        click.echo("The input was saved correctly", color=True)
    except Exception as err:
        click.echo(f"Failed adding input, err={err}", color=True)

@click.command(name="inbox-list")
@click.argument("filtre")
def inbox_list(filtre:str):
    app = AppInput(CsvRepository())
    click.echo(app.list_inputs())


if __name__ == "__main__":
    autorg.add_command(cmd_input)
    autorg()
