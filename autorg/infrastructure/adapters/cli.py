import click
from autorg.application.dtos.input_dto import InputDto, make_dto_from_input

from autorg.application.input import AppInput
from autorg.infrastructure.adapters.csvrepository import CsvRepository


@click.group
def autorg():
    pass


@autorg.group
def inbox():
    pass

@inbox.command(name="add", help="add a input to inbox")
@click.argument("input_")
def add_command(input_: str):
    try:
        app = AppInput(CsvRepository())
        app.add_input(input_)
        click.echo("The input was saved correctly", color=True)
    except Exception as err:
        click.echo(f"Failed adding input, err={err}", color=True)

@inbox.command(name="ls", help="show all inputs in the inbox")
def ls_command():
    app = AppInput(CsvRepository())
    inputs: list[str] = [make_dto_from_input(inp).content for inp in app.list_inputs()]

    if len(inputs) == 0:
        click.echo("Not inputs found")
    else:
        for item in inputs:
            print(item)

if __name__ == "__main__":
    autorg()
