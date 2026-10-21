# DatabaseStatementInterface::fetchAllAssoc()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2235–2235 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2235)
- **Class:** [DatabaseStatementInterface](../DatabaseStatementInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function fetchAllAssoc($key, $fetch = NULL);
```

## Documentation

```text
Returns the result set as an associative array keyed by the given field.

If the given key appears multiple times, later records will overwrite
earlier ones.

@param $key
  The name of the field on which to index the array.
@param $fetch
  The fetchmode to use. If set to PDO::FETCH_ASSOC, PDO::FETCH_NUM, or
  PDO::FETCH_BOTH the returned value with be an array of arrays. For any
  other value it will be an array of objects. By default, the fetch mode
  set for the query will be used.

@return
  An associative array, or an empty array if there is no result set.
```

## Code

```php
  public function fetchAllAssoc($key, $fetch = NULL);
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
