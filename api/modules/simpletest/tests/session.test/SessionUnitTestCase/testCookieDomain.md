# SessionUnitTestCase::testCookieDomain()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 858–868 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L858-L868)
- **Class:** [SessionUnitTestCase](../SessionUnitTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCookieDomain()
```

## Documentation

_No docblock in source._

## Code

```php
  function testCookieDomain() {
     $tests = array(
       array('example.com', '.example.com'),
       array('www.example.com', '.www.example.com'),
       array('subdomain.example.com', '.subdomain.example.com'),
     );

     foreach ($tests as $test) {
       $this->assertEqual(_drupal_get_cookie_domain($test[0]), $test[1], 'Correct $cookie_domain for host ' . $test[0]);
     }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
