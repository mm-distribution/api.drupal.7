# SelectQuery::getArguments()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1231–1237 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1231-L1237)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function getArguments(QueryPlaceholderInterface $queryPlaceholder = NULL)
```

## Documentation

_No docblock in source._

## Code

```php
  public function getArguments(QueryPlaceholderInterface $queryPlaceholder = NULL) {
    if (!isset($queryPlaceholder)) {
      $queryPlaceholder = $this;
    }
    $this->compile($this->connection, $queryPlaceholder);
    return $this->arguments();
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
