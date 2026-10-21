# hook_translated_menu_link_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1346–1350 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1346-L1350)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_translated_menu_link_alter(&$item, $map)
```

## Documentation

```text
Alter a menu link after it has been translated and before it is rendered.

This hook is invoked from _menu_link_translate() after a menu link has been
translated; i.e., after dynamic path argument placeholders (%) have been
replaced with actual values, the user access to the link's target page has
been checked, and the link has been localized. It is only invoked if
$item['options']['alter'] has been set to a non-empty value (e.g., TRUE).
This flag should be set using hook_menu_link_alter().

Implementations of this hook are able to alter any property of the menu link.
For example, this hook may be used to add a page-specific query string to all
menu links, or hide a certain link by setting:
@code
  'hidden' => 1,
@endcode

@param $item
  Associative array defining a menu link after _menu_link_translate()
@param $map
  Associative array containing the menu $map (path parts and/or objects).

@see hook_menu_link_alter()
```

## Code

```php
function hook_translated_menu_link_alter(&$item, $map) {
  if ($item['href'] == 'devel/cache/clear') {
    $item['localized_options']['query'] = drupal_get_destination();
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_translated_menu_link_alter()".

- [user_translated_menu_link_alter()](../../user/user.module/user_translated_menu_link_alter.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
