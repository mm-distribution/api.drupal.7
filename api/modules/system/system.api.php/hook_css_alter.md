# hook_css_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 865–868 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L865-L868)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_css_alter(&$css)
```

## Documentation

```text
Alter CSS files before they are output on the page.

@param $css
  An array of all CSS items (files and inline CSS) being requested on the page.

@see drupal_add_css()
@see drupal_get_css()
```

## Code

```php
function hook_css_alter(&$css) {
  // Remove defaults.css file.
  unset($css[drupal_get_path('module', 'system') . '/defaults.css']);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_css_alter()".

- [locale_css_alter()](../../locale/locale.module/locale_css_alter.md) — `modules/locale/locale.module`
- [seven_css_alter()](../../../themes/seven/template.php/seven_css_alter.md) — `themes/seven/template.php`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
