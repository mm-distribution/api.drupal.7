# php_disable()

- **Type:** Function
- **File:** [`modules/php/php.install`](_file.md), lines 43–45 · [local source](../../../../source/modules/php/php.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/php/php.install#L43-L45)
- **Module/theme:** php
- **Implements:** [hook_disable()](../../system/system.api.php/hook_disable.md)

## Signature

```php
function php_disable()
```

## Documentation

```text
Implements hook_disable().
```

## Code

```php
function php_disable() {
  drupal_set_message(t('The PHP module has been disabled. Any existing content that was using the PHP filter will now be visible in plain text. This might pose a security risk by exposing sensitive information, if any, used in the PHP code.'));
}
```

---
_Drupal 7.103 · [modules/php/php.install](https://github.com/drupal/drupal/blob/7.103/modules/php/php.install) · Licensed GPL-2.0-or-later (see LICENSE)._
