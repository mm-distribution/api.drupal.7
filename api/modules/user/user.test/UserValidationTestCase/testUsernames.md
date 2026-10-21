# UserValidationTestCase::testUsernames()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 268–293 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L268-L293)
- **Class:** [UserValidationTestCase](../UserValidationTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUsernames()
```

## Documentation

_No docblock in source._

## Code

```php
  function testUsernames() {
    $test_cases = array( // '<username>' => array('<description>', 'assert<testName>'),
      'foo'                    => array('Valid username', 'assertNull'),
      'FOO'                    => array('Valid username', 'assertNull'),
      'Foo O\'Bar'             => array('Valid username', 'assertNull'),
      'foo@bar'                => array('Valid username', 'assertNull'),
      'foo@example.com'        => array('Valid username', 'assertNull'),
      'foo@-example.com'       => array('Valid username', 'assertNull'), // invalid domains are allowed in usernames
      'þòøÇßªř€'               => array('Valid username', 'assertNull'),
      'foo+bar'                => array('Valid username', 'assertNull'), // '+' symbol is allowed
      'ᚠᛇᚻ᛫ᛒᛦᚦ'                => array('Valid UTF8 username', 'assertNull'), // runes
      ' foo'                   => array('Invalid username that starts with a space', 'assertNotNull'),
      'foo '                   => array('Invalid username that ends with a space', 'assertNotNull'),
      'foo  bar'               => array('Invalid username that contains 2 spaces \'&nbsp;&nbsp;\'', 'assertNotNull'),
      ''                       => array('Invalid empty username', 'assertNotNull'),
      'foo/'                   => array('Invalid username containing invalid chars', 'assertNotNull'),
      'foo' . chr(0) . 'bar'   => array('Invalid username containing chr(0)', 'assertNotNull'), // NULL
      'foo' . chr(13) . 'bar'  => array('Invalid username containing chr(13)', 'assertNotNull'), // CR
      str_repeat('x', USERNAME_MAX_LENGTH + 1) => array('Invalid excessively long username', 'assertNotNull'),
    );
    foreach ($test_cases as $name => $test_case) {
      list($description, $test) = $test_case;
      $result = user_validate_name($name);
      $this->$test($result, $description . ' (' . $name . ')');
    }
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
