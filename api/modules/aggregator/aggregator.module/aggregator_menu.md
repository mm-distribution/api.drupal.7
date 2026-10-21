# aggregator_menu()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 98–266 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L98-L266)
- **Module/theme:** aggregator
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function aggregator_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function aggregator_menu() {
  $items['admin/config/services/aggregator'] = array(
    'title' => 'Feed aggregator',
    'description' => "Configure which content your site aggregates from other sites, how often it polls them, and how they're categorized.",
    'page callback' => 'aggregator_admin_overview',
    'access arguments' => array('administer news feeds'),
    'weight' => 10,
    'file' => 'aggregator.admin.inc',
  );
  $items['admin/config/services/aggregator/add/feed'] = array(
    'title' => 'Add feed',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('aggregator_form_feed'),
    'access arguments' => array('administer news feeds'),
    'type' => MENU_LOCAL_ACTION,
    'file' => 'aggregator.admin.inc',
  );
  $items['admin/config/services/aggregator/add/category'] = array(
    'title' => 'Add category',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('aggregator_form_category'),
    'access arguments' => array('administer news feeds'),
    'type' => MENU_LOCAL_ACTION,
    'file' => 'aggregator.admin.inc',
  );
  $items['admin/config/services/aggregator/add/opml'] = array(
    'title' => 'Import OPML',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('aggregator_form_opml'),
    'access arguments' => array('administer news feeds'),
    'type' => MENU_LOCAL_ACTION,
    'file' => 'aggregator.admin.inc',
  );
  $items['admin/config/services/aggregator/remove/%aggregator_feed'] = array(
    'title' => 'Remove items',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('aggregator_admin_remove_feed', 5),
    'access arguments' => array('administer news feeds'),
    'file' => 'aggregator.admin.inc',
  );
  $items['admin/config/services/aggregator/update/%aggregator_feed'] = array(
    'title' => 'Update items',
    'page callback' => 'aggregator_admin_refresh_feed',
    'page arguments' => array(5),
    'access arguments' => array('administer news feeds'),
    'file' => 'aggregator.admin.inc',
  );
  $items['admin/config/services/aggregator/list'] = array(
    'title' => 'List',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
  );
  $items['admin/config/services/aggregator/settings'] = array(
    'title' => 'Settings',
    'description' => 'Configure the behavior of the feed aggregator, including when to discard feed items and how to present feed items and categories.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('aggregator_admin_form'),
    'access arguments' => array('administer news feeds'),
    'type' => MENU_LOCAL_TASK,
    'file' => 'aggregator.admin.inc',
  );
  $items['aggregator'] = array(
    'title' => 'Feed aggregator',
    'page callback' => 'aggregator_page_last',
    'access arguments' => array('access news feeds'),
    'weight' => 5,
    'file' => 'aggregator.pages.inc',
  );
  $items['aggregator/sources'] = array(
    'title' => 'Sources',
    'page callback' => 'aggregator_page_sources',
    'access arguments' => array('access news feeds'),
    'file' => 'aggregator.pages.inc',
  );
  $items['aggregator/categories'] = array(
    'title' => 'Categories',
    'page callback' => 'aggregator_page_categories',
    'access callback' => '_aggregator_has_categories',
    'file' => 'aggregator.pages.inc',
  );
  $items['aggregator/rss'] = array(
    'title' => 'RSS feed',
    'page callback' => 'aggregator_page_rss',
    'access arguments' => array('access news feeds'),
    'type' => MENU_CALLBACK,
    'file' => 'aggregator.pages.inc',
  );
  $items['aggregator/opml'] = array(
    'title' => 'OPML feed',
    'page callback' => 'aggregator_page_opml',
    'access arguments' => array('access news feeds'),
    'type' => MENU_CALLBACK,
    'file' => 'aggregator.pages.inc',
  );
  $items['aggregator/categories/%aggregator_category'] = array(
    'title callback' => '_aggregator_category_title',
    'title arguments' => array(2),
    'page callback' => 'aggregator_page_category',
    'page arguments' => array(2),
    'access arguments' => array('access news feeds'),
    'file' => 'aggregator.pages.inc',
  );
  $items['aggregator/categories/%aggregator_category/view'] = array(
    'title' => 'View',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
  );
  $items['aggregator/categories/%aggregator_category/categorize'] = array(
    'title' => 'Categorize',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('aggregator_page_category_form', 2),
    'access arguments' => array('administer news feeds'),
    'type' => MENU_LOCAL_TASK,
    'file' => 'aggregator.pages.inc',
  );
  $items['aggregator/categories/%aggregator_category/configure'] = array(
    'title' => 'Configure',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('aggregator_form_category', 2),
    'access arguments' => array('administer news feeds'),
    'type' => MENU_LOCAL_TASK,
    'weight' => 1,
    'file' => 'aggregator.admin.inc',
  );
  $items['aggregator/sources/%aggregator_feed'] = array(
    'page callback' => 'aggregator_page_source',
    'page arguments' => array(2),
    'access arguments' => array('access news feeds'),
    'file' => 'aggregator.pages.inc',
  );
  $items['aggregator/sources/%aggregator_feed/view'] = array(
    'title' => 'View',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
  );
  $items['aggregator/sources/%aggregator_feed/categorize'] = array(
    'title' => 'Categorize',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('aggregator_page_source_form', 2),
    'access arguments' => array('administer news feeds'),
    'type' => MENU_LOCAL_TASK,
    'file' => 'aggregator.pages.inc',
  );
  $items['aggregator/sources/%aggregator_feed/configure'] = array(
    'title' => 'Configure',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('aggregator_form_feed', 2),
    'access arguments' => array('administer news feeds'),
    'type' => MENU_LOCAL_TASK,
    'weight' => 1,
    'file' => 'aggregator.admin.inc',
  );
  $items['admin/config/services/aggregator/edit/feed/%aggregator_feed'] = array(
    'title' => 'Edit feed',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('aggregator_form_feed', 6),
    'access arguments' => array('administer news feeds'),
    'file' => 'aggregator.admin.inc',
  );
  $items['admin/config/services/aggregator/edit/category/%aggregator_category'] = array(
    'title' => 'Edit category',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('aggregator_form_category', 6),
    'access arguments' => array('administer news feeds'),
    'file' => 'aggregator.admin.inc',
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
