# garland_process_html()

- **Type:** Function
- **File:** [`themes/garland/template.php`](_file.md), lines 46–51 · [local source](../../../../source/themes/garland/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php#L46-L51)
- **Module/theme:** garland

## Signature

```php
function garland_process_html(&$variables)
```

## Documentation

```text
Override or insert variables into the html template.
```

## Code

```php
function garland_process_html(&$variables) {
  // Hook into color.module
  if (module_exists('color')) {
    _color_html_alter($variables);
  }
}
```

---
_Drupal 7.103 · [themes/garland/template.php](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
