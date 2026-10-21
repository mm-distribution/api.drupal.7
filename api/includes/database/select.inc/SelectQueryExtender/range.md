# SelectQueryExtender::range()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 775–778 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L775-L778)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
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
    $this->query->range($start, $length);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
