# FilterUnitTestCase::assertNormalized()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 1877–1879 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L1877-L1879)
- **Class:** [FilterUnitTestCase](../FilterUnitTestCase.md)
- **Module/theme:** filter

## Signature

```php
function assertNormalized($haystack, $needle, $message = '', $group = 'Other')
```

## Documentation

```text
Asserts that a text transformed to lowercase with HTML entities decoded does contains a given string.

Otherwise fails the test with a given message, similar to all the
SimpleTest assert* functions.

Note that this does not remove nulls, new lines and other characters that
could be used to obscure a tag or an attribute name.

@param $haystack
  Text to look in.
@param $needle
  Lowercase, plain text to look for.
@param $message
  (optional) Message to display if failed. Defaults to an empty string.
@param $group
  (optional) The group this message belongs to. Defaults to 'Other'.
@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  function assertNormalized($haystack, $needle, $message = '', $group = 'Other') {
    return $this->assertTrue(strpos(strtolower(decode_entities($haystack)), $needle) !== FALSE, $message, $group);
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
