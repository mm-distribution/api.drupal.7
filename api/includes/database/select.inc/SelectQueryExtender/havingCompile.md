# SelectQueryExtender::havingCompile()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 660–662 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L660-L662)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function havingCompile(DatabaseConnection $connection)
```

## Documentation

_No docblock in source._

## Code

```php
  public function havingCompile(DatabaseConnection $connection) {
    return $this->query->havingCompile($connection);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
