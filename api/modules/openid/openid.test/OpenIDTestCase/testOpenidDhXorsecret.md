# OpenIDTestCase::testOpenidDhXorsecret()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 693–695 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L693-L695)
- **Class:** [OpenIDTestCase](../OpenIDTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testOpenidDhXorsecret()
```

## Documentation

```text
Test _openid_dh_xorsecret().
```

## Code

```php
  function testOpenidDhXorsecret() {
    $this->assertEqual(_openid_dh_xorsecret('123456790123456790123456790', "abc123ABC\x00\xFF"), "\xa4'\x06\xbe\xf1.\x00y\xff\xc2\xc1", '_openid_dh_xorsecret() returned expected result.');
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
