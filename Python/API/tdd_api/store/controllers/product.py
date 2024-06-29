import asyncio
from fastapi import APIRouter, status, Body, Depends, Path, HTTPException
from pydantic import UUID4
from store.core.exceptions import NotFoundException
from typing import List

from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from store.usecases.product import ProductUsecase

router = APIRouter(tags=["products"])


@router.post(path="/", status_code=status.HTTP_201_CREATED)
async def post(
    body: ProductIn = Body(...), usecase: ProductUsecase = Depends()
) -> ProductOut:
    return await usecases.create(body=body)


@router.get(path="/{id}", status_code=status.HTTP_200_OK)
async def get(
    id: UUID4 = Path(alias="id"), usecase: ProductUsecase = Depends()
) -> ProductOut:
    try:
        return await usecases.get(id=id)
    except NotFoundException as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)


@router.get(path="/", status_code=status.HTTP_200_OK)
async def query(usecase: ProductUsecase = Depends()) -> List[ProductOut]:
    return await usecases.query()


@router.patch(path="/{id}", status_code=status.HTTP_200_OK)
async def patch(
    id: UUID4 = Path(alias="id"),
    body: ProductUpdate = Body(...),
    usecase: ProductUsecase = Depends(),
) -> ProductUpdateOut:
    return await usecase.update(id=id, body=body)


@router.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    id: UUID4 = Path(alias="id"), usecase: ProductUsecase = Depends()
) -> None:
    try:
        await usecases.delete(id=id)
    except NotFoundException as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)
