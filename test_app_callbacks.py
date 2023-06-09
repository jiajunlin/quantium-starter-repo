import pytest
from dash import Dash, html
from dash.testing.application_runners import import_app


# Test these:
# The header is present.
# The visualization is present.
# The region picker is present.


@pytest.fixture(scope="module")
def app():
    app = import_app("app")
    return app


def test_header_is_present(dash_duo, dash_app):
    dash_app.layout = app.layout
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=5)
    assert dash_duo.find_element("h1").text == "Soul Foods Sales Trend"


def test_visualization_present(dash_app, dash_duo):
    dash_app.layout = app.layout
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#example-graph-2")


def test_region_picker_present(dash_app, dash_duo):
    dash_app.layout = app.layout
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#region-filter")


if __name__ == "__main__":
    pytest.main([__file__])
