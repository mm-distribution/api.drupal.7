# drupal_implode_tags()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 7830–7841 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L7830-L7841)

## Signature

```php
function drupal_implode_tags($tags)
```

## Documentation

```text
Implodes an array of tags into a string.

@see drupal_explode_tags()
```

## Code

```php
function drupal_implode_tags($tags) {
  $encoded_tags = array();
  foreach ($tags as $tag) {
    // Commas and quotes in tag names are special cases, so encode them.
    if (strpos($tag, ',') !== FALSE || strpos($tag, '"') !== FALSE) {
      $tag = '"' . str_replace('"', '""', $tag) . '"';
    }

    $encoded_tags[] = $tag;
  }
  return implode(', ', $encoded_tags);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
