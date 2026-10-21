# DrupalWebTestCase::drupalCreateRole()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1275–1301 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1275-L1301)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function drupalCreateRole(array $permissions, $name = NULL)
```

## Documentation

```text
Creates a role with specified permissions.

@param $permissions
  Array of permission names to assign to role.
@param $name
  (optional) String for the name of the role.  Defaults to a random string.
@return
  Role ID of newly created role, or FALSE if role creation failed.
```

## Code

```php
  protected function drupalCreateRole(array $permissions, $name = NULL) {
    // Generate random name if it was not passed.
    if (!$name) {
      $name = $this->randomName();
    }

    // Check the all the permissions strings are valid.
    if (!$this->checkPermissions($permissions)) {
      return FALSE;
    }

    // Create new role.
    $role = new stdClass();
    $role->name = $name;
    user_role_save($role);
    user_role_grant_permissions($role->rid, $permissions);

    $this->assertTrue(isset($role->rid), t('Created role of name: @name, id: @rid', array('@name' => $name, '@rid' => (isset($role->rid) ? $role->rid : t('-n/a-')))), t('Role'));
    if ($role && !empty($role->rid)) {
      $count = db_query('SELECT COUNT(*) FROM {role_permission} WHERE rid = :rid', array(':rid' => $role->rid))->fetchField();
      $this->assertTrue($count == count($permissions), t('Created permissions: @perms', array('@perms' => implode(', ', $permissions))), t('Role'));
      return $role->rid;
    }
    else {
      return FALSE;
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
