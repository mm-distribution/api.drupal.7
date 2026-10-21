# SelectQueryInterface::getOrderBy()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 95–95 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L95)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function &getOrderBy();
```

## Documentation

```text
Returns a reference to the order by array for this query.

Because this method returns by reference, alter hooks may edit the order-by
array directly to make their changes. If just adding additional ordering
fields, however, the use of orderBy() is preferred.

Note that this method must be called by reference as well:

@code
$fields =& $query->getOrderBy();
@endcode

@return
  A reference to the expression array structure.
```

## Code

```php
  public function &getOrderBy();
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
