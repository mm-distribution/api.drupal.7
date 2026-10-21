# actions_function_lookup()

- **Type:** Function
- **File:** [`includes/actions.inc`](_file.md), lines 241–259 · [local source](../../../source/includes/actions.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc#L241-L259)

## Signature

```php
function actions_function_lookup($hash)
```

## Documentation

```text
Returns an action array key (function or ID), given its hash.

Faster than actions_actions_map() when you only need the function name or ID.

@param $hash
  Hash of a function name or action ID array key. The array key
  is a key into the return value of actions_list() (array key is the action
  function name) or actions_get_all_actions() (array key is the action ID).

@return
  The corresponding array key, or FALSE if no match is found.
```

## Code

```php
function actions_function_lookup($hash) {
  // Check for a function name match.
  $actions_list = actions_list();
  foreach ($actions_list as $function => $array) {
    if (drupal_hash_base64($function) == $hash) {
      return $function;
    }
  }
  $aid = FALSE;
  // Must be a configurable action; check database.
  $result = db_query("SELECT aid FROM {actions} WHERE parameters <> ''")->fetchAll(PDO::FETCH_ASSOC);
  foreach ($result as $row) {
    if (drupal_hash_base64($row['aid']) == $hash) {
      $aid = $row['aid'];
      break;
    }
  }
  return $aid;
}
```

---
_Drupal 7.103 · [includes/actions.inc](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
