# DBLogTestCase::testFilter()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 502–569 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L502-L569)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
protected function testFilter()
```

## Documentation

```text
Tests the database log filter functionality at admin/reports/dblog.
```

## Code

```php
  protected function testFilter() {
    $this->drupalLogin($this->big_user);

    // Clear the log to ensure that only generated entries will be found.
    db_delete('watchdog')->execute();

    // Generate 9 random watchdog entries.
    $type_names = array();
    $types = array();
    for ($i = 0; $i < 3; $i++) {
      $type_names[] = $type_name = $this->randomName();
      $severity = WATCHDOG_EMERGENCY;
      for ($j = 0; $j < 3; $j++) {
        $types[] = $type = array(
          'count' => $j + 1,
          'type' => $type_name,
          'severity' => $severity++,
        );
        $this->generateLogEntries($type['count'], $type['type'], $type['severity']);
      }
    }

    // View the database log page.
    $this->drupalGet('admin/reports/dblog');

    // Confirm that all the entries are displayed.
    $count = $this->getTypeCount($types);
    foreach ($types as $key => $type) {
      $this->assertEqual($count[$key], $type['count'], 'Count matched');
    }

    // Filter by each type and confirm that entries with various severities are
    // displayed.
    foreach ($type_names as $type_name) {
      $edit = array(
        'type[]' => array($type_name),
      );
      $this->drupalPost(NULL, $edit, t('Filter'));

      // Count the number of entries of this type.
      $type_count = 0;
      foreach ($types as $type) {
        if ($type['type'] == $type_name) {
          $type_count += $type['count'];
        }
      }

      $count = $this->getTypeCount($types);
      $this->assertEqual(array_sum($count), $type_count, 'Count matched');
    }

    // Set the filter to match each of the two filter-type attributes and
    // confirm the correct number of entries are displayed.
    foreach ($types as $key => $type) {
      $edit = array(
        'type[]' => array($type['type']),
        'severity[]' => array($type['severity']),
      );
      $this->drupalPost(NULL, $edit, t('Filter'));

      $count = $this->getTypeCount($types);
      $this->assertEqual(array_sum($count), $type['count'], 'Count matched');
    }

    // Clear all logs and make sure the confirmation message is found.
    $this->drupalPost('admin/reports/dblog', array(), t('Clear log messages'));
    $this->assertText(t('Database log cleared.'), 'Confirmation message found');
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
