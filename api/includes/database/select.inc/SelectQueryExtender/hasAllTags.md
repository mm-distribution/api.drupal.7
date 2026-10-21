# SelectQueryExtender::hasAllTags()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 593–596 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L593-L596)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
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
    return call_user_func_array(array($this->query, 'hasAllTags'), $args);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
