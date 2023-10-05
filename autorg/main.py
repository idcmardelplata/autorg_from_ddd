from UnleashClient import UnleashClient
from dotenv import load_dotenv
import os


def configure_flags():
    load_dotenv()

    client = UnleashClient(
        url="http://localhost:4242/api",
        app_name="Default",
        custom_headers={"Authorization": os.environ["API_KEY"]},
    )

    client.initialize_client()
    return client


def main():
    load_dotenv()

    try:
        client = configure_flags()

        if client.is_enabled("test-flag"):
            print(f"test-flag is enabled")
        else:
            print("test-flag is disabed")
    except Exception as error:
        print(f"Error getting feature-flag configuration: {error}")


main()
