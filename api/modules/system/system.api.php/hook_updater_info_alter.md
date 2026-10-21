# hook_updater_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4712–4716 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4712-L4716)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_updater_info_alter(&$updaters)
```

## Documentation

```text
Alter the Updater information array.

An Updater is a class that knows how to update various parts of the Drupal
file system, for example to update modules that have newer releases, or to
install a new theme.

@param array $updaters
  Associative array of updaters as defined through hook_updater_info().
  Alter this array directly.

@see drupal_get_updaters()
@see hook_updater_info()
```

## Code

```php
function hook_updater_info_alter(&$updaters) {
  // Adjust weight so that the theme Updater gets a chance to handle a given
  // update task before module updaters.
  $updaters['theme']['weight'] = -1;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_updater_info_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
