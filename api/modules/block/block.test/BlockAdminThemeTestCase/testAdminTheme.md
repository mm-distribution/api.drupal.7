# BlockAdminThemeTestCase::testAdminTheme()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 468–482 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L468-L482)
- **Class:** [BlockAdminThemeTestCase](../BlockAdminThemeTestCase.md)
- **Module/theme:** block

## Signature

```php
function testAdminTheme()
```

## Documentation

```text
Check for the accessibility of the admin theme on the  block admin page.
```

## Code

```php
  function testAdminTheme() {
    // Create administrative user.
    $admin_user = $this->drupalCreateUser(array('administer blocks', 'administer themes'));
    $this->drupalLogin($admin_user);

    // Ensure that access to block admin page is denied when theme is disabled.
    $this->drupalGet('admin/structure/block/list/stark');
    $this->assertResponse(403, 'The block admin page for a disabled theme can not be accessed');

    // Enable admin theme and confirm that tab is accessible.
    $edit['admin_theme'] = 'stark';
    $this->drupalPost('admin/appearance', $edit, t('Save configuration'));
    $this->drupalGet('admin/structure/block/list/stark');
    $this->assertResponse(200, 'The block admin page for the admin theme can be accessed');
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
