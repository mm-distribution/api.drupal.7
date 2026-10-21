# filter_fallback_format_title()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 588–591 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L588-L591)
- **Module/theme:** filter

## Signature

```php
function filter_fallback_format_title()
```

## Documentation

```text
Returns the title of the fallback text format.

@return string
  The title of the fallback text format.
```

## Code

```php
function filter_fallback_format_title() {
  $fallback_format = filter_format_load(filter_fallback_format());
  return filter_admin_format_title($fallback_format);
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
