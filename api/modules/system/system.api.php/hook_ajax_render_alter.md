# hook_ajax_render_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 878–881 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L878-L881)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_ajax_render_alter(&$commands)
```

## Documentation

```text
Alter the commands that are sent to the user through the Ajax framework.

@param $commands
  An array of all commands that will be sent to the user.

@see ajax_render()
```

## Code

```php
function hook_ajax_render_alter(&$commands) {
  // Inject any new status messages into the content area.
  $commands[] = ajax_command_prepend('#block-system-main .content', theme('status_messages'));
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_ajax_render_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
