# OpenIDTestCase::testOpenidNormalize()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 750–764 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L750-L764)
- **Class:** [OpenIDTestCase](../OpenIDTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testOpenidNormalize()
```

## Documentation

```text
Test openid_normalize().
```

## Code

```php
  function testOpenidNormalize() {
    // Test that the normalization is according to OpenID Authentication 2.0,
    // section 7.2 and 11.5.2.

    $this->assertEqual(openid_normalize('$foo'), '$foo', 'openid_normalize() correctly normalized an XRI.');
    $this->assertEqual(openid_normalize('xri://$foo'), '$foo', 'openid_normalize() correctly normalized an XRI with an xri:// scheme.');

    $this->assertEqual(openid_normalize('example.com/'), 'http://example.com/', 'openid_normalize() correctly normalized a URL with a missing scheme.');
    $this->assertEqual(openid_normalize('example.com'), 'http://example.com/', 'openid_normalize() correctly normalized a URL with a missing scheme and empty path.');
    $this->assertEqual(openid_normalize('http://example.com'), 'http://example.com/', 'openid_normalize() correctly normalized a URL with an empty path.');

    $this->assertEqual(openid_normalize('http://example.com/path'), 'http://example.com/path', 'openid_normalize() correctly normalized a URL with a path.');

    $this->assertEqual(openid_normalize('http://example.com/path#fragment'), 'http://example.com/path', 'openid_normalize() correctly normalized a URL with a fragment.');
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
