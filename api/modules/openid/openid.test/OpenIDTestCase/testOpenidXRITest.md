# OpenIDTestCase::testOpenidXRITest()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 720–745 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L720-L745)
- **Class:** [OpenIDTestCase](../OpenIDTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testOpenidXRITest()
```

## Documentation

```text
Test _openid_is_xri().
```

## Code

```php
  function testOpenidXRITest() {
    // Test that the XRI test is according to OpenID Authentication 2.0,
    // section 7.2. If the user-supplied string starts with xri:// it should be
    // stripped and the resulting string should be treated as an XRI when it
    // starts with "=", "@", "+", "$", "!" or "(".
    $this->assertTrue(_openid_is_xri('xri://=foo'), '_openid_is_xri() returned expected result for an xri identifier with xri scheme.');
    $this->assertTrue(_openid_is_xri('xri://@foo'), '_openid_is_xri() returned expected result for an xri identifier with xri scheme.');
    $this->assertTrue(_openid_is_xri('xri://+foo'), '_openid_is_xri() returned expected result for an xri identifier with xri scheme.');
    $this->assertTrue(_openid_is_xri('xri://$foo'), '_openid_is_xri() returned expected result for an xri identifier with xri scheme.');
    $this->assertTrue(_openid_is_xri('xri://!foo'), '_openid_is_xri() returned expected result for an xri identifier with xri scheme..');
    $this->assertTrue(_openid_is_xri('xri://(foo'), '_openid_is_xri() returned expected result for an xri identifier with xri scheme..');

    $this->assertTrue(_openid_is_xri('=foo'), '_openid_is_xri() returned expected result for an xri identifier.');
    $this->assertTrue(_openid_is_xri('@foo'), '_openid_is_xri() returned expected result for an xri identifier.');
    $this->assertTrue(_openid_is_xri('+foo'), '_openid_is_xri() returned expected result for an xri identifier.');
    $this->assertTrue(_openid_is_xri('$foo'), '_openid_is_xri() returned expected result for an xri identifier.');
    $this->assertTrue(_openid_is_xri('!foo'), '_openid_is_xri() returned expected result for an xri identifier.');
    $this->assertTrue(_openid_is_xri('(foo'), '_openid_is_xri() returned expected result for an xri identifier.');

    $this->assertFalse(_openid_is_xri('foo'), '_openid_is_xri() returned expected result for an http URL.');
    $this->assertFalse(_openid_is_xri('xri://foo'), '_openid_is_xri() returned expected result for an http URL.');
    $this->assertFalse(_openid_is_xri('http://foo/'), '_openid_is_xri() returned expected result for an http URL.');
    $this->assertFalse(_openid_is_xri('http://example.com/'), '_openid_is_xri() returned expected result for an http URL.');
    $this->assertFalse(_openid_is_xri('user@example.com/'), '_openid_is_xri() returned expected result for an http URL.');
    $this->assertFalse(_openid_is_xri('http://user@example.com/'), '_openid_is_xri() returned expected result for an http URL.');
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
