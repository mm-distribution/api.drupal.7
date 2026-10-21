# nyan_cat_init()

- **Type:** Function
- **File:** [`modules/simpletest/tests/themes/engines/nyan_cat/nyan_cat.engine`](_file.md), lines 11–16 · [local source](../../../../../../../../source/modules/simpletest/tests/themes/engines/nyan_cat/nyan_cat.engine) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/themes/engines/nyan_cat/nyan_cat.engine#L11-L16)
- **Module/theme:** batch_test

## Signature

```php
function nyan_cat_init($template)
```

## Documentation

```text
Includes .theme file from themes.
```

## Code

```php
function nyan_cat_init($template) {
  $file = dirname($template->filename) . '/template.theme';
  if (file_exists($file)) {
    include_once DRUPAL_ROOT . '/' . $file;
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/themes/engines/nyan_cat/nyan_cat.engine](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/themes/engines/nyan_cat/nyan_cat.engine) · Licensed GPL-2.0-or-later (see LICENSE)._
