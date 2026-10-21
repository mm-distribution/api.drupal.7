# announcements_feed_get_announcements()

- **Type:** Function
- **File:** [`modules/announcements_feed/announcements_feed.inc`](_file.md), lines 14–39 · [local source](../../../../source/modules/announcements_feed/announcements_feed.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.inc#L14-L39)
- **Module/theme:** announcements_feed

## Signature

```php
function announcements_feed_get_announcements()
```

## Documentation

```text
Returns the list of announcements.

@return array
  A build array with announcements.
```

## Code

```php
function announcements_feed_get_announcements() {
  drupal_set_title(t('Community announcements'));
  drupal_add_css(drupal_get_path('module', 'announcements_feed')
    . '/announcements_feed.css', array(
      'group' => CSS_DEFAULT,
      'every_page' => TRUE,
    ));
  try {
    $announcements = announcements_feed_get_all_announcements();
  }
  catch (Exception $e) {
    drupal_set_message(t('An error occurred while parsing the announcements feed, check the logs for more information.'), 'error');
    return array();
  }
  $build = array();
  foreach ($announcements as $announcement) {
    $key = $announcement['featured'] ? '#featured' : '#standard';
    $build[$key][] = $announcement;
  }
  $build = array_merge($build, array(
    '#theme' => 'announcements_feed',
    '#count' => count($announcements),
    '#feed_link' => variable_get('announcements_feed_link', ANNOUNCEMENTS_FEED_DEFAULT_LINK),
  ));
  return $build;
}
```

---
_Drupal 7.103 · [modules/announcements_feed/announcements_feed.inc](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
