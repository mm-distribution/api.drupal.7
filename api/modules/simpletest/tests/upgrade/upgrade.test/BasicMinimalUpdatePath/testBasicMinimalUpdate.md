# BasicMinimalUpdatePath::testBasicMinimalUpdate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.test`](../_file.md), lines 537–613 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test#L537-L613)
- **Class:** [BasicMinimalUpdatePath](../BasicMinimalUpdatePath.md)
- **Module/theme:** batch_test

## Signature

```php
public function testBasicMinimalUpdate()
```

## Documentation

```text
Tests a successful point release update.
```

## Code

```php
  public function testBasicMinimalUpdate() {
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

    // Confirm that a date format that just differs in the case can be added.
    $admin_date_format = 'j M y';
    $edit = array('date_format' => $admin_date_format);
    $this->drupalPost('admin/config/regional/date-time/formats/add', $edit, t('Add format'));

    // Add a new date format which just differs in the case.
    $admin_date_format_uppercase = 'j M Y';
    $edit = array('date_format' => $admin_date_format_uppercase);
    $this->drupalPost('admin/config/regional/date-time/formats/add', $edit, t('Add format'));
    $this->assertText(t('Custom date format added.'));

    // Verify that the unique key on {date_formats}.format still exists.
    try {
      // The PostgreSQL driver appends suffixes to keys/indexes according to
      // their types. A unique key is a key (not an index), so it has a _key
      // suffix. It is not possible to call db_index_exists() as this function
      // will check the index name with _idx suffix, so it will never succeed on
      // PostgreSQL. An attempt to create a new unique key when it exists should
      // fail and the thrown exception will confirm that the unique key exists.
      // MySQL and SQLite are not affected by this change, as they do not append
      // suffixes to keys/indexes names.
      db_add_unique_key('date_formats', 'formats', array('formats'));
      // This is executed if no exception has been thrown and the unique key
      // did not already exist.
      $this->fail('Unique key on {date_formats} does not exist');
    }
    catch (DatabaseSchemaObjectExistsException $e) {
      // Exception confirms that the unique key already existed.
      $this->pass('Unique key on {date_formats} exists');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test) · Licensed GPL-2.0-or-later (see LICENSE)._
