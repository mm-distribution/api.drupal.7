# locale_test_language_negotiation_info()

- **Type:** Function
- **File:** [`modules/locale/tests/locale_test.module`](_file.md), lines 85–107 · [local source](../../../../../source/modules/locale/tests/locale_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module#L85-L107)
- **Module/theme:** locale_test
- **Implements:** [hook_language_negotiation_info()](../../../system/language.api.php/hook_language_negotiation_info.md)

## Signature

```php
function locale_test_language_negotiation_info()
```

## Documentation

```text
Implements hook_language_negotiation_info().
```

## Code

```php
function locale_test_language_negotiation_info() {
  if (variable_get('locale_test_language_negotiation_info', FALSE)) {
    $info = array(
      'callbacks' => array(
        'language' => 'locale_test_language_provider',
      ),
      'file' => drupal_get_path('module', 'locale_test') .'/locale_test.module',
      'weight' => -10,
      'description' => t('This is a test language provider.'),
    );

    return array(
      'test_language_provider' => array(
        'name' => t('Test'),
        'types' => array(LANGUAGE_TYPE_CONTENT, 'test_language_type', 'fixed_test_language_type'),
      ) + $info,
      'test_language_provider_ts' => array(
        'name' => t('Type-specific test'),
        'types' => array('test_language_type'),
      ) + $info,
    );
  }
}
```

---
_Drupal 7.103 · [modules/locale/tests/locale_test.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
