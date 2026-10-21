# SelectQuery::where()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1070–1073 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1070-L1073)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function where($snippet, $args = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function where($snippet, $args = array()) {
    $this->where->where($snippet, $args);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
