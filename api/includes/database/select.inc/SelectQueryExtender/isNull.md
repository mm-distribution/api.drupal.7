# SelectQueryExtender::isNull()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 799–802 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L799-L802)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
function isNull($field)
```

## Documentation

_No docblock in source._

## Code

```php
  function isNull($field) {
    $this->query->isNull($field);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
