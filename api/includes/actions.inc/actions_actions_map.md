# actions_actions_map()

- **Type:** Function
- **File:** [`includes/actions.inc`](_file.md), lines 216–226 · [local source](../../../source/includes/actions.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc#L216-L226)

## Signature

```php
function actions_actions_map($actions)
```

## Documentation

```text
Creates an associative array keyed by hashes of function names or IDs.

Hashes are used to prevent actual function names from going out into HTML
forms and coming back.

@param $actions
  An associative array with function names or action IDs as keys
  and associative arrays with keys 'label', 'type', etc. as values.
  This is usually the output of actions_list() or actions_get_all_actions().

@return
  An associative array whose keys are hashes of the input array keys, and
  whose corresponding values are associative arrays with components
  'callback', 'label', 'type', and 'configurable' from the input array.
```

## Code

```php
function actions_actions_map($actions) {
  $actions_map = array();
  foreach ($actions as $callback => $array) {
    $key = drupal_hash_base64($callback);
    $actions_map[$key]['callback']     = isset($array['callback']) ? $array['callback'] : $callback;
    $actions_map[$key]['label']        = $array['label'];
    $actions_map[$key]['type']         = $array['type'];
    $actions_map[$key]['configurable'] = $array['configurable'];
  }
  return $actions_map;
}
```

---
_Drupal 7.103 · [includes/actions.inc](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
