# UserValidationTestCase::testMailAddresses()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 296–307 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L296-L307)
- **Class:** [UserValidationTestCase](../UserValidationTestCase.md)
- **Module/theme:** user

## Signature

```php
function testMailAddresses()
```

## Documentation

_No docblock in source._

## Code

```php
  function testMailAddresses() {
    $test_cases = array( // '<username>' => array('<description>', 'assert<testName>'),
      ''                => array('Empty mail address', 'assertNotNull'),
      'foo'             => array('Invalid mail address', 'assertNotNull'),
      'foo@example.com' => array('Valid mail address', 'assertNull'),
    );
    foreach ($test_cases as $name => $test_case) {
      list($description, $test) = $test_case;
      $result = user_validate_mail($name);
      $this->$test($result, $description . ' (' . $name . ')');
    }
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
