# _trigger_comment()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 416–442 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L416-L442)
- **Module/theme:** trigger

## Signature

```php
function _trigger_comment($a1, $hook)
```

## Documentation

```text
Calls action functions for comment triggers.

@param $a1
  Comment object or array of form values.
@param $hook
  Hook to trigger.
```

## Code

```php
function _trigger_comment($a1, $hook) {
  // Keep objects for reuse so that changes actions make to objects can persist.
  static $objects;
  $aids = trigger_get_assigned_actions($hook);
  $context = array(
    'group' => 'comment',
    'hook' => $hook,
  );
  // We need to get the expected object if the action's type is not 'comment'.
  // We keep the object in $objects so we can reuse it if we have multiple
  // actions that make changes to an object.
  foreach ($aids as $aid => $info) {
    $type = $info['type'];
    if ($type != 'comment') {
      if (!isset($objects[$type])) {
        $objects[$type] = _trigger_normalize_comment_context($type, $a1);
      }
      // Since we know about the comment, we pass it along to the action
      // in case it wants to peek at it.
      $context['comment'] = (object) $a1;
      actions_do($aid, $objects[$type], $context);
    }
    else {
      actions_do($aid, $a1, $context);
    }
  }
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
