# file_theme()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 88–115 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L88-L115)
- **Module/theme:** file
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function file_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function file_theme() {
  return array(
    // file.module.
    'file_link' => array(
      'variables' => array('file' => NULL, 'icon_directory' => NULL),
    ),
    'file_icon' => array(
      'variables' => array('file' => NULL, 'icon_directory' => NULL, 'alt' => ''),
    ),
    'file_managed_file' => array(
      'render element' => 'element',
    ),

    // file.field.inc.
    'file_widget' => array(
      'render element' => 'element',
    ),
    'file_widget_multiple' => array(
      'render element' => 'element',
    ),
    'file_formatter_table' => array(
      'variables' => array('items' => NULL),
    ),
    'file_upload_help' => array(
      'variables' => array('description' => NULL, 'upload_validators' => NULL),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
