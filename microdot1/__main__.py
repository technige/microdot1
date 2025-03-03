from asyncio import run

from microdot1 import app


async def main():
    await app.start_server(port=8080, debug=True)


if __name__ == "__main__":
    run(main())
