# announce_feed_test_set_feed_config()

- **Type:** Function
- **File:** [`modules/announcements_feed/tests/announce_feed_test.module`](_file.md), lines 26–35 · [local source](../../../../../source/modules/announcements_feed/tests/announce_feed_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.module#L26-L35)
- **Module/theme:** announce_feed_test

## Signature

```php
function announce_feed_test_set_feed_config($json_name)
```

## Documentation

```text
Helper function to set announcements feed URL.
```

## Code

```php
function announce_feed_test_set_feed_config($json_name) {
  $file = __DIR__ . "/announce_feed/$json_name.json";
  if (!is_file($file)) {
    // Return an empty response.
    drupal_not_found();
  }

  $contents = file_get_contents($file);
  drupal_json_output(drupal_json_decode($contents));
}
```

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.module](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
