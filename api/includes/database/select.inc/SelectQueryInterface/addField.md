# SelectQueryInterface::addField()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 193–193 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L193)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function addField($table_alias, $field, $alias = NULL);
```

## Documentation

```text
Adds a field to the list to be SELECTed.

@param $table_alias
  The name of the table from which the field comes, as an alias. Generally
  you will want to use the return value of join() here to ensure that it is
  valid.
@param $field
  The name of the field.
@param $alias
  The alias for this field. If not specified, one will be generated
  automatically based on the $table_alias and $field. The alias will be
  checked for uniqueness, so the requested alias may not be the alias
  that is assigned in all cases.
@return
  The unique alias that was assigned for this field.
```

## Code

```php
  public function addField($table_alias, $field, $alias = NULL);
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
