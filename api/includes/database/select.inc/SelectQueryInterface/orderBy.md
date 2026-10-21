# SelectQueryInterface::orderBy()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 385–385 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L385)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function orderBy($field, $direction = 'ASC');
```

## Documentation

```text
Orders the result set by a given field.

If called multiple times, the query will order by each specified field in the
order this method is called.

If the query uses DISTINCT or GROUP BY conditions, fields or expressions
that are used for the order must be selected to be compatible with some
databases like PostgreSQL. The PostgreSQL driver can handle simple cases
automatically but it is suggested to explicitly specify them. Additionally,
when ordering on an alias, the alias must be added before orderBy() is
called.

@param $field
  The field on which to order.
@param $direction
  The direction to sort. Legal values are "ASC" and "DESC". Any other value
  will be converted to "ASC".
@return SelectQueryInterface
  The called object.
```

## Code

```php
  public function orderBy($field, $direction = 'ASC');
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
