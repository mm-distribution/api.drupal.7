# OpenIDTestCase::testOpenidSignature()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 700–715 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L700-L715)
- **Class:** [OpenIDTestCase](../OpenIDTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testOpenidSignature()
```

## Documentation

```text
Test _openid_signature().
```

## Code

```php
  function testOpenidSignature() {
    // Test that signature is calculated according to OpenID Authentication 2.0,
    // section 6.1. In the following array, only the two first entries should be
    // included in the calculation, because the substring following the period
    // is mentioned in the third argument for _openid_signature(). The last
    // entry should not be included, because it does not start with "openid.".
    $response = array(
      'openid.foo' => 'abc1',
      'openid.bar' => 'abc2',
      'openid.baz' => 'abc3',
      'foobar.foo' => 'abc4',
    );
    $association = new stdClass();
    $association->mac_key = "1234567890abcdefghij\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9";
    $this->assertEqual(_openid_signature($association, $response, array('foo', 'bar')), 'QnKZQzSFstT+GNiJDFOptdcZjrc=', 'Expected signature calculated.');
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
