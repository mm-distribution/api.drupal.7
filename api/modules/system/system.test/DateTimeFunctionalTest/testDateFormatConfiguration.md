# DateTimeFunctionalTest::testDateFormatConfiguration()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1407–1457 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1407-L1457)
- **Class:** [DateTimeFunctionalTest](../DateTimeFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function testDateFormatConfiguration()
```

## Documentation

```text
Test date format configuration.
```

## Code

```php
  function testDateFormatConfiguration() {
    // Confirm 'no custom date formats available' message appears.
    $this->drupalGet('admin/config/regional/date-time/formats');
    $this->assertText(t('No custom date formats available.'), 'No custom date formats message appears.');

    // Add custom date format.
    $this->clickLink(t('Add format'));
    $edit = array(
      'date_format' => 'Y',
    );
    $this->drupalPost('admin/config/regional/date-time/formats/add', $edit, t('Add format'));
    $this->assertEqual($this->getUrl(), url('admin/config/regional/date-time/formats', array('absolute' => TRUE)), 'Correct page redirection.');
    $this->assertNoText(t('No custom date formats available.'), 'No custom date formats message does not appear.');
    $this->assertText(t('Custom date format added.'), 'Custom date format added.');

    // Ensure custom date format appears in date type configuration options.
    $this->drupalGet('admin/config/regional/date-time');
    $this->assertRaw('<option value="Y">', 'Custom date format appears in options.');

    // Edit custom date format.
    $this->drupalGet('admin/config/regional/date-time/formats');
    $this->clickLink(t('edit'));
    $edit = array(
      'date_format' => 'Y m',
    );
    $this->drupalPost($this->getUrl(), $edit, t('Save format'));
    $this->assertEqual($this->getUrl(), url('admin/config/regional/date-time/formats', array('absolute' => TRUE)), 'Correct page redirection.');
    $this->assertText(t('Custom date format updated.'), 'Custom date format successfully updated.');

    // Check that ajax callback is protected by CSRF token.
    $this->drupalGet('admin/config/regional/date-time/formats/lookup', array('query' => array('format' => 'Y m d')));
    $this->assertResponse(403, 'Access denied with no token');
    $this->drupalGet('admin/config/regional/date-time/formats/lookup', array('query' => array('token' => 'invalid', 'format' => 'Y m d')));
    $this->assertResponse(403, 'Access denied with invalid token');
    $this->drupalGet('admin/config/regional/date-time/formats');
    $this->clickLink(t('edit'));
    $settings = $this->drupalGetSettings();
    $lookup_url = $settings['dateTime']['date-format']['lookup'];
    preg_match('/token=([^&]+)/', $lookup_url, $matches);
    $this->assertFalse(empty($matches[1]), 'Found token value');
    $this->drupalGet('admin/config/regional/date-time/formats/lookup', array('query' => array('token' => $matches[1], 'format' => 'Y m d')));
    $this->assertResponse(200, 'Access allowed with valid token');
    $this->assertText(format_date(time(), 'custom', 'Y m d'));

    // Delete custom date format.
    $this->drupalGet('admin/config/regional/date-time/formats');
    $this->clickLink(t('delete'));
    $this->drupalPost($this->getUrl(), array(), t('Remove'));
    $this->assertEqual($this->getUrl(), url('admin/config/regional/date-time/formats', array('absolute' => TRUE)), 'Correct page redirection.');
    $this->assertText(t('Removed date format'), 'Custom date format removed successfully.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
