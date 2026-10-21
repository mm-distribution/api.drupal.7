# SelectQueryExtender::preExecute()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 707–714 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L707-L714)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function preExecute(SelectQueryInterface $query = NULL)
```

## Documentation

_No docblock in source._

## Code

```php
  public function preExecute(SelectQueryInterface $query = NULL) {
    // If no query object is passed in, use $this.
    if (!isset($query)) {
      $query = $this;
    }

    return $this->query->preExecute($query);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
