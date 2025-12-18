from biz import demo_biz_add

from typer import Typer

app = Typer()


@app.command()
def add(a: int, b: int) -> int:
    return demo_biz_add(a, b)


@app.command()
def sub(a: int, b: int) -> int:
    c = a - b
    print(f"sub({a}, {b}) = {c}")
    return c


if __name__ == "__main__":
    app()
