# _locale_test_plural_format_tests()

- **Type:** Function
- **File:** [`modules/locale/tests/locale_test.module`](_file.md), lines 162–242 · [local source](../../../../../source/modules/locale/tests/locale_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module#L162-L242)
- **Module/theme:** locale_test

## Signature

```php
function _locale_test_plural_format_tests()
```

## Documentation

```text
Helper function with list of test cases

@return array
```

## Code

```php
function _locale_test_plural_format_tests() {
  return array(
    // Test data for English (no formula present).
    array(
      'count' => 1,
      'language' => 'en',
      'expected-result' => 0,
    ),
    array(
      'count' => 0,
      'language' => 'en',
      'expected-result' => 1,
    ),
    array(
      'count' => 5,
      'language' => 'en',
      'expected-result' => 1,
    ),

    // Test data for French (simpler formula).
    array(
      'count' => 1,
      'language' => 'fr',
      'expected-result' => 0,
    ),
    array(
      'count' => 0,
      'language' => 'fr',
      'expected-result' => 1,
    ),
    array(
      'count' => 5,
      'language' => 'fr',
      'expected-result' => 1,
    ),

    // Test data for Croatian (more complex formula).
    array(
      'count' => 1,
      'language' => 'hr',
      'expected-result' => 0,
    ),
    array(
      'count' => 21,
      'language' => 'hr',
      'expected-result' => 0,
    ),
    array(
      'count' => 0,
      'language' => 'hr',
      'expected-result' => 2,
    ),
    array(
      'count' => 2,
      'language' => 'hr',
      'expected-result' => 1,
    ),
    array(
      'count' => 8,
      'language' => 'hr',
      'expected-result' => 2,
    ),

    // Test data for Hungarian (nonexistent language).
    array(
      'count' => 1,
      'language' => 'hu',
      'expected-result' => -1,
    ),
    array(
      'count' => 21,
      'language' => 'hu',
      'expected-result' => -1,
    ),
    array(
      'count' => 0,
      'language' => 'hu',
      'expected-result' => -1,
    ),
  );
}
```

---
_Drupal 7.103 · [modules/locale/tests/locale_test.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/tests/locale_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
