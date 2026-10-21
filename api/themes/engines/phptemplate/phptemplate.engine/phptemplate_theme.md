# phptemplate_theme()

- **Type:** Function
- **File:** [`themes/engines/phptemplate/phptemplate.engine`](_file.md), lines 21–25 · [local source](../../../../../source/themes/engines/phptemplate/phptemplate.engine) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/engines/phptemplate/phptemplate.engine#L21-L25)
- **Implements:** [hook_theme()](../../../../modules/system/system.api.php/hook_theme.md)

## Signature

```php
function phptemplate_theme($existing, $type, $theme, $path)
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function phptemplate_theme($existing, $type, $theme, $path) {
  $templates = drupal_find_theme_functions($existing, array($theme));
  $templates += drupal_find_theme_templates($existing, '.tpl.php', $path);
  return $templates;
}
```

---
_Drupal 7.103 · [themes/engines/phptemplate/phptemplate.engine](https://github.com/drupal/drupal/blob/7.103/themes/engines/phptemplate/phptemplate.engine) · Licensed GPL-2.0-or-later (see LICENSE)._
