# bartik_menu_tree()

- **Type:** Function
- **File:** [`themes/bartik/template.php`](_file.md), lines 130–132 · [local source](../../../../source/themes/bartik/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/bartik/template.php#L130-L132)
- **Module/theme:** bartik

## Signature

```php
function bartik_menu_tree($variables)
```

## Documentation

```text
Implements theme_menu_tree().
```

## Code

```php
function bartik_menu_tree($variables) {
  return '<ul class="menu clearfix">' . $variables['tree'] . '</ul>';
}
```

---
_Drupal 7.103 · [themes/bartik/template.php](https://github.com/drupal/drupal/blob/7.103/themes/bartik/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
