# ContactPersonalTestCase::setUp()

- **Type:** Method
- **File:** [`modules/contact/contact.test`](../_file.md), lines 314–324 · [local source](../../../../../source/modules/contact/contact.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test#L314-L324)
- **Class:** [ContactPersonalTestCase](../ContactPersonalTestCase.md)
- **Module/theme:** contact

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('contact');

    // Create an admin user.
    $this->admin_user = $this->drupalCreateUser(array('administer contact forms', 'administer users'));

    // Create some normal users with their contact forms enabled by default.
    variable_set('contact_default_status', TRUE);
    $this->web_user = $this->drupalCreateUser(array('access user contact forms'));
    $this->contact_user = $this->drupalCreateUser();
  }
```

---
_Drupal 7.103 · [modules/contact/contact.test](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test) · Licensed GPL-2.0-or-later (see LICENSE)._
