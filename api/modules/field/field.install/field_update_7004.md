# field_update_7004()

- **Type:** Function
- **File:** [`modules/field/field.install`](_file.md), lines 473–489 · [local source](../../../../source/modules/field/field.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install#L473-L489)
- **Module/theme:** field
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function field_update_7004()
```

## Documentation

```text
Grant the new "administer fields" permission to trusted users.
```

## Code

```php
function field_update_7004() {
  // Assign the permission to anyone that already has a trusted core permission
  // that would have previously let them administer fields on an entity type.
  $rids = array();
  $permissions = array(
    'administer site configuration',
    'administer content types',
    'administer users',
  );
  foreach ($permissions as $permission) {
    $rids = array_merge($rids, array_keys(user_roles(FALSE, $permission)));
  }
  $rids = array_unique($rids);
  foreach ($rids as $rid) {
    _update_7000_user_role_grant_permissions($rid, array('administer fields'), 'field');
  }
}
```

---
_Drupal 7.103 · [modules/field/field.install](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install) · Licensed GPL-2.0-or-later (see LICENSE)._
