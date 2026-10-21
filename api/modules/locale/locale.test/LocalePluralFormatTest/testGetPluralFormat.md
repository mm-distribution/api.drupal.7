# LocalePluralFormatTest::testGetPluralFormat()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 813–820 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L813-L820)
- **Class:** [LocalePluralFormatTest](../LocalePluralFormatTest.md)
- **Module/theme:** locale

## Signature

```php
function testGetPluralFormat()
```

## Documentation

```text
Tests locale_get_plural() functionality.
```

## Code

```php
  function testGetPluralFormat() {
    $this->drupalGet('locale_test_plural_format_page');
    $tests = _locale_test_plural_format_tests();
    $result = array();
    foreach ($tests as $test) {
      $this->assertPluralFormat($test['count'], $test['language'], $test['expected-result']);
    }
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
