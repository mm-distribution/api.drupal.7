# phptemplate_init()

- **Type:** Function
- **File:** [`themes/engines/phptemplate/phptemplate.engine`](_file.md), lines 11–16 · [local source](../../../../../source/themes/engines/phptemplate/phptemplate.engine) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/engines/phptemplate/phptemplate.engine#L11-L16)
- **Implements:** [hook_init()](../../../../modules/system/system.api.php/hook_init.md)

## Signature

```php
function phptemplate_init($template)
```

## Documentation

```text
Implements hook_init().
```

## Code

```php
function phptemplate_init($template) {
  $file = dirname($template->filename) . '/template.php';
  if (file_exists($file)) {
    include_once DRUPAL_ROOT . '/' . $file;
  }
}
```

---
_Drupal 7.103 · [themes/engines/phptemplate/phptemplate.engine](https://github.com/drupal/drupal/blob/7.103/themes/engines/phptemplate/phptemplate.engine) · Licensed GPL-2.0-or-later (see LICENSE)._
