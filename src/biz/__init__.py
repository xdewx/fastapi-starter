from ipa.decorator import deprecated

from sdk import add


@deprecated("use sdk.add instead")
def demo_biz_add(a: int, b: int) -> int:
    c = add(a, b)
    print(f"add({a}, {b}) = {c}")
    return c
