# filter_menu()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 88–141 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L88-L141)
- **Module/theme:** filter
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function filter_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function filter_menu() {
  $items['filter/tips'] = array(
    'title' => 'Compose tips',
    'page callback' => 'filter_tips_long',
    'access callback' => TRUE,
    'type' => MENU_SUGGESTED_ITEM,
    'file' => 'filter.pages.inc',
  );
  $items['filter/tips/%filter_format'] = array(
    'title' => 'Compose tips',
    'page callback' => 'filter_tips_long',
    'page arguments' => array(2),
    'access callback' => 'filter_access',
    'access arguments' => array(2),
    'file' => 'filter.pages.inc',
  );
  $items['admin/config/content/formats'] = array(
    'title' => 'Text formats',
    'description' => 'Configure how content input by users is filtered, including allowed HTML tags. Also allows enabling of module-provided filters.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('filter_admin_overview'),
    'access arguments' => array('administer filters'),
    'file' => 'filter.admin.inc',
  );
  $items['admin/config/content/formats/list'] = array(
    'title' => 'List',
    'type' => MENU_DEFAULT_LOCAL_TASK,
  );
  $items['admin/config/content/formats/add'] = array(
    'title' => 'Add text format',
    'page callback' => 'filter_admin_format_page',
    'access arguments' => array('administer filters'),
    'type' => MENU_LOCAL_ACTION,
    'weight' => 1,
    'file' => 'filter.admin.inc',
  );
  $items['admin/config/content/formats/%filter_format'] = array(
    'title callback' => 'filter_admin_format_title',
    'title arguments' => array(4),
    'page callback' => 'filter_admin_format_page',
    'page arguments' => array(4),
    'access arguments' => array('administer filters'),
    'file' => 'filter.admin.inc',
  );
  $items['admin/config/content/formats/%filter_format/disable'] = array(
    'title' => 'Disable text format',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('filter_admin_disable', 4),
    'access callback' => '_filter_disable_format_access',
    'access arguments' => array(4),
    'file' => 'filter.admin.inc',
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
