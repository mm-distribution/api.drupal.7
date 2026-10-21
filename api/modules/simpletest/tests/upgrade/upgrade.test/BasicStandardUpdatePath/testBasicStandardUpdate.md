# BasicStandardUpdatePath::testBasicStandardUpdate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.test`](../_file.md), lines 461–506 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test#L461-L506)
- **Class:** [BasicStandardUpdatePath](../BasicStandardUpdatePath.md)
- **Module/theme:** batch_test

## Signature

```php
public function testBasicStandardUpdate()
```

## Documentation

```text
Tests a successful point release update.
```

## Code

```php
  public function testBasicStandardUpdate() {
    $this->assertTrue($this->performUpgrade(), 'The upgrade was completed successfully.');

    // Hit the frontpage.
    $this->drupalGet('');
    $this->assertResponse(200);

    // Verify that we are still logged in.
    $this->drupalGet('user');
    $this->clickLink(t('Edit'));
    $this->assertEqual($this->getUrl(), url('user/1/edit', array('absolute' => TRUE)), 'We are still logged in as admin at the end of the upgrade.');

    // Logout and verify that we can login back in with our initial password.
    $this->drupalLogout();
    $this->drupalLogin((object) array(
      'uid' => 1,
      'name' => 'admin',
      'pass_raw' => 'admin',
    ));

    // The previous login should've triggered a password rehash, so login one
    // more time to make sure the new hash is readable.
    $this->drupalLogout();
    $this->drupalLogin((object) array(
      'uid' => 1,
      'name' => 'admin',
      'pass_raw' => 'admin',
    ));

    // Test that the site name is correctly displayed.
    $this->assertText('Drupal', 'The site name is correctly displayed.');

    // Verify that the main admin sections are available.
    $this->drupalGet('admin');
    $this->assertText(t('Content'));
    $this->assertText(t('Appearance'));
    $this->assertText(t('People'));
    $this->assertText(t('Configuration'));
    $this->assertText(t('Reports'));
    $this->assertText(t('Structure'));
    $this->assertText(t('Modules'));

    // Confirm that no {menu_links} entry exists for user/autocomplete.
    $result = db_query('SELECT COUNT(*) FROM {menu_links} WHERE link_path = :user_autocomplete', array(':user_autocomplete' => 'user/autocomplete'))->fetchField();
    $this->assertFalse($result, 'No {menu_links} entry exists for user/autocomplete');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test) · Licensed GPL-2.0-or-later (see LICENSE)._
