# [pytest]   # This section header tells pytest "the settings below are for pytest"

# asyncio_default_fixture_loop_scope = function


# # This is from pytest-asyncio.
# # It controls the scope of the event loop fixture for async tests.
# # Options: "function" (new loop per test), "class", "module", "session".
# # In your case → each test function gets a fresh event loop.

# markers =
#     smoke : these are smoke tests


# # This registers a custom marker called "smoke".
# # - Without registering, pytest would give warnings if you used @pytest.mark.smoke.
# # - By registering, you can tag tests like this:
# #       @pytest.mark.smoke
# #       def test_login(): ...
# #   Then run only smoke tests with: pytest -m smoke


# # pip install pytest-asyncio
# # then can use the file