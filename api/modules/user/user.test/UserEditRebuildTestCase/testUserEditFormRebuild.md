# UserEditRebuildTestCase::testUserEditFormRebuild()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2401–2427 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2401-L2427)
- **Class:** [UserEditRebuildTestCase](../UserEditRebuildTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserEditFormRebuild()
```

## Documentation

```text
Test user edit page when the form is set to rebuild.
```

## Code

```php
  function testUserEditFormRebuild() {
    $user1 = $this->drupalCreateUser(array('change own username'));
    $this->drupalLogin($user1);

    $roles = array_keys($user1->roles);
    // Save the user form twice.
    $edit = array();
    $edit['current_pass'] = $user1->pass_raw;
    $this->drupalPost("user/$user1->uid/edit", $edit, t('Save'));
    $this->assertRaw(t("The changes have been saved."));
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertRaw(t("The changes have been saved."));
    $saved_user1 = entity_load_unchanged('user', $user1->uid);
    $this->assertEqual(count($roles), count($saved_user1->roles), 'Count of user roles in database matches original count.');
    $diff = array_diff(array_keys($saved_user1->roles), $roles);
    $this->assertTrue(empty($diff), format_string('User roles in database match original: @roles', array('@roles' => implode(', ', $saved_user1->roles))));
    // Set variable that causes the form to be rebuilt in user_form_test.module.
    variable_set('user_form_test_user_profile_form_rebuild', TRUE);
    $this->drupalPost("user/$user1->uid/edit", $edit, t('Save'));
    $this->assertRaw(t("The changes have been saved."));
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertRaw(t("The changes have been saved."));
    $saved_user1 = entity_load_unchanged('user', $user1->uid);
    $this->assertEqual(count($roles), count($saved_user1->roles), 'Count of user roles in database matches original count.');
    $diff = array_diff(array_keys($saved_user1->roles), $roles);
    $this->assertTrue(empty($diff), format_string('User roles in database match original: @roles', array('@roles' => implode(', ', $saved_user1->roles))));
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
