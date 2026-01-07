from typer import Typer

from biz import demo_biz_add

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
def setup_db():
    from conf import setup_database

    # if you need to use database, invoke setup_database freely
    setup_database()


if __name__ == "__main__":
    cmd()
