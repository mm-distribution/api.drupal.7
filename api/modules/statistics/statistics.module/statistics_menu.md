# statistics_menu()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 149–217 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L149-L217)
- **Module/theme:** statistics
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function statistics_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function statistics_menu() {
  $items['admin/reports/hits'] = array(
    'title' => 'Recent hits',
    'description' => 'View pages that have recently been visited.',
    'page callback' => 'statistics_recent_hits',
    'access arguments' => array('access statistics'),
    'file' => 'statistics.admin.inc',
  );
  $items['admin/reports/pages'] = array(
    'title' => 'Top pages',
    'description' => 'View pages that have been hit frequently.',
    'page callback' => 'statistics_top_pages',
    'access arguments' => array('access statistics'),
    'weight' => 1,
    'file' => 'statistics.admin.inc',
  );
  $items['admin/reports/visitors'] = array(
    'title' => 'Top visitors',
    'description' => 'View visitors that hit many pages.',
    'page callback' => 'statistics_top_visitors',
    'access arguments' => array('access statistics'),
    'weight' => 2,
    'file' => 'statistics.admin.inc',
  );
  $items['admin/reports/referrers'] = array(
    'title' => 'Top referrers',
    'description' => 'View top referrers.',
    'page callback' => 'statistics_top_referrers',
    'access arguments' => array('access statistics'),
    'file' => 'statistics.admin.inc',
  );
  $items['admin/reports/access/%'] = array(
    'title' => 'Details',
    'description' => 'View access log.',
    'page callback' => 'statistics_access_log',
    'page arguments' => array(3),
    'access arguments' => array('access statistics'),
    'file' => 'statistics.admin.inc',
  );
  $items['admin/config/system/statistics'] = array(
    'title' => 'Statistics',
    'description' => 'Control details about what and how your site logs access statistics.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('statistics_settings_form'),
    'access arguments' => array('administer statistics'),
    'file' => 'statistics.admin.inc',
    'weight' => -15,
  );
  $items['user/%user/track/navigation'] = array(
    'title' => 'Track page visits',
    'page callback' => 'statistics_user_tracker',
    'access callback' => 'user_access',
    'access arguments' => array('access statistics'),
    'type' => MENU_LOCAL_TASK,
    'weight' => 2,
    'file' => 'statistics.pages.inc',
  );
  $items['node/%node/track'] = array(
    'title' => 'Track',
    'page callback' => 'statistics_node_tracker',
    'access callback' => 'user_access',
    'access arguments' => array('access statistics'),
    'type' => MENU_LOCAL_TASK,
    'weight' => 2,
    'file' => 'statistics.pages.inc',
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
