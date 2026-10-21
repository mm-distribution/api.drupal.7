# SelectQueryInterface::getGroupBy()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 113–113 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L113)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function &getGroupBy();
```

## Documentation

```text
Returns a reference to the group-by array for this query.

Because this method returns by reference, alter hooks may edit the group-by
array directly to make their changes. If just adding additional grouping
fields, however, the use of groupBy() is preferred.

Note that this method must be called by reference as well:

@code
$fields =& $query->getGroupBy();
@endcode

@return
  A reference to the group-by array structure.
```

## Code

```php
  public function &getGroupBy();
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
