# UserAutocompleteTestCase::testUserAutocomplete()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1950–1964 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1950-L1964)
- **Class:** [UserAutocompleteTestCase](../UserAutocompleteTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserAutocomplete()
```

## Documentation

```text
Tests access to user autocompletion and verify the correct results.
```

## Code

```php
  function testUserAutocomplete() {
    // Check access from unprivileged user, should be denied.
    $this->drupalLogin($this->unprivileged_user);
    $this->drupalGet('user/autocomplete/' . $this->unprivileged_user->name[0]);
    $this->assertResponse(403, 'Autocompletion access denied to user without permission.');

    // Check access from privileged user.
    $this->drupalLogout();
    $this->drupalLogin($this->privileged_user);
    $this->drupalGet('user/autocomplete/' . $this->unprivileged_user->name[0]);
    $this->assertResponse(200, 'Autocompletion access allowed.');

    // Using first letter of the user's name, make sure the user's full name is in the results.
    $this->assertRaw($this->unprivileged_user->name, 'User name found in autocompletion results.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
