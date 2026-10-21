# drupal_get_feeds()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 392–395 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L392-L395)

## Signature

```php
function drupal_get_feeds($delimiter = "\n")
```

## Documentation

```text
Gets the feed URLs for the current page.

@param $delimiter
  A delimiter to split feeds by.
```

## Code

```php
function drupal_get_feeds($delimiter = "\n") {
  $feeds = drupal_add_feed();
  return implode($delimiter, $feeds);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
