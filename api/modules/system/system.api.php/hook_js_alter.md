# hook_js_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 746–749 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L746-L749)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_js_alter(&$javascript)
```

## Documentation

```text
Perform necessary alterations to the JavaScript before it is presented on
the page.

@param $javascript
  An array of all JavaScript being presented on the page.

@see drupal_add_js()
@see drupal_get_js()
@see drupal_js_defaults()
```

## Code

```php
function hook_js_alter(&$javascript) {
  // Swap out jQuery to use an updated version of the library.
  $javascript['misc/jquery.js']['data'] = drupal_get_path('module', 'jquery_update') . '/jquery.js';
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_js_alter()".

- [locale_js_alter()](../../locale/locale.module/locale_js_alter.md) — `modules/locale/locale.module`
- [simpletest_js_alter()](../../simpletest/simpletest.module/simpletest_js_alter.md) — `modules/simpletest/simpletest.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
