# SelectQueryExtender::addExpression()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 741–743 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L741-L743)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function addExpression($expression, $alias = NULL, $arguments = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function addExpression($expression, $alias = NULL, $arguments = array()) {
    return $this->query->addExpression($expression, $alias, $arguments);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
