# SelectQueryExtender::hasAnyTag()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 598–601 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L598-L601)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function hasAnyTag()
```

## Documentation

_No docblock in source._

## Code

```php
  public function hasAnyTag() {
    $args = func_get_args();
    return call_user_func_array(array($this->query, 'hasAnyTag'), $args);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
