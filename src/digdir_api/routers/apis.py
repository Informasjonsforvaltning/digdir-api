from fastapi import APIRouter
from starlette import status
from starlette.responses import Response
from digdir_api.collections.apis import catalog
from digdir_api.models.response_model import ResponseModel

router = APIRouter()


@router.get("/apis", response_class=ResponseModel)
def get_all_apis():
    apis = catalog.create_catalog()
    return Response(status_code=status.HTTP_200_OK, content=apis, media_type="text/turtle")
