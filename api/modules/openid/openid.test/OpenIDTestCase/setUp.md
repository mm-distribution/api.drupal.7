# OpenIDTestCase::setUp()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 674–677 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L674-L677)
- **Class:** [OpenIDTestCase](../OpenIDTestCase.md)
- **Module/theme:** openid

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('openid');
    module_load_include('inc', 'openid');
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
