# garland_preprocess_region()

- **Type:** Function
- **File:** [`themes/garland/template.php`](_file.md), lines 152–156 · [local source](../../../../source/themes/garland/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php#L152-L156)
- **Module/theme:** garland

## Signature

```php
function garland_preprocess_region(&$variables)
```

## Documentation

```text
Override or insert variables into the region template.
```

## Code

```php
function garland_preprocess_region(&$variables) {
  if ($variables['region'] == 'header') {
    $variables['classes_array'][] = 'clearfix';
  }
}
```

---
_Drupal 7.103 · [themes/garland/template.php](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
