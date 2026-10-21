# SelectQuery::hasAllTags()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1004–1007 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1004-L1007)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function hasAllTags()
```

## Documentation

_No docblock in source._

## Code

```php
  public function hasAllTags() {
    $args = func_get_args();
    return !(boolean)array_diff($args, array_keys($this->alterTags));
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
