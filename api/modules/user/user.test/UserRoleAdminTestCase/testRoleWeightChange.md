# UserRoleAdminTestCase::testRoleWeightChange()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2625–2646 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2625-L2646)
- **Class:** [UserRoleAdminTestCase](../UserRoleAdminTestCase.md)
- **Module/theme:** user

## Signature

```php
function testRoleWeightChange()
```

## Documentation

```text
Test user role weight change operation.
```

## Code

```php
  function testRoleWeightChange() {
    $this->drupalLogin($this->admin_user);

    // Pick up a random role and get its weight.
    $rid = array_rand(user_roles());
    $role = user_role_load($rid);
    $old_weight = $role->weight;

    // Change the role weight and submit the form.
    $edit = array('roles['. $rid .'][weight]' => $old_weight + 1);
    $this->drupalPost('admin/people/permissions/roles', $edit, t('Save order'));
    $this->assertText(t('The role settings have been updated.'), 'The role settings form submitted successfully.');

    // Retrieve the saved role and compare its weight.
    $role = user_role_load($rid);
    $new_weight = $role->weight;
    $this->assertTrue(($old_weight + 1) == $new_weight, 'Role weight updated successfully.');

    // Check if the updated weight is displayed on the roles settings page.
    $this->drupalGet('admin/people/permissions/roles');
    $this->assertFieldByXPath("//input[@name='roles[$rid][weight]']", $new_weight, 'The role weight is displayed correctly.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
