# UserCancelTestCase

- **Type:** Class
- **File:** [`modules/user/user.test`](_file.md), lines 965–1360 · [local source](../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L965-L1360)
- **Module/theme:** user

## Signature

```php
class UserCancelTestCase extends DrupalWebTestCase
```

## Documentation

```text
Test cancelling a user.
```

## Properties

### $admin_user

```php
protected $admin_user;
```

## Methods (derived index)

- [getInfo()](UserCancelTestCase/getInfo.md)
- [setUp()](UserCancelTestCase/setUp.md)
- [testUserCancelWithoutPermission()](UserCancelTestCase/testUserCancelWithoutPermission.md) — Attempt to cancel account without permission.
- [testUserCancelUid1()](UserCancelTestCase/testUserCancelUid1.md) — Tests that user account for uid 1 cannot be cancelled.
- [testUserCancelInvalid()](UserCancelTestCase/testUserCancelInvalid.md) — Attempt invalid account cancellations.
- [testUserBlock()](UserCancelTestCase/testUserBlock.md) — Disable account and keep all content.
- [testUserBlockUnpublish()](UserCancelTestCase/testUserBlockUnpublish.md) — Disable account and unpublish all content.
- [testUserAnonymize()](UserCancelTestCase/testUserAnonymize.md) — Delete account and anonymize all content.
- [testUserDelete()](UserCancelTestCase/testUserDelete.md) — Delete account and remove all content.
- [testUserCancelByAdmin()](UserCancelTestCase/testUserCancelByAdmin.md) — Create an administrative user and delete another user.
- [testMassUserCancelByAdmin()](UserCancelTestCase/testMassUserCancelByAdmin.md) — Create an administrative user and mass-delete other users.

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
