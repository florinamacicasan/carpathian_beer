# carpathian_beer
Florina &amp; Catalin - carpathian beers

carpathian-beer is a Python library for using PUNK API

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install carpathian-beer.

```bash
pip install carpathian-beer
```

## Usage
### Code
First you need to import carpathian-beer then you'll need to instantiate a client

```python
import carpathian-beer

carpathian_client = carpathian-beer.Client()
```
The get_beer(id) function returns the beer with the given id (required int argument)
```
carpathian_client.get_beer(1) # returns the beer with id=1 
carpathian_client.get_beer('a') # raises InvalidIdException
```
The get_random_beer() function returns a random beer
```
carpathian_client.get_random_beer() # returns a beer with a random id
```

The get_all_beers(page, per_page, limit) function returns a number of beers depending on the parameters page, per_page, limit
Parameters: <br/>
&nbsp;&nbsp;&nbsp;&nbsp; page      -  specify the page to fetch beers from  <br/>
&nbsp;&nbsp;&nbsp;&nbsp; per_page - specify the number of beers from each page <br/>
&nbsp;&nbsp;&nbsp;&nbsp; limit - specify the number of beers to be displayed <br/>

```
carpathian_client.get_all_beers()  # returns all beers 
carpathian_client.get_all_beers(page = 3, limit = 90)  # returns 90 beers starting from page 3
carpathian_client.get_all_beers(page = 2, per_page = 10)  # returns 10 beers from page 2
carpathian_client.get_all_beers(page = 1, per_page = 10, limit = 5) # returns 5 beers from page 1
```
This function raises ArgumentException if per_page < 0 or page < 0 

### CLI

Usage: carpathian_beer [-h] [--log-to-stdout LOG_TO_STDOUT] [--file-logger FILE_LOGGER] {get_beer,get_random_beer,get_beers} ...

Optional arguments: <br/>
&nbsp;&nbsp;&nbsp;&nbsp;  -h, --help  &nbsp;&nbsp;&nbsp;&nbsp; -  show this help message and exit <br/>
&nbsp;&nbsp;&nbsp;&nbsp;  --log-to-stdout LOG_TO_STDOUT &nbsp;&nbsp;&nbsp;&nbsp; - specify if should log to standard output <br/>
&nbsp;&nbsp;&nbsp;&nbsp;  --file-logger FILE_LOGGER &nbsp;&nbsp;&nbsp;&nbsp; - specify filename to log <br/>

```
$ carpathian-beer -h
$ carpathian-beer --log-to-stdout=True
$ carpathian-beer --file-logger=example.log
$ carpathian-beer --log-to-stdout=True --file-logger=example.log
```

Use command get_beer [-h] id to display the beer with specified id <br/>
Positional argument: <br/>
&nbsp;&nbsp;&nbsp;&nbsp; id is a required int argument
```
$ carpathian-beer get_beer 1  
```

Use command get_random_beer [-h] to display a beer with a random id
```
$ carpathian-beer get_random_beer
```

Use command get_beers [-h] [--page PAGE] [--per_page PER_PAGE] [--limit LIMIT] <br/>
Optional arguments: <br/> 
&nbsp;&nbsp;&nbsp;&nbsp; --page      -  specify the page to fetch beers from  <br/>
&nbsp;&nbsp;&nbsp;&nbsp; --per_page - specify the number of beers from each page <br/>
&nbsp;&nbsp;&nbsp;&nbsp; --limit - specify the number of beers to be displayed <br/>

```
$ carpathian-beer get_beers
$ carpathian-beer get_beers --page=1 --limit=5
$ carpathian-beer get_beers --page=2 --per_page=10
$ carpathian-beer get_beers --limit=7
$ carpathian-beer get_beers --page=5 --per_page=3 --limit=20
```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

