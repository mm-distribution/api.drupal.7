# filter_theme()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 44–68 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L44-L68)
- **Module/theme:** filter
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function filter_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function filter_theme() {
  return array(
    'filter_admin_overview' => array(
      'render element' => 'form',
      'file' => 'filter.admin.inc',
    ),
    'filter_admin_format_filter_order' => array(
      'render element' => 'element',
      'file' => 'filter.admin.inc',
    ),
    'filter_tips' => array(
      'variables' => array('tips' => NULL, 'long' => FALSE),
      'file' => 'filter.pages.inc',
    ),
    'text_format_wrapper' => array(
      'render element' => 'element',
    ),
    'filter_tips_more_info' => array(
      'variables' => array(),
    ),
    'filter_guidelines' => array(
      'variables' => array('format' => NULL),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
