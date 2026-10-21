# filter_test_replace()

- **Type:** Function
- **File:** [`modules/simpletest/tests/filter_test.module`](_file.md), lines 53–63 · [local source](../../../../../source/modules/simpletest/tests/filter_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filter_test.module#L53-L63)
- **Module/theme:** batch_test

## Signature

```php
function filter_test_replace($text, $filter, $format, $langcode, $cache, $cache_id)
```

## Documentation

```text
Implements callback_filter_process().

Process handler for filter_test_replace filter.

Replaces all text with filter and text format information.
```

## Code

```php
function filter_test_replace($text, $filter, $format, $langcode, $cache, $cache_id) {
  $text = array();
  $text[] = 'Filter: ' . $filter->title . ' (' . $filter->name . ')';
  $text[] = 'Format: ' . $format->name . ' (' . $format->format . ')';
  $text[] = 'Language: ' . $langcode;
  $text[] = 'Cache: ' . ($cache ? 'Enabled' : 'Disabled');
  if ($cache_id) {
    $text[] = 'Cache ID: ' . $cache_id;
  }
  return implode("<br />\n", $text);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/filter_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filter_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
