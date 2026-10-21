# hook_preprocess()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/theme.api.php`](_file.md), lines 113–145 · [local source](../../../../source/modules/system/theme.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/theme.api.php#L113-L145)
- **Module/theme:** system

## Signature

```php
function hook_preprocess(&$variables, $hook)
```

## Documentation

```text
Preprocess theme variables for templates.

This hook allows modules to preprocess theme variables for theme templates.
It is called for all theme hooks implemented as templates, but not for theme
hooks implemented as functions. hook_preprocess_HOOK() can be used to
preprocess variables for a specific theme hook, whether implemented as a
template or function.

For more detailed information, see theme().

@param $variables
  The variables array (modify in place).
@param $hook
  The name of the theme hook.
```

## Code

```php
function hook_preprocess(&$variables, $hook) {
 static $hooks;

  // Add contextual links to the variables, if the user has permission.

  if (!user_access('access contextual links')) {
    return;
  }

  if (!isset($hooks)) {
    $hooks = theme_get_registry();
  }

  // Determine the primary theme function argument.
  if (isset($hooks[$hook]['variables'])) {
    $keys = array_keys($hooks[$hook]['variables']);
    $key = $keys[0];
  }
  else {
    $key = $hooks[$hook]['render element'];
  }

  if (isset($variables[$key])) {
    $element = $variables[$key];
  }

  if (isset($element) && is_array($element) && !empty($element['#contextual_links'])) {
    $variables['title_suffix']['contextual_links'] = contextual_links_view($element);
    if (!empty($variables['title_suffix']['contextual_links'])) {
      $variables['classes_array'][] = 'contextual-links-region';
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_preprocess()".

- [contextual_preprocess()](../../contextual/contextual.module/contextual_preprocess.md) — `modules/contextual/contextual.module`

---
_Drupal 7.103 · [modules/system/theme.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/theme.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
