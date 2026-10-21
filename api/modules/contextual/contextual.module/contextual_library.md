# contextual_library()

- **Type:** Function
- **File:** [`modules/contextual/contextual.module`](_file.md), lines 41–55 · [local source](../../../../source/modules/contextual/contextual.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.module#L41-L55)
- **Module/theme:** contextual
- **Implements:** [hook_library()](../../system/system.api.php/hook_library.md)

## Signature

```php
function contextual_library()
```

## Documentation

```text
Implements hook_library().
```

## Code

```php
function contextual_library() {
  $path = drupal_get_path('module', 'contextual');
  $libraries['contextual-links'] = array(
    'title' => 'Contextual links',
    'website' => 'http://drupal.org/node/473268',
    'version' => '1.0',
    'js' => array(
      $path . '/contextual.js' => array(),
    ),
    'css' => array(
      $path . '/contextual.css' => array(),
    ),
  );
  return $libraries;
}
```

---
_Drupal 7.103 · [modules/contextual/contextual.module](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.module) · Licensed GPL-2.0-or-later (see LICENSE)._
