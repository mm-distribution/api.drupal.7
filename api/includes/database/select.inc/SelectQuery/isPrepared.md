# SelectQuery::isPrepared()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1242–1244 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1242-L1244)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function isPrepared()
```

## Documentation

```text
Indicates if preExecute() has already been called on that object.
```

## Code

```php
  public function isPrepared() {
    return $this->prepared;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
