# SelectQueryInterface::getUnion()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 150–150 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L150)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function &getUnion();
```

## Documentation

```text
Returns a reference to the union queries for this query. This include
queries for UNION, UNION ALL, and UNION DISTINCT.

Because this method returns by reference, alter hooks may edit the tables
array directly to make their changes. If just adding union queries,
however, the use of the union() method is preferred.

Note that this method must be called by reference as well:

@code
$fields =& $query->getUnion();
@endcode

@return
  A reference to the union query array structure.
```

## Code

```php
  public function &getUnion();
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
