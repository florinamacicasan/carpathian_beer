# carpathian_beer
Florina &amp; Catalin - carpathian beers

carpathian_beer is a Python library for using PUNK API

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install carpathian_beer.

```bash
pip install carpathian_beer
```

## Usage
### Code
First you need to import carpathian_beer then you'll need to instantiate a client

```python
import carpathian-beer

carpathian_client = carpathian-beer.Client()
```
The get_beer(id) function returns the beer with the given id
```
carpathian_client.get_beer(1) # returns the beer with id=1 
```
The get_random_beer() function return a random beer
```
carpathian_client.get_random_beer() # returns a beer with a random id
```

### Terminal

```
$ carpathian-client -h
$ carpathian_client get_beer 1  
$ carpathian_client get_random_beer
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

