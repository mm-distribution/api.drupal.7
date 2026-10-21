# SelectQueryInterface::range()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 423–423 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L423)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function range($start = NULL, $length = NULL);
```

## Documentation

```text
Restricts a query to a given range in the result set.

If this method is called with no parameters, will remove any range
directives that have been set.

@param $start
  The first record from the result set to return. If NULL, removes any
  range directives that are set.
@param $length
  The number of records to return from the result set.
@return SelectQueryInterface
  The called object.
```

## Code

```php
  public function range($start = NULL, $length = NULL);
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
