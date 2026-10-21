# drupal_region_class()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 4182–4184 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L4182-L4184)

## Signature

```php
function drupal_region_class($region)
```

## Documentation

```text
Provides a standard HTML class name that identifies a page region.

It is recommended that template preprocess functions apply this class to any
page region that is output by the theme (Drupal core already handles this in
the standard template preprocess implementation). Standardizing the class
names in this way allows modules to implement certain features, such as
drag-and-drop or dynamic Ajax loading, in a theme-independent way.

@param $region
  The name of the page region (for example, 'page_top' or 'content').

@return
  An HTML class that identifies the region (for example, 'region-page-top'
  or 'region-content').

@see template_preprocess_region()
```

## Code

```php
function drupal_region_class($region) {
  return drupal_html_class("region-$region");
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
