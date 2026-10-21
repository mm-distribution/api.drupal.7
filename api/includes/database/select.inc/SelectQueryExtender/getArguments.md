# SelectQueryExtender::getArguments()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 699–701 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L699-L701)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
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
    return $this->query->getArguments($queryPlaceholder);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
