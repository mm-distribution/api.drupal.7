# UserAccountLinksUnitTests::testSecondaryMenu()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1987–2018 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1987-L2018)
- **Class:** [UserAccountLinksUnitTests](../UserAccountLinksUnitTests.md)
- **Module/theme:** user

## Signature

```php
function testSecondaryMenu()
```

## Documentation

```text
Tests the secondary menu.
```

## Code

```php
  function testSecondaryMenu() {
    // Create a regular user.
    $user = $this->drupalCreateUser(array());

    // Log in and get the homepage.
    $this->drupalLogin($user);
    $this->drupalGet('<front>');

    // For a logged-in user, expect the secondary menu to have links for "My
    // account" and "Log out".
    $link = $this->xpath('//ul[@id=:menu_id]/li/a[contains(@href, :href) and text()=:text]', array(
      ':menu_id' => 'secondary-menu-links',
      ':href' => 'user',
      ':text' => 'My account',
    ));
    $this->assertEqual(count($link), 1, 'My account link is in secondary menu.');

    $link = $this->xpath('//ul[@id=:menu_id]/li/a[contains(@href, :href) and text()=:text]', array(
      ':menu_id' => 'secondary-menu-links',
      ':href' => 'user/logout',
      ':text' => 'Log out',
    ));
    $this->assertEqual(count($link), 1, 'Log out link is in secondary menu.');

    // Log out and get the homepage.
    $this->drupalLogout();
    $this->drupalGet('<front>');

    // For a logged-out user, expect no secondary links.
    $element = $this->xpath('//ul[@id=:menu_id]', array(':menu_id' => 'secondary-menu-links'));
    $this->assertEqual(count($element), 0, 'No secondary-menu for logged-out users.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
