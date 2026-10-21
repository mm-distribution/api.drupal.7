# DatabaseStatementPrefetch::fetchCol()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 463–477 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L463-L477)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetchCol($index = 0)
```

## Documentation

_No docblock in source._

## Code

```php
  public function fetchCol($index = 0) {
    if (isset($this->columnNames[$index])) {
      $column = $this->columnNames[$index];
      $result = array();
      // Traverse the array as PHP would have done.
      while (isset($this->currentRow)) {
        $result[] = $this->currentRow[$this->columnNames[$index]];
        $this->next();
      }
      return $result;
    }
    else {
      return array();
    }
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
