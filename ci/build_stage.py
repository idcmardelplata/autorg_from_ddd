import sys
import dagger
import anyio

async def build_package():
    config = dagger.Config(log_output=sys.stdout)

    async with dagger.Connection(config) as client:

        container = (
            client.container()
            .from_("idcmardelplata/poetry:v01")
            .with_directory("/src", client.host().directory("."), exclude=["ci"])
            .with_workdir("/src")
            .with_exec(["poetry", "install"]))

        verify_code = container.with_exec(["poetry", "run", "bandit", "-r", "autorg"])
        build = container.with_exec(["poetry", "run", "autorg"])

        # Verify code vulnerabilities
        await verify_code.stderr()

        # Run the code
        await build.stdout()


async def main():
    await build_package()


anyio.run(main)
