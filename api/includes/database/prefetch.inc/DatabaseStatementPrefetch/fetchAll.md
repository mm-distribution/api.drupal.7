# DatabaseStatementPrefetch::fetchAll()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 439–461 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L439-L461)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetchAll($fetch_style = NULL, $fetch_column = NULL, $constructor_args = NULL)
```

## Documentation

_No docblock in source._

## Code

```php
  public function fetchAll($fetch_style = NULL, $fetch_column = NULL, $constructor_args = NULL) {
    $this->fetchStyle = isset($fetch_style) ? $fetch_style : $this->defaultFetchStyle;
    $this->fetchOptions = $this->defaultFetchOptions;
    if (isset($fetch_column)) {
      $this->fetchOptions['column'] = $fetch_column;
    }
    if (isset($constructor_args)) {
      $this->fetchOptions['constructor_args'] = $constructor_args;
    }

    $result = array();
    // Traverse the array as PHP would have done.
    while (isset($this->currentRow)) {
      // Grab the row in the format specified above.
      $result[] = $this->current();
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
