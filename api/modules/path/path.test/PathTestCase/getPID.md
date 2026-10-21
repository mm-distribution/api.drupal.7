# PathTestCase::getPID()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 251–253 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L251-L253)
- **Class:** [PathTestCase](../PathTestCase.md)
- **Module/theme:** path

## Signature

```php
function getPID($alias)
```

## Documentation

```text
Returns the path ID.

@param $alias
  A string containing an aliased path.

@return int
  Integer representing the path ID.
```

## Code

```php
  function getPID($alias) {
    return db_query("SELECT pid FROM {url_alias} WHERE alias = :alias", array(':alias' => $alias))->fetchField();
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
