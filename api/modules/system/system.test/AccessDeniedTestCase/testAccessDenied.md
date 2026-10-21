# AccessDeniedTestCase::testAccessDenied()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1067–1130 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1067-L1130)
- **Class:** [AccessDeniedTestCase](../AccessDeniedTestCase.md)
- **Module/theme:** system

## Signature

```php
function testAccessDenied()
```

## Documentation

_No docblock in source._

## Code

```php
  function testAccessDenied() {
    $this->drupalGet('admin');
    $this->assertText(t('Access denied'), 'Found the default 403 page');
    $this->assertResponse(403);

    $this->drupalLogin($this->admin_user);
    $edit = array(
      'title' => $this->randomName(10),
      'body' => array(LANGUAGE_NONE => array(array('value' => $this->randomName(100)))),
    );
    $node = $this->drupalCreateNode($edit);

    // Use a custom 403 page.
    $this->drupalPost('admin/config/system/site-information', array('site_403' => 'node/' . $node->nid), t('Save configuration'));

    $this->drupalLogout();
    $this->drupalGet('admin');
    $this->assertText($node->title, 'Found the custom 403 page');

    // Logout and check that the user login block is shown on custom 403 pages.
    $this->drupalLogout();

    $this->drupalGet('admin');
    $this->assertText($node->title, 'Found the custom 403 page');
    $this->assertText(t('User login'), 'Blocks are shown on the custom 403 page');

    // Log back in and remove the custom 403 page.
    $this->drupalLogin($this->admin_user);
    $this->drupalPost('admin/config/system/site-information', array('site_403' => ''), t('Save configuration'));

    // Logout and check that the user login block is shown on default 403 pages.
    $this->drupalLogout();

    $this->drupalGet('admin');
    $this->assertText(t('Access denied'), 'Found the default 403 page');
    $this->assertResponse(403);
    $this->assertText(t('User login'), 'Blocks are shown on the default 403 page');

    // Log back in, set the custom 403 page to /user and remove the block
    $this->drupalLogin($this->admin_user);
    variable_set('site_403', 'user');
    $this->drupalPost('admin/structure/block', array('blocks[user_login][region]' => '-1'), t('Save blocks'));

    // Check that we can log in from the 403 page.
    $this->drupalLogout();
    $edit = array(
      'name' => $this->admin_user->name,
      'pass' => $this->admin_user->pass_raw,
    );
    $this->drupalPost('admin/config/system/site-information', $edit, t('Log in'));

    // Check that we're still on the same page.
    $this->assertText(t('Site information'));

    // Check batch page response.
    $query_parameters = array(
      ':type' => 'php',
      ':severity' => WATCHDOG_WARNING,
    );
    $this->assertEqual(db_query('SELECT COUNT(*) FROM {watchdog} WHERE type = :type AND severity = :severity', $query_parameters)->fetchField(), 0, 'No warning message appears in the logs before accessing the batch page.');
    $this->drupalGet('batch');
    $this->assertResponse(403);
    $this->assertEqual(db_query('SELECT COUNT(*) FROM {watchdog} WHERE type = :type AND severity = :severity', $query_parameters)->fetchField(), 0, 'No warning message appears in the logs after accessing the batch page.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
