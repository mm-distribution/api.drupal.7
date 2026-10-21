# tracker_menu()

- **Type:** Function
- **File:** [`modules/tracker/tracker.module`](_file.md), lines 32–69 · [local source](../../../../source/modules/tracker/tracker.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module#L32-L69)
- **Module/theme:** tracker
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function tracker_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function tracker_menu() {
  $items['tracker'] = array(
    'title' => 'Recent content',
    'page callback' => 'tracker_page',
    'access arguments' => array('access content'),
    'weight' => 1,
    'file' => 'tracker.pages.inc',
  );
  $items['tracker/all'] = array(
    'title' => 'All recent content',
    'type' => MENU_DEFAULT_LOCAL_TASK,
  );
  $items['tracker/%user_uid_optional'] = array(
    'title' => 'My recent content',
    'page callback' => 'tracker_page',
    'access callback' => '_tracker_myrecent_access',
    'access arguments' => array(1),
    'page arguments' => array(1),
    'type' => MENU_LOCAL_TASK,
    'file' => 'tracker.pages.inc',
  );

  $items['user/%user/track'] = array(
    'title' => 'Track',
    'page callback' => 'tracker_page',
    'page arguments' => array(1, TRUE),
    'access callback' => '_tracker_user_access',
    'access arguments' => array(1),
    'type' => MENU_LOCAL_TASK,
    'file' => 'tracker.pages.inc',
  );
  $items['user/%user/track/content'] = array(
    'title' => 'Track content',
    'type' => MENU_DEFAULT_LOCAL_TASK,
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.module](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module) · Licensed GPL-2.0-or-later (see LICENSE)._
