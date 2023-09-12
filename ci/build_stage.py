import sys
import dagger
import anyio

async def build_package():
    config = dagger.Config(log_output=sys.stdout)

    async with dagger.Connection(config) as client:
        build = (
            client.container()
            .from_("idcmardelplata/poetry:v01")
            .with_directory("/src", client.host().directory("."), exclude=["ci"])
            .with_workdir("/src")
            .with_exec(["poetry", "install"])
            # .with_exec(["ls", "dist"]) # Show the whl and tgz output file
            .with_exec(["poetry", "run", "autorg"])
            )
        await build.stdout()

async def main():
    await build_package()


anyio.run(main)
