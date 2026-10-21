# LocalePluralFormatTest::assertPluralFormat()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 833–846 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L833-L846)
- **Class:** [LocalePluralFormatTest](../LocalePluralFormatTest.md)
- **Module/theme:** locale

## Signature

```php
function assertPluralFormat($count, $lang, $expected_result)
```

## Documentation

```text
Helper assert to test locale_get_plural page.

@param $count
 Number for testing.
@param $lang
 Language for testing
@param $expected_result
  Expected result.
@param $message
```

## Code

```php
  function assertPluralFormat($count, $lang, $expected_result) {
    $message_param =  array(
      '@lang' => $lang,
      '@count' => $count,
      '@expected_result' => $expected_result,
    );
    $message = t("Computed plural index for '@lang' with count @count is @expected_result.", $message_param);

    $message_param = array(
      '@lang' => $lang,
      '@expected_result' => $expected_result,
    );
    $this->assertText(format_string('Language: @lang, locale_get_plural: @expected_result.', $message_param, $message));
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
