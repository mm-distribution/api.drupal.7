# DatabaseStatementInterface::fetchAllKeyed()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2216–2216 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2216)
- **Class:** [DatabaseStatementInterface](../DatabaseStatementInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetchAllKeyed($key_index = 0, $value_index = 1);
```

## Documentation

```text
Returns the entire result set as a single associative array.

This method is only useful for two-column result sets. It will return an
associative array where the key is one column from the result set and the
value is another field. In most cases, the default of the first two columns
is appropriate.

Note that this method will run the result set to the end.

@param $key_index
  The numeric index of the field to use as the array key.
@param $value_index
  The numeric index of the field to use as the array value.

@return
  An associative array, or an empty array if there is no result set.
```

## Code

```php
  public function fetchAllKeyed($key_index = 0, $value_index = 1);
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
