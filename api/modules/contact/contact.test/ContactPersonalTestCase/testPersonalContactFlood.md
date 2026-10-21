# ContactPersonalTestCase::testPersonalContactFlood()

- **Type:** Method
- **File:** [`modules/contact/contact.test`](../_file.md), lines 414–439 · [local source](../../../../../source/modules/contact/contact.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test#L414-L439)
- **Class:** [ContactPersonalTestCase](../ContactPersonalTestCase.md)
- **Module/theme:** contact

## Signature

```php
function testPersonalContactFlood()
```

## Documentation

```text
Tests the personal contact form flood protection.
```

## Code

```php
  function testPersonalContactFlood() {
    $flood_limit = 3;
    variable_set('contact_threshold_limit', $flood_limit);

    // Clear flood table in preparation for flood test and allow other checks to complete.
    db_delete('flood')->execute();
    $num_records_flood = db_query("SELECT COUNT(*) FROM {flood}")->fetchField();
    $this->assertIdentical($num_records_flood, '0', 'Flood table emptied.');

    $this->drupalLogin($this->web_user);

    // Submit contact form with correct values and check flood interval.
    for ($i = 0; $i < $flood_limit; $i++) {
      $this->submitPersonalContact($this->contact_user);
      $this->assertText(t('Your message has been sent.'), 'Message sent.');
    }

    // Submit contact form one over limit.
    $this->drupalGet('user/' . $this->contact_user->uid. '/contact');
    $this->assertRaw(t('You cannot send more than %number messages in @interval. Try again later.', array('%number' => $flood_limit, '@interval' => format_interval(variable_get('contact_threshold_window', 3600)))), 'Normal user denied access to flooded contact form.');

    // Test that the admin user can still access the contact form even though
    // the flood limit was reached.
    $this->drupalLogin($this->admin_user);
    $this->assertNoText('Try again later.', 'Admin user not denied access to flooded contact form.');
  }
```

---
_Drupal 7.103 · [modules/contact/contact.test](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test) · Licensed GPL-2.0-or-later (see LICENSE)._
