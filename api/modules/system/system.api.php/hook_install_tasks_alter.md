# hook_install_tasks_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3944–3948 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3944-L3948)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_install_tasks_alter(&$tasks, $install_state)
```

## Documentation

```text
Alter the full list of installation tasks.

This hook is invoked on the install profile in install_tasks().

@param $tasks
  An array of all available installation tasks, including those provided by
  Drupal core. You can modify this array to change or replace any part of
  the Drupal installation process that occurs after the installation profile
  is selected.
@param $install_state
  An array of information about the current installation state.

@see hook_install_tasks()
@see install_tasks()
```

## Code

```php
function hook_install_tasks_alter(&$tasks, $install_state) {
  // Replace the "Choose language" installation task provided by Drupal core
  // with a custom callback function defined by this installation profile.
  $tasks['install_select_locale']['function'] = 'myprofile_locale_selection';
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_install_tasks_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
