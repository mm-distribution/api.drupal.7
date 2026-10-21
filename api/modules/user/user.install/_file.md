# modules/user/user.install

- **Source:** [local](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · 975 lines
- **Module/theme:** user

## File documentation

```text
@file
Install, update and uninstall functions for the user module.
```

## Functions (derived index)

- [user_schema()](user_schema.md) — Implements hook_schema().
- [user_install()](user_install.md) — Implements hook_install().
- [user_update_dependencies()](user_update_dependencies.md) — Implements hook_update_dependencies().
- [_update_7000_user_role_grant_permissions()](_update_7000_user_role_grant_permissions.md) — Utility function: grant a set of permissions to a role during update.
- [user_update_7000()](user_update_7000.md) — Increase the length of the password field to accommodate better hashes.
- [user_update_7001()](user_update_7001.md) — Remove the 'threshold', 'mode' and 'sort' columns from the {users} table.
- [user_update_7002()](user_update_7002.md) — Convert user time zones from time zone offsets to time zone names.
- [user_update_7003()](user_update_7003.md) — Update user settings for cancelling user accounts.
- [user_update_7005()](user_update_7005.md) — Changes the users table to allow longer e-mail addresses.
- [user_update_7006()](user_update_7006.md) — Add module data to {role_permission}.
- [user_update_7007()](user_update_7007.md) — Add a weight column to user roles.
- [user_update_7008()](user_update_7008.md) — If 'user_register' variable was unset in Drupal 6, set it to be the same as the Drupal 6 default setting.
- [user_update_7009()](user_update_7009.md) — Converts fields that store serialized variables from text to blob.
- [user_update_7010()](user_update_7010.md) — Update the {user}.signature_format column.
- [user_update_7011()](user_update_7011.md) — Placeholder function.
- [user_update_7012()](user_update_7012.md) — Add the user's pictures to the {file_managed} table and make them managed files.
- [user_update_7013()](user_update_7013.md) — Add user module file usage entries.
- [user_update_7014()](user_update_7014.md) — Rename the 'post comments without approval' permission.
- [user_update_7015()](user_update_7015.md) — Change {users}.signature_format into varchar.
- [user_update_7016()](user_update_7016.md) — Update the database to match the schema.
- [user_update_7017()](user_update_7017.md) — Update email templates to use new tokens.
- [user_update_7018()](user_update_7018.md) — Ensure there is an index on {users}.picture.
- [user_update_7019()](user_update_7019.md) — Ensure there is a combined index on {authmap}.uid and {authmap}.module.
- [user_update_7020()](user_update_7020.md) — Add changed field to users table.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
