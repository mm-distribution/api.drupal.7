# DatabaseStatementPrefetch::fetchObject()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 403–426 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L403-L426)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetchObject($class_name = NULL, $constructor_args = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function fetchObject($class_name = NULL, $constructor_args = array()) {
    if (isset($this->currentRow)) {
      if (!isset($class_name)) {
        // Directly cast to an object to avoid a function call.
        $result = (object) $this->currentRow;
      }
      else {
        $this->fetchStyle = PDO::FETCH_CLASS;
        $this->fetchOptions = array('constructor_args' => $constructor_args);
        // Grab the row in the format specified above.
        $result = $this->current();
        // Reset the fetch parameters to the value stored using setFetchMode().
        $this->fetchStyle = $this->defaultFetchStyle;
        $this->fetchOptions = $this->defaultFetchOptions;
      }

      $this->next();

      return $result;
    }
    else {
      return FALSE;
    }
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
