from os import error
import sys
from typing import List

from ds import Recipe
from shopping import make_shopping_list
from add import RecipeAddException, add_recipe

def help():
    """
    Comprehensive help for API
    """
    print("WIP")

class Args:
    def __init__(self, argv: List[str]) -> None:
        self.program_name = argv[0]
        self.cmds = {
            "shop": make_shopping_list,
            "add": add_recipe,
            "help": help
        }

        if len(argv[1:]) == 0 or argv[1] not in self.cmds.keys():
            self.usage()
            exit(1)

        self.given_cmd = argv[1]
        self.remaining_args = argv[2:]


    def usage(self) -> None:
        print(
f"""
Shopping list maker:
usage:
{self.program_name} [shop|add|help] <args>
"""
        )

    def run_given_cmd(self) -> List[Recipe] | Exception | RecipeAddException | None:
        """
        Run the command provided in the args, handle issues with argument
        quantities, but not types
        """
        cmd = self.cmds[self.given_cmd]
        args = self.remaining_args
        match self.given_cmd:
            case "add":
                if len(args) < 2:
                    raise Exception("Not enough arguments")
                (recipes_path, ingr_path) = self.remaining_args
                return cmd(recipes_path, ingr_path)
            case "shop":
                if len(args) < 3:
                    raise Exception("Not enough arguments")
                (days, recipes_path, ingr_path) = self.remaining_args
                return cmd(days, recipes_path, ingr_path)
            case "help":
                return cmd()
            case _:
                raise Exception("This is an unexpected error")


if __name__ == '__main__':
    args = Args(sys.argv)
    try:
        args.run_given_cmd()
    except Exception as e:
        print("Catching general exceptions for now")
        print(e)
