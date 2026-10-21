# DatabaseStatementPrefetch::fetch()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 366–385 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L366-L385)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetch($fetch_style = NULL, $cursor_orientation = PDO::FETCH_ORI_NEXT, $cursor_offset = NULL)
```

## Documentation

_No docblock in source._

## Code

```php
  public function fetch($fetch_style = NULL, $cursor_orientation = PDO::FETCH_ORI_NEXT, $cursor_offset = NULL) {
    if (isset($this->currentRow)) {
      // Set the fetch parameter.
      $this->fetchStyle = isset($fetch_style) ? $fetch_style : $this->defaultFetchStyle;
      $this->fetchOptions = $this->defaultFetchOptions;

      // Grab the row in the format specified above.
      $return = $this->current();
      // Advance the cursor.
      $this->next();

      // Reset the fetch parameters to the value stored using setFetchMode().
      $this->fetchStyle = $this->defaultFetchStyle;
      $this->fetchOptions = $this->defaultFetchOptions;
      return $return;
    }
    else {
      return FALSE;
    }
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
