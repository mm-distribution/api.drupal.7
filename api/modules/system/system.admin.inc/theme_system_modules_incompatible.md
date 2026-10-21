# theme_system_modules_incompatible()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2707–2709 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2707-L2709)
- **Module/theme:** system
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_system_modules_incompatible($variables)
```

## Documentation

```text
Returns HTML for a message about incompatible modules.

@param $variables
  An associative array containing:
  - message: The form array representing the currently disabled modules.

@ingroup themeable
```

## Code

```php
function theme_system_modules_incompatible($variables) {
  return '<div class="incompatible">' . $variables['message'] . '</div>';
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
