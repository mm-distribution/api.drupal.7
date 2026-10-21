# file_element_info()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 61–83 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L61-L83)
- **Module/theme:** file
- **Implements:** [hook_element_info()](../../system/system.api.php/hook_element_info.md)

## Signature

```php
function file_element_info()
```

## Documentation

```text
Implements hook_element_info().

The managed file element may be used anywhere in Drupal.
```

## Code

```php
function file_element_info() {
  $file_path = drupal_get_path('module', 'file');
  $types['managed_file'] = array(
    '#input' => TRUE,
    '#process' => array('file_managed_file_process'),
    '#value_callback' => 'file_managed_file_value',
    '#element_validate' => array('file_managed_file_validate'),
    '#pre_render' => array('file_managed_file_pre_render'),
    '#theme' => 'file_managed_file',
    '#theme_wrappers' => array('form_element'),
    '#progress_indicator' => 'throbber',
    '#progress_message' => NULL,
    '#upload_validators' => array(),
    '#upload_location' => NULL,
    '#size' => 22,
    '#extended' => FALSE,
    '#attached' => array(
      'css' => array($file_path . '/file.css'),
      'js' => array($file_path . '/file.js'),
    ),
  );
  return $types;
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
