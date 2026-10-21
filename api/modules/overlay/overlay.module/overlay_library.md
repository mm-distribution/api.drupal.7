# overlay_library()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 217–250 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L217-L250)
- **Module/theme:** overlay
- **Implements:** [hook_library()](../../system/system.api.php/hook_library.md)

## Signature

```php
function overlay_library()
```

## Documentation

```text
Implements hook_library().
```

## Code

```php
function overlay_library() {
  $module_path = drupal_get_path('module', 'overlay');

  // Overlay parent.
  $libraries['parent'] = array(
    'title' => 'Overlay: Parent',
    'website' => 'http://drupal.org/documentation/modules/overlay',
    'version' => '1.0',
    'js' => array(
      $module_path . '/overlay-parent.js' => array(),
    ),
    'css' => array(
      $module_path . '/overlay-parent.css' => array(),
    ),
    'dependencies' => array(
      array('system', 'ui'),
      array('system', 'jquery.bbq'),
    ),
  );
  // Overlay child.
  $libraries['child'] = array(
    'title' => 'Overlay: Child',
    'website' => 'http://drupal.org/documentation/modules/overlay',
    'version' => '1.0',
    'js' => array(
      $module_path . '/overlay-child.js' => array(),
    ),
    'css' => array(
      $module_path . '/overlay-child.css' => array(),
    ),
  );

  return $libraries;
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
