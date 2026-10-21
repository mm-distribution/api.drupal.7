# MenuRouterTestCase::testAuthUserUserLogin()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 241–252 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L241-L252)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAuthUserUserLogin()
```

## Documentation

```text
Test that an authenticated user hitting 'user/login' gets redirected to
'user' and 'user/register' gets redirected to the user edit page.
```

## Code

```php
  function testAuthUserUserLogin() {
    $loggedInUser = $this->drupalCreateUser(array());
    $this->drupalLogin($loggedInUser);

    $this->drupalGet('user/login');
    // Check that we got to 'user'.
    $this->assertTrue($this->url == url('user', array('absolute' => TRUE)), "Logged-in user redirected to q=user on accessing q=user/login");

    // user/register should redirect to user/UID/edit.
    $this->drupalGet('user/register');
    $this->assertTrue($this->url == url('user/' . $this->loggedInUser->uid . '/edit', array('absolute' => TRUE)), "Logged-in user redirected to q=user/UID/edit on accessing q=user/register");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
