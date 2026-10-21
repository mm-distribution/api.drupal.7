# UserTimeZoneFunctionalTest::testUserTimeZone()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1873–1921 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1873-L1921)
- **Class:** [UserTimeZoneFunctionalTest](../UserTimeZoneFunctionalTest.md)
- **Module/theme:** user

## Signature

```php
function testUserTimeZone()
```

## Documentation

```text
Tests the display of dates and time when user-configurable time zones are set.
```

## Code

```php
  function testUserTimeZone() {
    // Setup date/time settings for Los Angeles time.
    variable_set('date_default_timezone', 'America/Los_Angeles');
    variable_set('configurable_timezones', 1);

    // Override the 'medium' date format, which is the default for node
    // creation time. Since we are testing time zones with Daylight Saving
    // Time, and need to future proof against changes to the zoneinfo database,
    // we choose the 'I' format placeholder instead of a human-readable zone
    // name. With 'I', a 1 means the date is in DST, and 0 if not.
    variable_set('date_format_medium', 'Y-m-d H:i I');

    // Create a user account and login.
    $web_user = $this->drupalCreateUser();
    $this->drupalLogin($web_user);

    // Create some nodes with different authored-on dates.
    // Two dates in PST (winter time):
    $date1 = '2007-03-09 21:00:00 -0800';
    $date2 = '2007-03-11 01:00:00 -0800';
    // One date in PDT (summer time):
    $date3 = '2007-03-20 21:00:00 -0700';
    $node1 = $this->drupalCreateNode(array('created' => strtotime($date1), 'type' => 'article'));
    $node2 = $this->drupalCreateNode(array('created' => strtotime($date2), 'type' => 'article'));
    $node3 = $this->drupalCreateNode(array('created' => strtotime($date3), 'type' => 'article'));

    // Confirm date format and time zone.
    $this->drupalGet("node/$node1->nid");
    $this->assertText('2007-03-09 21:00 0', 'Date should be PST.');
    $this->drupalGet("node/$node2->nid");
    $this->assertText('2007-03-11 01:00 0', 'Date should be PST.');
    $this->drupalGet("node/$node3->nid");
    $this->assertText('2007-03-20 21:00 1', 'Date should be PDT.');

    // Change user time zone to Santiago time.
    $edit = array();
    $edit['mail'] = $web_user->mail;
    $edit['timezone'] = 'America/Santiago';
    $this->drupalPost("user/$web_user->uid/edit", $edit, t('Save'));
    $this->assertText(t('The changes have been saved.'), 'Time zone changed to Santiago time.');

    // Confirm date format and time zone.
    $this->drupalGet("node/$node1->nid");
    $this->assertText('2007-03-10 02:00 1', 'Date should be Chile summer time; five hours ahead of PST.');
    $this->drupalGet("node/$node2->nid");
    $this->assertText('2007-03-11 05:00 0', 'Date should be Chile time; four hours ahead of PST');
    $this->drupalGet("node/$node3->nid");
    $this->assertText('2007-03-21 00:00 0', 'Date should be Chile time; three hours ahead of PDT.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
