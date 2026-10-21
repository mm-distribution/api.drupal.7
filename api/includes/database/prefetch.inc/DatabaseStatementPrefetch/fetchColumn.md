# DatabaseStatementPrefetch::fetchColumn()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 387–397 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L387-L397)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetchColumn($index = 0)
```

## Documentation

_No docblock in source._

## Code

```php
  public function fetchColumn($index = 0) {
    if (isset($this->currentRow) && isset($this->columnNames[$index])) {
      // We grab the value directly from $this->data, and format it.
      $return = $this->currentRow[$this->columnNames[$index]];
      $this->next();
      return $return;
    }
    else {
      return FALSE;
    }
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
