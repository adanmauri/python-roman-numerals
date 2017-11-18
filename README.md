# What is Python Roman Numerals
Python Roman Numerals is a library in order to convert arabic and roman numerals.

## deromanize()
### Definition and Usage
The deromanize function converts a roman numeral string to its corresponding arabic numeral integer.

### Syntax
```python
deromanize(string)
```

### Parameters values
* **string**: Required. The roman numeral string

### Example

Returns a integer which is the corresponding arabic number of "MMXVII":

```python
num = deromanize("MMXVII")
```
The result of *num* will be:
```python
2017
```

## romanize()
### Definition and Usage
The romanize function converts a arabic numeral integer to its corresponding roman numeral string.

### Syntax
```python
romanize(integer)
```

### Parameters values
* **integer**: Required. The arabic numeral integer

#### Example

Returns a string which is the corresponding arabic number of 2017:
```python
num = romanize(2017)
```
The result of *num* will be:
```python
MMXVII
```
