# UserAccountLinksUnitTests::testDisabledAccountLink()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2023–2049 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2023-L2049)
- **Class:** [UserAccountLinksUnitTests](../UserAccountLinksUnitTests.md)
- **Module/theme:** user

## Signature

```php
function testDisabledAccountLink()
```

## Documentation

```text
Tests disabling the 'My account' link.
```

## Code

```php
  function testDisabledAccountLink() {
    // Create an admin user and log in.
    $this->drupalLogin($this->drupalCreateUser(array('access administration pages', 'administer menu')));

    // Verify that the 'My account' link is enabled.
    $this->drupalGet('admin/structure/menu/manage/user-menu');
    $label = $this->xpath('//label[contains(.,:text)]/@for', array(':text' => 'Enable My account menu link'));
    $this->assertFieldChecked((string) $label[0], "The 'My account' link is enabled by default.");

    // Disable the 'My account' link.
    $input = $this->xpath('//input[@id=:field_id]/@name', array(':field_id' => (string)$label[0]));
    $edit = array(
      (string) $input[0] => FALSE,
    );
    $this->drupalPost('admin/structure/menu/manage/user-menu', $edit, t('Save configuration'));

    // Get the homepage.
    $this->drupalGet('<front>');

    // Verify that the 'My account' link does not appear when disabled.
    $link = $this->xpath('//ul[@id=:menu_id]/li/a[contains(@href, :href) and text()=:text]', array(
      ':menu_id' => 'secondary-menu-links',
      ':href' => 'user',
      ':text' => 'My account',
    ));
    $this->assertEqual(count($link), 0, 'My account link is not in the secondary menu.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
