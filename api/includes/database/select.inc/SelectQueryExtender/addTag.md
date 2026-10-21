# SelectQueryExtender::addTag()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 584–587 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L584-L587)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function addTag($tag)
```

## Documentation

_No docblock in source._

## Code

```php
  public function addTag($tag) {
    $this->query->addTag($tag);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
