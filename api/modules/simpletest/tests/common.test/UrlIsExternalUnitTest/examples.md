# UrlIsExternalUnitTest::examples()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 456–483 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L456-L483)
- **Class:** [UrlIsExternalUnitTest](../UrlIsExternalUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
protected function examples()
```

## Documentation

```text
Provides data for testUrlIsExternal().

@return array
  An array of test data, keyed by a path, with the expected value where
  TRUE is external, and FALSE is not external.
```

## Code

```php
  protected function examples() {
    return array(
      // Simple external URLs.
      'http://example.com' => TRUE,
      'https://example.com' => TRUE,
      'http://drupal.org/foo/bar?foo=bar&bar=baz&baz#foo' => TRUE,
      '//drupal.org' => TRUE,
      // Some browsers ignore or strip leading control characters.
      "\x00//www.example.com" => TRUE,
      "\x08//www.example.com" => TRUE,
      "\x1F//www.example.com" => TRUE,
      "\n//www.example.com" => TRUE,
      // JSON supports decoding directly from UTF-8 code points.
      json_decode('"\u00AD"') . "//www.example.com" => TRUE,
      json_decode('"\u200E"') . "//www.example.com" => TRUE,
      json_decode('"\uE0020"') . "//www.example.com" => TRUE,
      json_decode('"\uE000"')  . "//www.example.com" => TRUE,
      // Backslashes should be normalized to forward.
      '\\\\example.com' => TRUE,
      // Local URLs.
      'node' => FALSE,
      '/system/ajax' => FALSE,
      '?q=foo:bar' => FALSE,
      'node/edit:me' => FALSE,
      '/drupal.org' => FALSE,
      '<front>' => FALSE,
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
