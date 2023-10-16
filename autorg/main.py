import anyio
from autorg.infrastructure.adapters.cli import autorg

async def main():
    autorg()

if __name__ == "__main__":
    anyio.run(main)
