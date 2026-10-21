# path_load()

- **Type:** Function
- **File:** [`includes/path.inc`](_file.md), lines 404–424 · [local source](../../../source/includes/path.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/path.inc#L404-L424)

## Signature

```php
function path_load($conditions)
```

## Documentation

```text
Fetches a specific URL alias from the database.

@param $conditions
  A string representing the source, a number representing the pid, or an
  array of query conditions.

@return
  FALSE if no alias was found or an associative array containing the
  following keys:
  - source: The internal system path.
  - alias: The URL alias.
  - pid: Unique path alias identifier.
  - language: The language of the alias.
```

## Code

```php
function path_load($conditions) {
  if (is_numeric($conditions)) {
    $conditions = array('pid' => $conditions);
  }
  elseif (is_string($conditions)) {
    $conditions = array('source' => $conditions);
  }
  elseif (!is_array($conditions)) {
    return FALSE;
  }
  $select = db_select('url_alias');
  foreach ($conditions as $field => $value) {
    $select->condition($field, $value);
  }
  return $select
    ->fields('url_alias')
    ->orderBy('pid', 'DESC')
    ->range(0, 1)
    ->execute()
    ->fetchAssoc();
}
```

---
_Drupal 7.103 · [includes/path.inc](https://github.com/drupal/drupal/blob/7.103/includes/path.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
