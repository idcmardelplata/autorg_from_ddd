import click

from autorg.application.input import AppInput
from autorg.infrastructure.adapters.csvrepository import CsvRepository


@click.group
def autorg():
    pass


@click.command(name="input")
@click.argument("body")
def inbox(body: str):
    try:
        app = AppInput(CsvRepository())
        app.add_input(body)
        click.echo("The input was saved correctly", color=True)
    except Exception as err:
        click.echo(f"Failed adding input, err={err}", color=True)

@click.command(name="inbox-list")
# @click.argument("filtre")
def inbox_list():
    app = AppInput(CsvRepository())
    click.echo(app.list_inputs())


# class InboxCmd(click.MultiCommand):
#     def add(self, _, body: str):
#         try:
#             app = AppInput(CsvRepository())
#             app.add_input(body)
#             click.echo("The input was saved correctly", color=True)
#         except Exception as err:
#             click.echo(f"Failed adding input, err={err}", color=True)
#

if __name__ == "__main__":
    inbox = InboxCmd(help="Permite gestionar la bandeja de entrada")
    # inbox()
    autorg.add_command(inbox)
    # autorg()
