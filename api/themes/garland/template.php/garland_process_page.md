# garland_process_page()

- **Type:** Function
- **File:** [`themes/garland/template.php`](_file.md), lines 142–147 · [local source](../../../../source/themes/garland/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php#L142-L147)
- **Module/theme:** garland

## Signature

```php
function garland_process_page(&$variables)
```

## Documentation

```text
Override or insert variables into the page template.
```

## Code

```php
function garland_process_page(&$variables) {
  // Hook into color.module
  if (module_exists('color')) {
    _color_page_alter($variables);
  }
}
```

---
_Drupal 7.103 · [themes/garland/template.php](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
