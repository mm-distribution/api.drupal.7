# hook_updater_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4683–4696 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4683-L4696)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_updater_info()
```

## Documentation

```text
Provide information on Updaters (classes that can update Drupal).

An Updater is a class that knows how to update various parts of the Drupal
file system, for example to update modules that have newer releases, or to
install a new theme.

@return
  An associative array of information about the updater(s) being provided.
  This array is keyed by a unique identifier for each updater, and the
  values are subarrays that can contain the following keys:
  - class: The name of the PHP class which implements this updater.
  - name: Human-readable name of this updater.
  - weight: Controls what order the Updater classes are consulted to decide
    which one should handle a given task. When an update task is being run,
    the system will loop through all the Updater classes defined in this
    registry in weight order and let each class respond to the task and
    decide if each Updater wants to handle the task. In general, this
    doesn't matter, but if you need to override an existing Updater, make
    sure your Updater has a lighter weight so that it comes first.

@see drupal_get_updaters()
@see hook_updater_info_alter()
```

## Code

```php
function hook_updater_info() {
  return array(
    'module' => array(
      'class' => 'ModuleUpdater',
      'name' => t('Update modules'),
      'weight' => 0,
    ),
    'theme' => array(
      'class' => 'ThemeUpdater',
      'name' => t('Update themes'),
      'weight' => 0,
    ),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_updater_info()".

- [system_updater_info()](../system.module/system_updater_info.md) — `modules/system/system.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
