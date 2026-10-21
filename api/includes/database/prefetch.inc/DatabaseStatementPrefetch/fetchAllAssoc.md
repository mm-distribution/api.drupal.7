# DatabaseStatementPrefetch::fetchAllAssoc()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 495–514 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L495-L514)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetchAllAssoc($key, $fetch_style = NULL)
```

## Documentation

_No docblock in source._

## Code

```php
  public function fetchAllAssoc($key, $fetch_style = NULL) {
    $this->fetchStyle = isset($fetch_style) ? $fetch_style : $this->defaultFetchStyle;
    $this->fetchOptions = $this->defaultFetchOptions;

    $result = array();
    // Traverse the array as PHP would have done.
    while (isset($this->currentRow)) {
      // Grab the row in its raw PDO::FETCH_ASSOC format.
      $row = $this->currentRow;
      // Grab the row in the format specified above.
      $result_row = $this->current();
      $result[$this->currentRow[$key]] = $result_row;
      $this->next();
    }

    // Reset the fetch parameters to the value stored using setFetchMode().
    $this->fetchStyle = $this->defaultFetchStyle;
    $this->fetchOptions = $this->defaultFetchOptions;
    return $result;
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
