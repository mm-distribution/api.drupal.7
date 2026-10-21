# SelectQueryExtender::compile()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 632–634 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L632-L634)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function compile(DatabaseConnection $connection, QueryPlaceholderInterface $queryPlaceholder)
```

## Documentation

_No docblock in source._

## Code

```php
  public function compile(DatabaseConnection $connection, QueryPlaceholderInterface $queryPlaceholder) {
    return $this->query->compile($connection, $queryPlaceholder);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
