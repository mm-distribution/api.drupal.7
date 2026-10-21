# variable_get()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1288–1292 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1288-L1292)

## Signature

```php
function variable_get($name, $default = NULL)
```

## Documentation

```text
Returns a persistent variable.

Case-sensitivity of the variable_* functions depends on the database
collation used. To avoid problems, always use lower case for persistent
variable names.

@param $name
  The name of the variable to return.
@param $default
  The default value to use if this variable has never been set.

@return
  The value of the variable. Unserialization is taken care of as necessary.

@see variable_del()
@see variable_set()
```

## Code

```php
function variable_get($name, $default = NULL) {
  global $conf;

  return isset($conf[$name]) ? $conf[$name] : $default;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
