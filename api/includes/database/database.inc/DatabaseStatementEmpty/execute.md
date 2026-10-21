# DatabaseStatementEmpty::execute()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2354–2356 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2354-L2356)
- **Class:** [DatabaseStatementEmpty](../DatabaseStatementEmpty.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function execute($args = array(), $options = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function execute($args = array(), $options = array()) {
    return FALSE;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
