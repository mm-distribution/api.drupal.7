# SelectQueryInterface::getTables()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 131–131 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L131)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function &getTables();
```

## Documentation

```text
Returns a reference to the tables array for this query.

Because this method returns by reference, alter hooks may edit the tables
array directly to make their changes. If just adding tables, however, the
use of the join() methods is preferred.

Note that this method must be called by reference as well:

@code
$fields =& $query->getTables();
@endcode

@return
  A reference to the tables array structure.
```

## Code

```php
  public function &getTables();
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
