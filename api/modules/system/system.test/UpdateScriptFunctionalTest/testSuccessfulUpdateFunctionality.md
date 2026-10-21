# UpdateScriptFunctionalTest::testSuccessfulUpdateFunctionality()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2666–2690 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2666-L2690)
- **Class:** [UpdateScriptFunctionalTest](../UpdateScriptFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function testSuccessfulUpdateFunctionality()
```

## Documentation

```text
Tests update.php after performing a successful update.
```

## Code

```php
  function testSuccessfulUpdateFunctionality() {
    drupal_set_installed_schema_version('update_script_test', drupal_get_installed_schema_version('update_script_test') - 1);
    // Click through update.php with 'administer software updates' permission.
    $this->drupalLogin($this->update_user);
    $this->drupalPost($this->update_url, array(), t('Continue'), array('external' => TRUE));
    $this->drupalPost(NULL, array(), t('Apply pending updates'));
    $this->assertText('Updates were attempted.');
    $this->assertLink('site');
    $this->assertNoLink('Administration pages');
    $this->assertNoLink('logged');
    $this->clickLink('Front page');
    $this->assertResponse(200);

    drupal_set_installed_schema_version('update_script_test', drupal_get_installed_schema_version('update_script_test') - 1);
    // Click through update.php with 'access administration pages' and
    // 'access site reports' permissions.
    $admin_user = $this->drupalCreateUser(array('administer software updates', 'access administration pages', 'access site reports'));
    $this->drupalLogin($admin_user);
    $this->drupalPost($this->update_url, array(), t('Continue'), array('external' => TRUE));
    $this->drupalPost(NULL, array(), t('Apply pending updates'));
    $this->assertText('Updates were attempted.');
    $this->assertLink('logged');
    $this->clickLink('Administration pages');
    $this->assertResponse(200);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
