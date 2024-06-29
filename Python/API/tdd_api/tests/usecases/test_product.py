import pytest
from uuid import UUID

from store.usecases.product import product_usecase
from tests.factories import product_data, products_data
from tests.conftest import (
    product_id,
    product_in,
    product_up,
    product_inserted,
    products_inserted,
)
from store.schemas.product import ProductOut, ProductUpdateOut
from store.core.exceptions import NotFoundException


async def test_usecases_create_should_return_success(product_in):
    results = await product_usecase.create(body=product_in)

    assert isinstance(results, ProductOut)
    assert results.name == "iPhone 14 Pro max"


async def test_usecases_get_should_return_success(product_inserted):
    result = await product_usecase.get(id=product_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "iPhone 14 Pro max"


async def test_usecases_get_should_not_found():
    with pytest.raises(NotFoundException) as error:
        await product_usecase.get(id=UUID("1e4f214e-58f7-461a-a781a32e3bb9"))

    assert (
        error.value.message
        == "Product not found with filter: 1e4f214e-58f7-461a-a781a32e3bb9"
    )


@pytest.mark.usefixtures("products_inserted")
async def test_usecases_querry_should_return_success():
    result = await product_usecase.query()

    assert isinstance(result, List)
    assert len(result) > 1


async def test_usecases_update_should_return_success(product_up, product_inserted):
    product_up.price = "7.500"
    result = await product_usecase.update(id=product_inserted.id, body=product_up)

    assert isinstance(result, ProductUpdateOut)


async def test_usecases_delete_should_return_success(product_inserted):
    result = await product_usecase.delete(id=product_inserted.id)

    assert result is True


async def test_usecases_delete_should_not_found():
    with pytest.raises(NotFoundException) as error:
        await product_usecase.delete(id=UUID("1e4f214e-58f7-461a-a781a32e3bb9"))

    assert (
        error.value.message
        == "Product not found with filter: 1e4f214e-58f7-461a-a781a32e3bb9"
    )
