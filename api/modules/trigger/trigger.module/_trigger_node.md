# _trigger_node()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 267–307 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L267-L307)
- **Module/theme:** trigger

## Signature

```php
function _trigger_node($node, $hook, $a3 = NULL, $a4 = NULL)
```

## Documentation

```text
Calls action functions for node triggers.

@param $node
  Node object.
@param $hook
  Hook to trigger.
@param $a3
  Additional argument to action function.
@param $a4
  Additional argument to action function.
```

## Code

```php
function _trigger_node($node, $hook, $a3 = NULL, $a4 = NULL) {
  // Keep objects for reuse so that changes actions make to objects can persist.
  static $objects;
  // Prevent recursion by tracking which operations have already been called.
  static $recursion;

  $aids = trigger_get_assigned_actions($hook);
  if (!$aids) {
    return;
  }

  if (isset($recursion[$hook])) {
    return;
  }
  $recursion[$hook] = TRUE;

  $context = array(
    'group' => 'node',
    'hook' => $hook,
  );

  // We need to get the expected object if the action's type is not 'node'.
  // We keep the object in $objects so we can reuse it if we have multiple actions
  // that make changes to an object.
  foreach ($aids as $aid => $info) {
    $type = $info['type'];
    if ($type != 'node') {
      if (!isset($objects[$type])) {
        $objects[$type] = _trigger_normalize_node_context($type, $node);
      }
      // Since we know about the node, we pass that info along to the action.
      $context['node'] = $node;
      $result = actions_do($aid, $objects[$type], $context, $a3, $a4);
    }
    else {
      actions_do($aid, $node, $context, $a3, $a4);
    }
  }

  unset($recursion[$hook]);
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
