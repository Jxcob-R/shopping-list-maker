import sys
from typing import List

from shopping import choose_ingredients

class Args:
    PROGRAM_ARGS = 3

    def __init__(self, argv: List[str]) -> None:
        self.program_name = argv[0]
        if len(argv[1:]) < Args.PROGRAM_ARGS:
            self.usage()
            exit(1)

        # TODO: Parse this a bit more carefully
        self.days: int = int(argv[1])
        self.recipe_csv_path: str = argv[2];
        self.ingredients_csv_path: str = argv[3];

    def usage(self) -> None:
        print(
f"""
Shopping list maker:
usage:
{self.program_name} <days> <recipe_csv> <ingredients_csv>
"""
        )


if __name__ == '__main__':
    args = Args(sys.argv)

    chosen_recipes = choose_ingredients(args.days, args.recipe_csv_path,
                                        args.ingredients_csv_path)
    if len(chosen_recipes) < args.days:
        print("Not enough recipes in database to fulfill all days requested")
