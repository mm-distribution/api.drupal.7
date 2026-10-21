# announcements_feed_sort_featured()

- **Type:** Function
- **File:** [`modules/announcements_feed/announcements_feed.inc`](_file.md), lines 137–145 · [local source](../../../../source/modules/announcements_feed/announcements_feed.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.inc#L137-L145)
- **Module/theme:** announcements_feed

## Signature

```php
function announcements_feed_sort_featured($a, $b)
```

## Documentation

```text
Sort the elements of announcements_feed by values in comparison function.
```

## Code

```php
function announcements_feed_sort_featured($a, $b) {
  $a_value = (int) $a['_drupalorg']['featured'];
  $b_value = (int) $b['_drupalorg']['featured'];
  if ($a_value == $b_value) {
    return 0;
  }

  return ($a_value < $b_value) ? -1 : 1;
}
```

---
_Drupal 7.103 · [modules/announcements_feed/announcements_feed.inc](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
