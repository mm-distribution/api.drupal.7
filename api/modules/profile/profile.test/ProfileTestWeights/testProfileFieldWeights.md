# ProfileTestWeights::testProfileFieldWeights()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 297–312 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L297-L312)
- **Class:** [ProfileTestWeights](../ProfileTestWeights.md)
- **Module/theme:** profile

## Signature

```php
function testProfileFieldWeights()
```

## Documentation

_No docblock in source._

## Code

```php
  function testProfileFieldWeights() {
    $this->drupalLogin($this->admin_user);

    $category = $this->randomName();
    $field1 = $this->createProfileField('textfield', $category, array('weight' => 1));
    $field2 = $this->createProfileField('textfield', $category, array('weight' => -1));

    $this->setProfileField($field1, $this->randomName(8));
    $this->setProfileField($field2, $this->randomName(8));

    $profile_edit = $this->drupalGet('user/' . $this->normal_user->uid . '/edit/' . $category);
    $this->assertTrue(strpos($profile_edit, $field1['title']) > strpos($profile_edit, $field2['title']), 'Profile field weights are respected on the user edit form.');

    $profile_page = $this->drupalGet('user/' . $this->normal_user->uid);
    $this->assertTrue(strpos($profile_page, $field1['title']) > strpos($profile_page, $field2['title']), 'Profile field weights are respected on the user profile page.');
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
