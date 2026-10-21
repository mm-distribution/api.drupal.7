# DatabaseStatementPrefetch::setFetchMode()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 239–259 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L239-L259)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function setFetchMode($fetchStyle, $a2 = NULL, $a3 = NULL)
```

## Documentation

```text
@see PDOStatement::setFetchMode()
```

## Code

```php
  public function setFetchMode($fetchStyle, $a2 = NULL, $a3 = NULL) {
    $this->defaultFetchStyle = $fetchStyle;
    switch ($fetchStyle) {
      case PDO::FETCH_CLASS:
        $this->defaultFetchOptions['class'] = $a2;
        if ($a3) {
          $this->defaultFetchOptions['constructor_args'] = $a3;
        }
        break;
      case PDO::FETCH_COLUMN:
        $this->defaultFetchOptions['column'] = $a2;
        break;
      case PDO::FETCH_INTO:
        $this->defaultFetchOptions['object'] = $a2;
        break;
    }

    // Set the values for the next fetch.
    $this->fetchStyle = $this->defaultFetchStyle;
    $this->fetchOptions = $this->defaultFetchOptions;
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
