# announcements_feed_menu()

- **Type:** Function
- **File:** [`modules/announcements_feed/announcements_feed.module`](_file.md), lines 54–71 · [local source](../../../../source/modules/announcements_feed/announcements_feed.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module#L54-L71)
- **Module/theme:** announcements_feed
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function announcements_feed_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function announcements_feed_menu() {
  $items['admin/announcements_feed'] = array(
    'title' => 'Announcements',
    'description' => 'Announcements and updates posted by the drupal.org community.',
    'page callback' => 'announcements_feed_get_announcements',
    'access arguments' => array('access announcements'),
    'position' => 'left',
    'weight' => 2,
    'file' => 'announcements_feed.inc',
    'options' => array(
      'attributes' => array(
        'class' => array('announcement-menu-class'),
      ),
    ),
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/announcements_feed/announcements_feed.module](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module) · Licensed GPL-2.0-or-later (see LICENSE)._
