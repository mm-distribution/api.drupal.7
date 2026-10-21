# OpenIDTestCase::testOpenidExtractNamespace()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 769–801 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L769-L801)
- **Class:** [OpenIDTestCase](../OpenIDTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testOpenidExtractNamespace()
```

## Documentation

```text
Test openid_extract_namespace().
```

## Code

```php
  function testOpenidExtractNamespace() {
    $response = array(
      'openid.sreg.nickname' => 'john',
      'openid.ns.ext1' => OPENID_NS_SREG,
      'openid.ext1.nickname' => 'george',
      'openid.ext1.email' => 'george@example.com',
      'openid.ns.ext2' => 'http://example.com/ns/ext2',
      'openid.ext2.foo' => '123',
      'openid.ext2.bar' => '456',
      'openid.signed' => 'sreg.nickname,ns.ext1,ext1.email,ext2.foo',
    );

    $values = openid_extract_namespace($response, 'http://example.com/ns/dummy', NULL, FALSE);
    $this->assertEqual($values, array(), 'Nothing found for unused namespace.');

    $values = openid_extract_namespace($response, 'http://example.com/ns/dummy', 'sreg', FALSE);
    $this->assertEqual($values, array('nickname' => 'john'), 'Value found for fallback prefix.');

    $values = openid_extract_namespace($response, OPENID_NS_SREG, 'sreg', FALSE);
    $this->assertEqual($values, array('nickname' => 'george', 'email' => 'george@example.com'), 'Namespace takes precedence over fallback prefix.');

    // ext1.email is signed, but ext1.nickname is not.
    $values = openid_extract_namespace($response, OPENID_NS_SREG, 'sreg', TRUE);
    $this->assertEqual($values, array('email' => 'george@example.com'), 'Unsigned namespaced fields ignored.');

    $values = openid_extract_namespace($response, 'http://example.com/ns/ext2', 'sreg', FALSE);
    $this->assertEqual($values, array('foo' => '123', 'bar' => '456'), 'Unsigned fields found.');

    // ext2.foo and ext2.bar are ignored, because ns.ext2 is not signed. The
    // fallback prefix is not used, because the namespace is specified.
    $values = openid_extract_namespace($response, 'http://example.com/ns/ext2', 'sreg', TRUE);
    $this->assertEqual($values, array(), 'Unsigned fields ignored.');
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
