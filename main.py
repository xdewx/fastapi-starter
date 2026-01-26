import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from typer import Typer

from conf import STATIC_DIR

# TODO: i don't want to add this manually, but i have no idea how to do it automatically at present
sys.path.append(str(Path(__file__).parent / "src"))

# print(sys.path)

from biz import demo_biz_add

app = FastAPI()
app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")


cmd = Typer()

@cmd.command()
def add(a: int, b: int) -> int:
    return demo_biz_add(a, b)


@cmd.command()
def sub(a: int, b: int) -> int:
    c = a - b
    print(f"sub({a}, {b}) = {c}")
    return c


@cmd.command()
def version():
    from my_sdk.version import version

    print(version)


@cmd.command()
def setup_db():
    from conf import setup_database

    setup_database()


@cmd.command()
def serve(host: str = "0.0.0.0", port: int = 8000):
    from conf import setup_database

    setup_database()

    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    cmd()
