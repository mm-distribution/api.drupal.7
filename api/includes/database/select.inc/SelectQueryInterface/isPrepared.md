# SelectQueryInterface::isPrepared()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 474–474 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L474)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function isPrepared();
```

## Documentation

```text
Indicates if preExecute() has already been called on that object.

@return
  TRUE is this query has already been prepared, FALSE otherwise.
```

## Code

```php
  public function isPrepared();
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
