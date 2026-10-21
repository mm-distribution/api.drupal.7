# db_merge()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2561–2566 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2561-L2566)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_merge($table, array $options = array())
```

## Documentation

```text
Returns a new MergeQuery object for the active database.

@param $table
  The table into which to merge.
@param $options
  An array of options to control how the query operates.

@return MergeQuery
  A new MergeQuery object for this connection.
```

## Code

```php
function db_merge($table, array $options = array()) {
  if (empty($options['target']) || $options['target'] == 'slave') {
    $options['target'] = 'default';
  }
  return Database::getConnection($options['target'])->merge($table, $options);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
