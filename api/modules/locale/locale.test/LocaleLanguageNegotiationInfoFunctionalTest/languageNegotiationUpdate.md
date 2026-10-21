# LocaleLanguageNegotiationInfoFunctionalTest::languageNegotiationUpdate()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 3206–3226 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L3206-L3226)
- **Class:** [LocaleLanguageNegotiationInfoFunctionalTest](../LocaleLanguageNegotiationInfoFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
private function languageNegotiationUpdate($op = 'enable')
```

## Documentation

```text
Update language types/negotiation information.

Manually invoke locale_modules_enabled()/locale_modules_disabled() since
they would not be invoked after enabling/disabling locale_test the first
time.
```

## Code

```php
  private function languageNegotiationUpdate($op = 'enable') {
    static $last_op = NULL;
    $modules = array('locale_test');

    // Enable/disable locale_test only if we did not already before.
    if ($last_op != $op) {
      $function = "module_{$op}";
      $function($modules);
      // Reset hook implementation cache.
      module_implements(NULL, FALSE, TRUE);
    }

    drupal_static_reset('language_types_info');
    drupal_static_reset('language_negotiation_info');
    $function = "locale_modules_{$op}d";
    if (function_exists($function)) {
      $function($modules);
    }

    $this->drupalGet('admin/config/regional/language/configure');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
