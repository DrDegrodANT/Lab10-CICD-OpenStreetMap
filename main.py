import requests


def test_openstreetmap_main_page_available():
    response = requests.get("https://www.openstreetmap.org", timeout=10)

    assert response.status_code == 200
    assert "OpenStreetMap" in response.text


def test_openstreetmap_search_kyiv_api():
    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": "Kyiv",
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "Lab10-CICD-OpenStreetMap-Test"
    }

    response = requests.get(url, params=params, headers=headers, timeout=10)

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0
    assert "Kyiv" in data[0]["display_name"] or "Київ" in data[0]["display_name"]
