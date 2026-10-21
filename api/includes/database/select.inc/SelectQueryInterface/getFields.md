# SelectQueryInterface::getFields()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 59–59 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L59)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function &getFields();
```

## Documentation

```text
Returns a reference to the fields array for this query.

Because this method returns by reference, alter hooks may edit the fields
array directly to make their changes. If just adding fields, however, the
use of addField() is preferred.

Note that this method must be called by reference as well:

@code
$fields =& $query->getFields();
@endcode

@return
  A reference to the fields array structure.
```

## Code

```php
  public function &getFields();
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
