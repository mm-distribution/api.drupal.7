# garland_preprocess_node()

- **Type:** Function
- **File:** [`themes/garland/template.php`](_file.md), lines 120–122 · [local source](../../../../source/themes/garland/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php#L120-L122)
- **Module/theme:** garland

## Signature

```php
function garland_preprocess_node(&$variables)
```

## Documentation

```text
Override or insert variables into the node template.
```

## Code

```php
function garland_preprocess_node(&$variables) {
  $variables['submitted'] = $variables['date'] . ' — ' . $variables['name'];
}
```

---
_Drupal 7.103 · [themes/garland/template.php](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
