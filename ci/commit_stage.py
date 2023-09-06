import sys
from typing import Dict
import dagger
import anyio

async def run(command: str):

    config = dagger.Config(log_output=sys.stdout)
    async with dagger.Connection(config) as client:
        cache = client.cache_volume("pip")
        python = (
            client.container()
            .from_("idcmardelplata/poetry:v01")
            .with_directory("/src", client.host().directory("."), exclude=["ci/"])
            .with_workdir("/src")
            .with_env_variable("POETRY_CACHE_DIR", "/src/.cache")
            .with_mounted_cache("/src/.cache", cache)
            .with_exec(["poetry", "install", "--no-root"])
            .with_mounted_cache("/src/.cache", cache)
        )

        linter = ( python.with_exec(["poetry", "run", "black", "."]))
        unittest = ( python.with_exec(["poetry", "run", "pytest"]))

        options = {'linter': linter.stdout, 'unittest': unittest.stderr}

        if command == 'both':
            await linter.stdout()
            await unittest.stderr()
        else:
            await options.get(command)()


async def main():
    await run("both")

anyio.run(main)
