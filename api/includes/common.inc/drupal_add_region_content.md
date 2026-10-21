# drupal_add_region_content()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 175–182 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L175-L182)

## Signature

```php
function drupal_add_region_content($region = NULL, $data = NULL)
```

## Documentation

```text
Adds content to a specified region.

@param $region
  Page region the content is added to.
@param $data
  Content to be added.
```

## Code

```php
function drupal_add_region_content($region = NULL, $data = NULL) {
  static $content = array();

  if (isset($region) && isset($data)) {
    $content[$region][] = $data;
  }
  return $content;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
