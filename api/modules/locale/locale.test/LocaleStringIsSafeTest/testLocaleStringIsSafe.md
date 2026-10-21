# LocaleStringIsSafeTest::testLocaleStringIsSafe()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 3308–3329 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L3308-L3329)
- **Class:** [LocaleStringIsSafeTest](../LocaleStringIsSafeTest.md)
- **Module/theme:** locale

## Signature

```php
public function testLocaleStringIsSafe()
```

## Documentation

```text
Tests for locale_string_is_safe().
```

## Code

```php
  public function testLocaleStringIsSafe() {
    // Check a translatable string without HTML.
    $string = 'Hello world!';
    $result = locale_string_is_safe($string);
    $this->assertTrue($result);

    // Check a translatable string which includes trustable HTML.
    $string = 'Hello <strong>world</strong>!';
    $result = locale_string_is_safe($string);
    $this->assertTrue($result);

    // Check an untranslatable string which includes untrustable HTML (according
    // to the locale_string_is_safe() function definition).
    $string = 'Hello <img src="world.png" alt="world" />!';
    $result = locale_string_is_safe($string);
    $this->assertFalse($result);

    // Check a translatable string which includes a token in an href attribute.
    $string = 'Hi <a href="[current-user:url]">user</a>';
    $result = locale_string_is_safe($string);
    $this->assertTrue($result);
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
