import click
import random


class Pizza():
    """The parent class for all pizza types."""
    def __init__(self, size:str) -> None:
        self.ingredients = {"sauce": "tomato sauce", 
            "cheese" : "mozzarella"}

        self.size = size

    def dict(self) -> dict:
        return self.ingredients

    def __eq__(self, other) -> bool:   # не смог сделать typehint Pizza, потому что класс еще не определен
        if self.ingredients == other.ingredients and \
            self.size == other.size:
            return True
        
        return False


class Margherita(Pizza):
    """Margherita pizza."""
    def __init__(self, size:str):
        super().__init__(size)
        self.ingredients["seasoning"] = "tomatoes"


class Pepperoni(Pizza):
    """Pepperoni pizza."""
    def __init__(self, size:str) -> None:
        super().__init__(size)
        self.ingredients["seasoning"] = "pepperoni"


class Hawaiian(Pizza):
    """Hawaiian pizza with pineapple!"""
    def __init__(self, size:str) -> None:
        super().__init__(size)
        self.ingredients["seasoning"] = "pineapples"
        self.ingredients["meat"] = "chicken"


def log(template):
    def log_decorator(func):
        """Determines task completion time and creates a log."""
        def wrapper(*args, **kwargs):
            time = random.randint(20, 60)
            print(template % str(time))
            return func(*args, time, **kwargs)
        return wrapper
    return log_decorator


@log("Pizza baked in %s minutes!")
def bake(pizza: str, time: int) -> None:
    """Bakes the pizza."""
    pass
    #click.echo(f"{pizza} pizza baked in {time} minutes!")


@log("Pizza delivered in %s minutes!")
def deliver(pizza: str, time: int) -> None:
    """Delivers the pizza"""
    pass
    #click.echo(f"{pizza} pizza deliered in {time} minutes!")


@click.group()
def cli():
    pass


@cli.command()
def menu() -> None:
    """Prints the menu."""
    click.echo("All pizzas are available in 'L' or 'XL' sizes")
    click.echo("- Margherita\U0001F9C0: tomato sauce, mozzarella, tomatoes")
    click.echo("- Pepperoni\U0001F355: tomato sauce, mozzarella, pepperoni")
    click.echo("- Hawaiian\U0001F34D: tomato sauce, mozzarella, pineapples, chicken")


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool) -> None:
    if delivery:
        bake(pizza)
        deliver(pizza)
    else:
        bake(pizza)


if __name__ == "__main__":
    cli()