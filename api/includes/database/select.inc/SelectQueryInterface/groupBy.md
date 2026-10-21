# SelectQueryInterface::groupBy()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 458–458 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L458)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function groupBy($field);
```

## Documentation

```text
Groups the result set by the specified field.

@param $field
  The field on which to group. This should be the field as aliased.
@return SelectQueryInterface
  The called object.
```

## Code

```php
  public function groupBy($field);
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
