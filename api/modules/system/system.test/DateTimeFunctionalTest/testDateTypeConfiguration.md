# DateTimeFunctionalTest::testDateTypeConfiguration()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1375–1402 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1375-L1402)
- **Class:** [DateTimeFunctionalTest](../DateTimeFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function testDateTypeConfiguration()
```

## Documentation

```text
Test date type configuration.
```

## Code

```php
  function testDateTypeConfiguration() {
    // Confirm system date types appear.
    $this->drupalGet('admin/config/regional/date-time');
    $this->assertText(t('Medium'), 'System date types appear in date type list.');
    $this->assertNoRaw('href="/admin/config/regional/date-time/types/medium/delete"', 'No delete link appear for system date types.');

    // Add custom date type.
    $this->clickLink(t('Add date type'));
    $date_type = strtolower($this->randomName(8));
    $machine_name = 'machine_' . $date_type;
    $date_format = 'd.m.Y - H:i';
    $edit = array(
      'date_type' => $date_type,
      'machine_name' => $machine_name,
      'date_format' => $date_format,
    );
    $this->drupalPost('admin/config/regional/date-time/types/add', $edit, t('Add date type'));
    $this->assertEqual($this->getUrl(), url('admin/config/regional/date-time', array('absolute' => TRUE)), 'Correct page redirection.');
    $this->assertText(t('New date type added successfully.'), 'Date type added confirmation message appears.');
    $this->assertText($date_type, 'Custom date type appears in the date type list.');
    $this->assertText(t('delete'), 'Delete link for custom date type appears.');

    // Delete custom date type.
    $this->clickLink(t('delete'));
    $this->drupalPost('admin/config/regional/date-time/types/' . $machine_name . '/delete', array(), t('Remove'));
    $this->assertEqual($this->getUrl(), url('admin/config/regional/date-time', array('absolute' => TRUE)), 'Correct page redirection.');
    $this->assertText(t('Removed date type ' . $date_type), 'Custom date type removed.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
