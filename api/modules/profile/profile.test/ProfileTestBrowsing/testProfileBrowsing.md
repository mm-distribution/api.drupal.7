# ProfileTestBrowsing::testProfileBrowsing()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 487–497 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L487-L497)
- **Class:** [ProfileTestBrowsing](../ProfileTestBrowsing.md)
- **Module/theme:** profile

## Signature

```php
function testProfileBrowsing()
```

## Documentation

```text
Test profile browsing.
```

## Code

```php
  function testProfileBrowsing() {
    $this->drupalLogin($this->admin_user);
    $field = $this->createProfileField('list', 'simpletest', array('page' => '%value'));

    // Set a random value for the profile field.
    $value = $this->setProfileField($field);

    // Check that user is found on the profile browse page.
    $this->drupalGet("profile/{$field['form_name']}/$value");
    $this->assertText($this->normal_user->name);
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
