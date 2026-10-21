# SelectQueryExtender::arguments()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 623–625 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L623-L625)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function arguments()
```

## Documentation

_No docblock in source._

## Code

```php
  public function arguments() {
    return $this->query->arguments();
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
