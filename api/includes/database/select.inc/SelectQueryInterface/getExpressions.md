# SelectQueryInterface::getExpressions()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 77–77 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L77)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function &getExpressions();
```

## Documentation

```text
Returns a reference to the expressions array for this query.

Because this method returns by reference, alter hooks may edit the expressions
array directly to make their changes. If just adding expressions, however, the
use of addExpression() is preferred.

Note that this method must be called by reference as well:

@code
$fields =& $query->getExpressions();
@endcode

@return
  A reference to the expression array structure.
```

## Code

```php
  public function &getExpressions();
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
