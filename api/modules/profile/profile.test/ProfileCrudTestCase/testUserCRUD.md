# ProfileCrudTestCase::testUserCRUD()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 515–537 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L515-L537)
- **Class:** [ProfileCrudTestCase](../ProfileCrudTestCase.md)
- **Module/theme:** profile

## Signature

```php
public function testUserCRUD()
```

## Documentation

```text
Test profile integration with user CRUD operations.
```

## Code

```php
  public function testUserCRUD() {
    // @todo Add profile fields in addition to base user properties.
    $edit = array(
      'name' => 'Test user',
      'mail' => 'test@example.com',
    );

    // Create.
    // @todo Add assertions.
    $account = user_save(NULL, $edit);

    // Read.
    // @todo Add assertions.
    $account = user_load($account->uid);

    // Update.
    // @todo Add assertions.
    $account = user_save($account, $edit);

    // Delete.
    // @todo Add assertions.
    user_delete($account->uid);
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
