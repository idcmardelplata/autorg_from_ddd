import sys
import dagger
import anyio

async def run(command: str):

    config = dagger.Config(log_output=sys.stdout)
    async with dagger.Connection(config) as client:
        cache = client.cache_volume("pip")
        python = (
            client.container()
            .from_("idcmardelplata/poetry:v01")
            .with_workdir("/src")
            .with_directory("/src", client.host().directory("."), exclude=["__pycache__", "ci", "diagrams", "docs", "build", "dist"])
            .with_env_variable("POETRY_CACHE_DIR", "/src/.cache")
            .with_mounted_cache("/src/.cache", cache)
            .with_exec(["poetry", "install", "--no-root"])
            .with_mounted_cache("/src/.cache", cache)
        )

        linter = ( python.with_exec(["poetry", "run", "black", "."]))
        unittest = ( python.with_exec(["poetry", "run", "pytest"]))
        vulture = (python.with_exec(["poetry", "run", "vulture", "autorg", "tests"]))

        options = {'linter': linter.stdout, 'unittest': unittest.stderr}

        if command == 'all':
            await linter.stdout()
            await unittest.stderr()
            await vulture.stderr()
        else:
            await options.get(command)()


async def main():
    await run("all")

anyio.run(main)
