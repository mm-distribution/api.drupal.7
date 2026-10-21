# SelectQueryExtender::__toString()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 819–821 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L819-L821)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __toString()
```

## Documentation

_No docblock in source._

## Code

```php
  public function __toString() {
    return (string) $this->query;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
