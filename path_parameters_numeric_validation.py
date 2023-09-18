from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)],
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# With Query, Path (and others you haven't seen yet) you can declare metadata and string
# validations in the same ways as with Query Parameters and String Validations.

# And you can also declare numeric validations:

# gt: greater than
# ge: greater than or equal
# lt: less than
# le: less than or equal
