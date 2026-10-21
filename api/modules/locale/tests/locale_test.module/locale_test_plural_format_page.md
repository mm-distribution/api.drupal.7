# locale_test_plural_format_page()

- **Type:** Function
- **File:** [`modules/locale/tests/locale_test.module`](_file.md), lines 141–155 · [local source](../../../../../source/modules/locale/tests/locale_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module#L141-L155)
- **Module/theme:** locale_test

## Signature

```php
function locale_test_plural_format_page()
```

## Documentation

```text
Returns markup for locale_get_plural testing.

@return array
```

## Code

```php
function locale_test_plural_format_page() {
  $tests = _locale_test_plural_format_tests();
  $result = array();
  foreach ($tests as $test) {
    $string_param = array(
      '@lang' => $test['language'],
      '@locale_get_plural' => locale_get_plural($test['count'], $test['language'])
    );
    $result[] = array(
      '#prefix' => '<br/>',
      '#markup' => format_string('Language: @lang, locale_get_plural: @locale_get_plural.', $string_param),
    );
  }
  return $result;
}
```

---
_Drupal 7.103 · [modules/locale/tests/locale_test.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
