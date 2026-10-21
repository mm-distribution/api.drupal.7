# UpdateScriptFunctionalTest::testNoUpdateFunctionality()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2645–2661 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2645-L2661)
- **Class:** [UpdateScriptFunctionalTest](../UpdateScriptFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function testNoUpdateFunctionality()
```

## Documentation

```text
Tests update.php when there are no updates to apply.
```

## Code

```php
  function testNoUpdateFunctionality() {
    // Click through update.php with 'administer software updates' permission.
    $this->drupalLogin($this->update_user);
    $this->drupalPost($this->update_url, array(), t('Continue'), array('external' => TRUE));
    $this->assertText(t('No pending updates.'));
    $this->assertNoLink('Administration pages');
    $this->clickLink('Front page');
    $this->assertResponse(200);

    // Click through update.php with 'access administration pages' permission.
    $admin_user = $this->drupalCreateUser(array('administer software updates', 'access administration pages'));
    $this->drupalLogin($admin_user);
    $this->drupalPost($this->update_url, array(), t('Continue'), array('external' => TRUE));
    $this->assertText(t('No pending updates.'));
    $this->clickLink('Administration pages');
    $this->assertResponse(200);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
