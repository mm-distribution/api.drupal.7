# ProfileBlockTestCase::setUp()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 396–415 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L396-L415)
- **Class:** [ProfileBlockTestCase](../ProfileBlockTestCase.md)
- **Module/theme:** profile

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();

    // Login the admin user.
    $this->drupalLogin($this->admin_user);

    // Create two fields.
    $category = $this->randomName();
    $this->field1 = $this->createProfileField('textfield', $category, array('weight' => 0));
    $this->field2 = $this->createProfileField('textfield', $category, array('weight' => 1));

    // Assign values to those fields.
    $this->value1 = $this->setProfileField($this->field1);
    $this->value2 = $this->setProfileField($this->field2);

    // Create a node authored by the normal user.
    $this->node = $this->drupalCreateNode(array(
      'uid' => $this->normal_user->uid,
    ));
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
