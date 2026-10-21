# _trigger_user()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 558–580 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L558-L580)
- **Module/theme:** trigger

## Signature

```php
function _trigger_user($hook, &$edit, $account, $category = NULL)
```

## Documentation

```text
Calls action functions for user triggers.

@param $hook
  The hook that called this function.
@param $edit
  Edit variable passed in to the hook or empty array if not needed.
@param $account
  Account variable passed in to the hook.
@param $method
  Method variable passed in to the hook or NULL if not needed.
```

## Code

```php
function _trigger_user($hook, &$edit, $account, $category = NULL) {
  // Keep objects for reuse so that changes actions make to objects can persist.
  static $objects;
  $aids = trigger_get_assigned_actions($hook);
  $context = array(
    'group' => 'user',
    'hook' => $hook,
    'form_values' => &$edit,
  );
  foreach ($aids as $aid => $info) {
    $type = $info['type'];
    if ($type != 'user') {
      if (!isset($objects[$type])) {
        $objects[$type] = _trigger_normalize_user_context($type, $account);
      }
      $context['user'] = $account;
      actions_do($aid, $objects[$type], $context);
    }
    else {
      actions_do($aid, $account, $context, $category);
    }
  }
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
