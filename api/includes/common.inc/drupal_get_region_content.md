# drupal_get_region_content()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 193–208 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L193-L208)

## Signature

```php
function drupal_get_region_content($region = NULL, $delimiter = ' ')
```

## Documentation

```text
Gets assigned content for a given region.

@param $region
  A specified region to fetch content for. If NULL, all regions will be
  returned.
@param $delimiter
  Content to be inserted between imploded array elements.
```

## Code

```php
function drupal_get_region_content($region = NULL, $delimiter = ' ') {
  $content = drupal_add_region_content();
  if (isset($region)) {
    if (isset($content[$region]) && is_array($content[$region])) {
      return implode($delimiter, $content[$region]);
    }
  }
  else {
    foreach (array_keys($content) as $region) {
      if (is_array($content[$region])) {
        $content[$region] = implode($delimiter, $content[$region]);
      }
    }
    return $content;
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
