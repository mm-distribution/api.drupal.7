# nyan_cat_theme()

- **Type:** Function
- **File:** [`modules/simpletest/tests/themes/engines/nyan_cat/nyan_cat.engine`](_file.md), lines 21–25 · [local source](../../../../../../../../source/modules/simpletest/tests/themes/engines/nyan_cat/nyan_cat.engine) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/themes/engines/nyan_cat/nyan_cat.engine#L21-L25)
- **Module/theme:** batch_test
- **Implements:** [hook_theme()](../../../../../../system/system.api.php/hook_theme.md)

## Signature

```php
function nyan_cat_theme($existing, $type, $theme, $path)
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function nyan_cat_theme($existing, $type, $theme, $path) {
  $templates = drupal_find_theme_functions($existing, array($theme));
  $templates += drupal_find_theme_templates($existing, '.nyan-cat.html', $path);
  return $templates;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/themes/engines/nyan_cat/nyan_cat.engine](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/themes/engines/nyan_cat/nyan_cat.engine) · Licensed GPL-2.0-or-later (see LICENSE)._
