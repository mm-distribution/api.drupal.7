# hook_custom_theme()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2400–2405 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2400-L2405)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_custom_theme()
```

## Documentation

```text
Return the machine-readable name of the theme to use for the current page.

This hook can be used to dynamically set the theme for the current page
request. It should be used by modules which need to override the theme
based on dynamic conditions (for example, a module which allows the theme to
be set based on the current user's role). The return value of this hook will
be used on all pages except those which have a valid per-page or per-section
theme set via a theme callback function in hook_menu(); the themes on those
pages can only be overridden using hook_menu_alter().

Note that returning different themes for the same path may not work with page
caching. This is most likely to be a problem if an anonymous user on a given
path could have different themes returned under different conditions.

Since only one theme can be used at a time, the last (i.e., highest
weighted) module which returns a valid theme name from this hook will
prevail.

@return
  The machine-readable name of the theme that should be used for the current
  page request. The value returned from this function will only have an
  effect if it corresponds to a currently-active theme on the site. Do not
  return a value if you do not wish to set a custom theme.
```

## Code

```php
function hook_custom_theme() {
  // Allow the user to request a particular theme via a query parameter.
  if (isset($_GET['theme'])) {
    return $_GET['theme'];
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_custom_theme()".

- [menu_test_custom_theme()](../../simpletest/tests/menu_test.module/menu_test_custom_theme.md) — `modules/simpletest/tests/menu_test.module`
- [system_custom_theme()](../system.module/system_custom_theme.md) — `modules/system/system.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
