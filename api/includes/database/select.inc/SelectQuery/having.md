# SelectQuery::having()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1159–1162 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1159-L1162)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function having($snippet, $args = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function having($snippet, $args = array()) {
    $this->having->where($snippet, $args);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
