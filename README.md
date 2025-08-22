# Shopping List Generator Maker

This outlines some simple usage of the program.

> [!NOTE]
> Project is currently is very minimal prototype, many features listed below are
> not yet implemented.
> Expect items listed here to be *priorities* for development.

## Initial CLI Usage

*This is for current prototyping as a CLI tool*

The two main commands:
- `add`: Add a recipe
- `list`: Make a shopping list for the next `n` days, as specified

## Datakeeping (simple)

Recipes will be read in JSON format, in the form:
```json
{
    "name": "<Recipe name>",
    "ingredients_list": [ <Ingredient object>, ... ]
}
```

Where ingredients are specified as:
```json
{
    "name": "<Ingredient name>",
    "unit": "<Unit type>",
    "qty": <qty>,
}
```

<!-- TODO: We may also have a separate 'database' of objects for ingredients
     themselves which may provide cost data and size of a single server etc.

    If a relational model approach is preferred, we may need to re-design this
    backend, otherwise this simplistic model is fine.
-->

## Project structure

- `main.py`: Current starting point for CLI use; this will hand control to the
  appropriate module given the command used, call directly to start program.

- `shopping.py`: Called with `list` command, reads data from recipe base and
  appropriate sources, considering other factors to optimise a list/plan.

- `add.py`: Called with `add` command, used to write to the shopping data stored
  locally.
