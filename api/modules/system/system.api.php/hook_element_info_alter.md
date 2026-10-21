# hook_element_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 702–707 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L702-L707)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_element_info_alter(&$type)
```

## Documentation

```text
Alter the element type information returned from modules.

A module may implement this hook in order to alter the element type defaults
defined by a module.

@param $type
  All element type defaults as collected by hook_element_info().

@see hook_element_info()
```

## Code

```php
function hook_element_info_alter(&$type) {
  // Decrease the default size of textfields.
  if (isset($type['textfield']['#size'])) {
    $type['textfield']['#size'] = 40;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_element_info_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
