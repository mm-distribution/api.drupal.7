# QueryExtendableInterface::extend()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 33–33 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L33)
- **Class:** [QueryExtendableInterface](../QueryExtendableInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function extend($extender_name);
```

## Documentation

```text
Enhance this object by wrapping it in an extender object.

@param $extender_name
  The base name of the extending class.  The base name will be checked
  against the current database connection to allow driver-specific subclasses
  as well, using the same logic as the query objects themselves.  For example,
  PagerDefault_mysql is the MySQL-specific override for PagerDefault.
@return QueryExtendableInterface
  The extender object, which now contains a reference to this object.
```

## Code

```php
  public function extend($extender_name);
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
