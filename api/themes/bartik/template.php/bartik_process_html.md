# bartik_process_html()

- **Type:** Function
- **File:** [`themes/bartik/template.php`](_file.md), lines 32–37 · [local source](../../../../source/themes/bartik/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/bartik/template.php#L32-L37)
- **Module/theme:** bartik

## Signature

```php
function bartik_process_html(&$variables)
```

## Documentation

```text
Override or insert variables into the page template for HTML output.
```

## Code

```php
function bartik_process_html(&$variables) {
  // Hook into color.module.
  if (module_exists('color')) {
    _color_html_alter($variables);
  }
}
```

---
_Drupal 7.103 · [themes/bartik/template.php](https://github.com/drupal/drupal/blob/7.103/themes/bartik/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
