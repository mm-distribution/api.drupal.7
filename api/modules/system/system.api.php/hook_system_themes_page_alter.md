# hook_system_themes_page_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4300–4311 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4300-L4311)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_system_themes_page_alter(&$theme_groups)
```

## Documentation

```text
Alters theme operation links.

@param $theme_groups
  An associative array containing groups of themes.

@see system_themes_page()
```

## Code

```php
function hook_system_themes_page_alter(&$theme_groups) {
  foreach ($theme_groups as $state => &$group) {
    foreach ($theme_groups[$state] as &$theme) {
      // Add a foo link to each list of theme operations.
      $theme->operations[] = array(
        'title' => t('Foo'),
        'href' => 'admin/appearance/foo',
        'query' => array('theme' => $theme->name)
      );
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_system_themes_page_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
