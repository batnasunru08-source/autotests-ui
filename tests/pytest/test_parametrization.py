import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int) -> None:
    assert number > 0

@pytest.mark.parametrize("numbers, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(numbers:int, expected:int) -> None:
    assert numbers ** 2 == expected

@pytest.mark.parametrize("os", ["macos", "Windows", "Linux", "debian"])
@pytest.mark.parametrize("browser", ["chromium", "webkit", "firefox"])
def test_multiplication_of_numbers(os:str, browser:str) -> None:
    assert len(os + browser) > 0


@pytest.fixture(params=["chromium", "webkit", "firefox"])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser:str) -> None:
    print(f"Running test on browser: {browser}")


@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    @pytest.mark.parametrize("account",["Credit card", "Debit cardt"])
    def test_user_with_operation(self, user: str, account: str):
        print(f"Running test on user: {user} and account: {account}")

    def test_user_without_operation(self, user: str):
        print(f"Running test on user: {user}")


users = {
    "+7000000011": "user with money on bank account",
    "+7000000022": "user without money on bank account",
    "+7000000033": "user with operation on bank account",
}


@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
)
def test_identifiers(phone_number: str):
    ...