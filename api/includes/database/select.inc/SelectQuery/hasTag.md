# SelectQuery::hasTag()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1000–1002 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1000-L1002)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function hasTag($tag)
```

## Documentation

_No docblock in source._

## Code

```php
  public function hasTag($tag) {
    return isset($this->alterTags[$tag]);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
