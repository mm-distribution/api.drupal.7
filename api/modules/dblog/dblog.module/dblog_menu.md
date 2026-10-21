# dblog_menu()

- **Type:** Function
- **File:** [`modules/dblog/dblog.module`](_file.md), lines 39–84 · [local source](../../../../source/modules/dblog/dblog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.module#L39-L84)
- **Module/theme:** dblog
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function dblog_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function dblog_menu() {
  $items['admin/reports/dblog'] = array(
    'title' => 'Recent log messages',
    'description' => 'View events that have recently been logged.',
    'page callback' => 'dblog_overview',
    'access arguments' => array('access site reports'),
    'weight' => -1,
    'file' => 'dblog.admin.inc',
  );
  $items['admin/reports/page-not-found'] = array(
    'title' => "Top 'page not found' errors",
    'description' => "View 'page not found' errors (404s).",
    'page callback' => 'dblog_top',
    'page arguments' => array('page not found'),
    'access arguments' => array('access site reports'),
    'file' => 'dblog.admin.inc',
  );
  $items['admin/reports/access-denied'] = array(
    'title' => "Top 'access denied' errors",
    'description' => "View 'access denied' errors (403s).",
    'page callback' => 'dblog_top',
    'page arguments' => array('access denied'),
    'access arguments' => array('access site reports'),
    'file' => 'dblog.admin.inc',
  );
  $items['admin/reports/event/%'] = array(
    'title' => 'Details',
    'page callback' => 'dblog_event',
    'page arguments' => array(3),
    'access arguments' => array('access site reports'),
    'file' => 'dblog.admin.inc',
  );

  if (module_exists('search')) {
    $items['admin/reports/search'] = array(
      'title' => 'Top search phrases',
      'description' => 'View most popular search phrases.',
      'page callback' => 'dblog_top',
      'page arguments' => array('search'),
      'access arguments' => array('access site reports'),
      'file' => 'dblog.admin.inc',
    );
  }

  return $items;
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.module](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
