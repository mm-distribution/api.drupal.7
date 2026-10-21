# variable_del()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1333–1342 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1333-L1342)

## Signature

```php
function variable_del($name)
```

## Documentation

```text
Unsets a persistent variable.

Case-sensitivity of the variable_* functions depends on the database
collation used. To avoid problems, always use lower case for persistent
variable names.

@param $name
  The name of the variable to undefine.

@see variable_get()
@see variable_set()
```

## Code

```php
function variable_del($name) {
  global $conf;

  db_delete('variable')
    ->condition('name', $name)
    ->execute();
  cache_clear_all('variables', 'cache_bootstrap');

  unset($conf[$name]);
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
