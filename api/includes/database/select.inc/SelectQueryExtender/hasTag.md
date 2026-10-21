# SelectQueryExtender::hasTag()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 589–591 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L589-L591)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
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
    return $this->query->hasTag($tag);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
