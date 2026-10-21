# DrupalWebTestCase::drupalLogout()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1388–1400 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1388-L1400)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function drupalLogout()
```

## Documentation

_No docblock in source._

## Code

```php
  protected function drupalLogout() {
    // Make a request to the logout page, and redirect to the user page, the
    // idea being if you were properly logged out you should be seeing a login
    // screen.
    $this->drupalGet('user/logout');
    $this->drupalGet('user');
    $pass = $this->assertField('name', t('Username field found.'), t('Logout'));
    $pass = $pass && $this->assertField('pass', t('Password field found.'), t('Logout'));

    if ($pass) {
      $this->loggedInUser = FALSE;
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
