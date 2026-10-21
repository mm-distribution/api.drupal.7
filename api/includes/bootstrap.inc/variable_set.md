# variable_set()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1310–1318 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1310-L1318)

## Signature

```php
function variable_set($name, $value)
```

## Documentation

```text
Sets a persistent variable.

Case-sensitivity of the variable_* functions depends on the database
collation used. To avoid problems, always use lower case for persistent
variable names.

@param $name
  The name of the variable to set.
@param $value
  The value to set. This can be any PHP data type; these functions take care
  of serialization as necessary.

@see variable_del()
@see variable_get()
```

## Code

```php
function variable_set($name, $value) {
  global $conf;

  db_merge('variable')->key(array('name' => $name))->fields(array('value' => serialize($value)))->execute();

  cache_clear_all('variables', 'cache_bootstrap');

  $conf[$name] = $value;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
