# SelectQueryExtender::having()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 655–658 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L655-L658)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function having($snippet, $args = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function having($snippet, $args = array()) {
    $this->query->having($snippet, $args);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
