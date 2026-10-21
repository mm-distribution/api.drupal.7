# SelectQueryInterface::distinct()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 174–174 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L174)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function distinct($distinct = TRUE);
```

## Documentation

```text
Sets this query to be DISTINCT.

@param $distinct
  TRUE to flag this query DISTINCT, FALSE to disable it.
@return SelectQueryInterface
  The called object.
```

## Code

```php
  public function distinct($distinct = TRUE);
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
