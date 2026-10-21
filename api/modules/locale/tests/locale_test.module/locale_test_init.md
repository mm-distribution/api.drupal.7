# locale_test_init()

- **Type:** Function
- **File:** [`modules/locale/tests/locale_test.module`](_file.md), lines 33–38 · [local source](../../../../../source/modules/locale/tests/locale_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module#L33-L38)
- **Module/theme:** locale_test
- **Implements:** [hook_init()](../../../system/system.api.php/hook_init.md)

## Signature

```php
function locale_test_init()
```

## Documentation

```text
Implements hook_init().
```

## Code

```php
function locale_test_init() {
  locale_test_store_language_negotiation();
  if (isset($GLOBALS['language']) && isset($GLOBALS['language']->provider)) {
    drupal_set_message(t('Language negotiation provider: @name', array('@name' => $GLOBALS['language']->provider)));
  }
}
```

---
_Drupal 7.103 · [modules/locale/tests/locale_test.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
