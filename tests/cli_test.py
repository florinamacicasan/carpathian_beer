from carpathian_beer.cli import carpathian_beer
import subprocess
import re
from carpathian_beer import Client

client=Client()

def test_cli_random_beer():
    output = subprocess.run(['carpathian-beer', 'get_random_beer'], capture_output=True)
    assert output.returncode==0
    assert len(re.findall("'id':",output.stdout.decode()))==1

def test_cli_get_beer():
    output = subprocess.run(['carpathian-beer', 'get_beer', '1'], capture_output=True)
    assert output.returncode==0
    assert len(re.findall("'id':",output.stdout.decode()))==1

def test_cli_get_beers():
    output = subprocess.run(['carpathian-beer', 'get_beers'], capture_output=True)
    assert output.returncode==0
    assert len(re.findall("'id':",output.stdout.decode()))==len(client.get_all_beers())

def test_cli_get_beers_page():
    output = subprocess.run(['carpathian-beer', 'get_beers', '--page=2'], capture_output=True)
    assert output.returncode==0
    assert len(re.findall("'id':",output.stdout.decode()))==len(client.get_all_beers(page=2))

def test_cli_get_beers_page_per_page():
    output = subprocess.run(['carpathian-beer', 'get_beers', '--page=1','--per_page=10'], capture_output=True)
    assert output.returncode==0
    assert len(re.findall("'id':",output.stdout.decode()))==len(client.get_all_beers(page=1,per_page=10))

def test_cli_get_beers_limit():
    output = subprocess.run(['carpathian-beer', 'get_beers', '--limit=10'], capture_output=True)
    assert output.returncode==0
    assert len(re.findall("'id':",output.stdout.decode()))==len(client.get_all_beers(limit=10))
    