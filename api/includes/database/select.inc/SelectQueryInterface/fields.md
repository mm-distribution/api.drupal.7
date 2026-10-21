# SelectQueryInterface::fields()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 216–216 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L216)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fields($table_alias, array $fields = array());
```

## Documentation

```text
Add multiple fields from the same table to be SELECTed.

This method does not return the aliases set for the passed fields. In the
majority of cases that is not a problem, as the alias will be the field
name. However, if you do need to know the alias you can call getFields()
and examine the result to determine what alias was created. Alternatively,
simply use addField() for the few fields you care about and this method for
the rest.

@param $table_alias
  The name of the table from which the field comes, as an alias. Generally
  you will want to use the return value of join() here to ensure that it is
  valid.
@param $fields
  An indexed array of fields present in the specified table that should be
  included in this query. If not specified, $table_alias.* will be generated
  without any aliases.
@return SelectQueryInterface
  The called object.
```

## Code

```php
  public function fields($table_alias, array $fields = array());
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
