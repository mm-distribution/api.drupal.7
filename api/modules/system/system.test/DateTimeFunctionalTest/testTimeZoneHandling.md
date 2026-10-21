# DateTimeFunctionalTest::testTimeZoneHandling()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1344–1370 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1344-L1370)
- **Class:** [DateTimeFunctionalTest](../DateTimeFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function testTimeZoneHandling()
```

## Documentation

```text
Test time zones and DST handling.
```

## Code

```php
  function testTimeZoneHandling() {
    // Setup date/time settings for Honolulu time.
    variable_set('date_default_timezone', 'Pacific/Honolulu');
    variable_set('configurable_timezones', 0);
    variable_set('date_format_medium', 'Y-m-d H:i:s O');

    // Create some nodes with different authored-on dates.
    $date1 = '2007-01-31 21:00:00 -1000';
    $date2 = '2007-07-31 21:00:00 -1000';
    $node1 = $this->drupalCreateNode(array('created' => strtotime($date1), 'type' => 'article'));
    $node2 = $this->drupalCreateNode(array('created' => strtotime($date2), 'type' => 'article'));

    // Confirm date format and time zone.
    $this->drupalGet("node/$node1->nid");
    $this->assertText('2007-01-31 21:00:00 -1000', 'Date should be identical, with GMT offset of -10 hours.');
    $this->drupalGet("node/$node2->nid");
    $this->assertText('2007-07-31 21:00:00 -1000', 'Date should be identical, with GMT offset of -10 hours.');

    // Set time zone to Los Angeles time.
    variable_set('date_default_timezone', 'America/Los_Angeles');

    // Confirm date format and time zone.
    $this->drupalGet("node/$node1->nid");
    $this->assertText('2007-01-31 23:00:00 -0800', 'Date should be two hours ahead, with GMT offset of -8 hours.');
    $this->drupalGet("node/$node2->nid");
    $this->assertText('2007-08-01 00:00:00 -0700', 'Date should be three hours ahead, with GMT offset of -7 hours.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
