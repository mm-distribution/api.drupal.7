# _trigger_taxonomy()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 592–599 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L592-L599)
- **Module/theme:** trigger

## Signature

```php
function _trigger_taxonomy($hook, $array)
```

## Documentation

```text
Calls action functions for taxonomy triggers.

@param $hook
  Hook to trigger actions for taxonomy_term_insert(),
  taxonomy_term_update(), and taxonomy_term_delete().
@param $array
  Item on which operation is being performed, either a term or
  form values.
```

## Code

```php
function _trigger_taxonomy($hook, $array) {
  $aids = trigger_get_assigned_actions($hook);
  $context = array(
    'group' => 'taxonomy',
    'hook' => $hook
  );
  actions_do(array_keys($aids), (object) $array, $context);
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
