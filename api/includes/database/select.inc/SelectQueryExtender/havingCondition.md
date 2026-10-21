# SelectQueryExtender::havingCondition()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 642–645 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L642-L645)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function havingCondition($field, $value = NULL, $operator = '=')
```

## Documentation

_No docblock in source._

## Code

```php
  public function havingCondition($field, $value = NULL, $operator = '=') {
    $this->query->havingCondition($field, $value, $operator);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
