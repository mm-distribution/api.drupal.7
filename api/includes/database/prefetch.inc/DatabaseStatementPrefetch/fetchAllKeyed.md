# DatabaseStatementPrefetch::fetchAllKeyed()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 479–493 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L479-L493)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetchAllKeyed($key_index = 0, $value_index = 1)
```

## Documentation

_No docblock in source._

## Code

```php
  public function fetchAllKeyed($key_index = 0, $value_index = 1) {
    if (!isset($this->columnNames[$key_index]) || !isset($this->columnNames[$value_index]))
      return array();

    $key = $this->columnNames[$key_index];
    $value = $this->columnNames[$value_index];

    $result = array();
    // Traverse the array as PHP would have done.
    while (isset($this->currentRow)) {
      $result[$this->currentRow[$key]] = $this->currentRow[$value];
      $this->next();
    }
    return $result;
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
