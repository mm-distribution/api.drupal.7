# SystemValidTokenTest::testTokenValidation()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 3099–3120 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3099-L3120)
- **Class:** [SystemValidTokenTest](../SystemValidTokenTest.md)
- **Module/theme:** system

## Signature

```php
public function testTokenValidation()
```

## Documentation

```text
Tests invalid invocations of drupal_valid_token() that must return FALSE.
```

## Code

```php
  public function testTokenValidation() {
    // The following checks will throw PHP notices, so we disable error
    // assertions.
    $this->assertErrors = FALSE;

    try {
      $this->assertFalse(drupal_valid_token(NULL, new stdClass()), 'Token NULL, value object returns FALSE.');
    }
    // PHP 7.4 compatibility: the stdClass string conversion throws an exception
    // which is also an acceptable outcome of this test.
    catch (Error $e) {
      $this->pass('Token NULL, value object throws error exception which is ok.');
    }

    $this->assertFalse(drupal_valid_token(0, array()), 'Token 0, value array returns FALSE.');
    $this->assertFalse(drupal_valid_token('', array()), "Token '', value array returns FALSE.");
    $this->assertFalse('' === drupal_get_token(array()), 'Token generation does not return an empty string on invalid parameters.');
    $this->assertErrors = TRUE;

    $this->assertFalse(drupal_valid_token(TRUE, 'foo'), 'Token TRUE, value foo returns FALSE.');
    $this->assertFalse(drupal_valid_token(0, 'foo'), 'Token 0, value foo returns FALSE.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
