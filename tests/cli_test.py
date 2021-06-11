import subprocess
from carpathian_beer import Client

client = Client()


def test_cli_random_beer():
    output = subprocess.run(["carpathian-beer", "get_random_beer"], capture_output=True)
    assert output.returncode == 0
    beer_data = eval(output.stdout)
    assert "id" in beer_data


def test_cli_get_beer():
    output = subprocess.run(["carpathian-beer", "get_beer", "1"], capture_output=True)
    assert output.returncode == 0
    beer_data = eval(output.stdout)
    assert beer_data["id"] == client.get_beer(1).id


def test_cli_get_beer_invalid_id():
    output = subprocess.run(["carpathian-beer", "get_beer", "a"], capture_output=True)
    assert output.returncode != 0


def test_cli_get_beers():
    output = subprocess.run(["carpathian-beer", "get_beers"], capture_output=True)
    assert output.returncode == 0
    output_data = eval(output.stdout)
    assert len(output_data) == len(client.get_all_beers())


def test_cli_get_beers_page():
    output = subprocess.run(
        ["carpathian-beer", "get_beers", "--page=0"], capture_output=True
    )
    assert output.returncode == 1


def test_cli_get_beers_page_limit():
    output = subprocess.run(
        ["carpathian-beer", "get_beers", "--page=2", "--limit=10"], capture_output=True
    )
    assert output.returncode == 0
    output_data = eval(output.stdout)
    assert len(output_data) == len(client.get_all_beers(page=2, limit=10))


def test_cli_get_beers_page_per_page():
    output = subprocess.run(
        ["carpathian-beer", "get_beers", "--page=1", "--per_page=10"],
        capture_output=True,
    )
    assert output.returncode == 0
    output_data = eval(output.stdout)
    assert len(output_data) == len(client.get_all_beers(page=1, per_page=10))


def test_cli_get_beers_limit():
    output = subprocess.run(
        ["carpathian-beer", "get_beers", "--limit=0"], capture_output=True
    )
    assert output.returncode == 0
    output_data = eval(output.stdout.decode())
    assert len(output_data) == len(client.get_all_beers(limit=0))


def test_cli_get_beers_per_page():
    output = subprocess.run(
        ["carpathian-beer", "get_beers", "--per_page=0"],
        capture_output=True,
    )
    assert output.returncode == 1
