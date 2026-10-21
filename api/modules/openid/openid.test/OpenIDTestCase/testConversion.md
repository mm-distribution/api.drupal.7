# OpenIDTestCase::testConversion()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 682–688 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L682-L688)
- **Class:** [OpenIDTestCase](../OpenIDTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testConversion()
```

## Documentation

```text
Test _openid_dh_XXX_to_XXX() functions.
```

## Code

```php
  function testConversion() {
    $this->assertIdentical(_openid_dh_long_to_base64('12345678901234567890123456789012345678901234567890'), 'CHJ/Y2mq+DyhUCZ0evjH8ZbOPwrS', '_openid_dh_long_to_base64() returned expected result.');
    $this->assertIdentical(_openid_dh_base64_to_long('BsH/g8Nrpn2dtBSdu/sr1y8hxwyx'), '9876543210987654321098765432109876543210987654321', '_openid_dh_base64_to_long() returned expected result.');

    $this->assertIdentical(_openid_dh_long_to_binary('12345678901234567890123456789012345678901234567890'), "\x08r\x7fci\xaa\xf8<\xa1P&tz\xf8\xc7\xf1\x96\xce?\x0a\xd2", '_openid_dh_long_to_binary() returned expected result.');
    $this->assertIdentical(_openid_dh_binary_to_long("\x06\xc1\xff\x83\xc3k\xa6}\x9d\xb4\x14\x9d\xbb\xfb+\xd7/!\xc7\x0c\xb1"), '9876543210987654321098765432109876543210987654321', '_openid_dh_binary_to_long() returned expected result.');
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
