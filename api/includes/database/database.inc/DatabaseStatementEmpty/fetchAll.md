# DatabaseStatementEmpty::fetchAll()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2386–2388 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2386-L2388)
- **Class:** [DatabaseStatementEmpty](../DatabaseStatementEmpty.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
function fetchAll($mode = NULL, $column_index = NULL, array $constructor_arguments = array())
```

## Documentation

_No docblock in source._

## Code

```php
  function fetchAll($mode = NULL, $column_index = NULL, array $constructor_arguments = array()) {
    return array();
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
