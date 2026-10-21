# SelectQueryInterface::countQuery()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 466–466 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L466)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function countQuery();
```

## Documentation

```text
Get the equivalent COUNT query of this query as a new query object.

@return SelectQueryInterface
  A new SelectQuery object with no fields or expressions besides COUNT(*).
```

## Code

```php
  public function countQuery();
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
