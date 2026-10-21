# SelectQuery::range()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1446–1449 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1446-L1449)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function range($start = NULL, $length = NULL)
```

## Documentation

_No docblock in source._

## Code

```php
  public function range($start = NULL, $length = NULL) {
    $this->range = func_num_args() ? array('start' => $start, 'length' => $length) : array();
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
