# book_menu()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 130–195 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L130-L195)
- **Module/theme:** book
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function book_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function book_menu() {
  $items['admin/content/book'] = array(
    'title' => 'Books',
    'description' => "Manage your site's book outlines.",
    'page callback' => 'book_admin_overview',
    'access arguments' => array('administer book outlines'),
    'type' => MENU_LOCAL_TASK,
    'file' => 'book.admin.inc',
  );
  $items['admin/content/book/list'] = array(
    'title' => 'List',
    'type' => MENU_DEFAULT_LOCAL_TASK,
  );
  $items['admin/content/book/settings'] = array(
    'title' => 'Settings',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('book_admin_settings'),
    'access arguments' => array('administer site configuration'),
    'type' => MENU_LOCAL_TASK,
    'weight' => 8,
    'file' => 'book.admin.inc',
  );
  $items['admin/content/book/%node'] = array(
    'title' => 'Re-order book pages and change titles',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('book_admin_edit', 3),
    'access callback' => '_book_outline_access',
    'access arguments' => array(3),
    'type' => MENU_CALLBACK,
    'file' => 'book.admin.inc',
  );
  $items['book'] = array(
    'title' => 'Books',
    'page callback' => 'book_render',
    'access arguments' => array('access content'),
    'type' => MENU_SUGGESTED_ITEM,
    'file' => 'book.pages.inc',
  );
  $items['book/export/%/%'] = array(
    'page callback' => 'book_export',
    'page arguments' => array(2, 3),
    'access arguments' => array('access printer-friendly version'),
    'type' => MENU_CALLBACK,
    'file' => 'book.pages.inc',
  );
  $items['node/%node/outline'] = array(
    'title' => 'Outline',
    'page callback' => 'book_outline',
    'page arguments' => array(1),
    'access callback' => '_book_outline_access',
    'access arguments' => array(1),
    'type' => MENU_LOCAL_TASK,
    'weight' => 2,
    'file' => 'book.pages.inc',
  );
  $items['node/%node/outline/remove'] = array(
    'title' => 'Remove from outline',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('book_remove_form', 1),
    'access callback' => '_book_outline_remove_access',
    'access arguments' => array(1),
    'file' => 'book.pages.inc',
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
