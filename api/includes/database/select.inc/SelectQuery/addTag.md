# SelectQuery::addTag()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 995–998 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L995-L998)
- **Class:** [SelectQuery](../SelectQuery.md)
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
    $this->alterTags[$tag] = 1;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
