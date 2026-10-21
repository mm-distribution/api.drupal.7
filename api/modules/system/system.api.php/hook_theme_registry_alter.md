# hook_theme_registry_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2366–2373 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2366-L2373)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_theme_registry_alter(&$theme_registry)
```

## Documentation

```text
Alter the theme registry information returned from hook_theme().

The theme registry stores information about all available theme hooks,
including which callback functions those hooks will call when triggered,
what template files are exposed by these hooks, and so on.

Note that this hook is only executed as the theme cache is re-built.
Changes here will not be visible until the next cache clear.

The $theme_registry array is keyed by theme hook name, and contains the
information returned from hook_theme(), as well as additional properties
added by _theme_process_registry().

For example:
@code
$theme_registry['user_profile'] = array(
  'variables' => array(
    'account' => NULL,
  ),
  'template' => 'modules/user/user-profile',
  'file' => 'modules/user/user.pages.inc',
  'type' => 'module',
  'theme path' => 'modules/user',
  'preprocess functions' => array(
    0 => 'template_preprocess',
    1 => 'template_preprocess_user_profile',
  ),
);
@endcode

@param $theme_registry
  The entire cache of theme registry information, post-processing.

@see hook_theme()
@see _theme_process_registry()
```

## Code

```php
function hook_theme_registry_alter(&$theme_registry) {
  // Kill the next/previous forum topic navigation links.
  foreach ($theme_registry['forum_topic_navigation']['preprocess functions'] as $key => $value) {
    if ($value == 'template_preprocess_forum_topic_navigation') {
      unset($theme_registry['forum_topic_navigation']['preprocess functions'][$key]);
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_theme_registry_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
