# UserAutocompleteTestCase::setUp()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1939–1945 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1939-L1945)
- **Class:** [UserAutocompleteTestCase](../UserAutocompleteTestCase.md)
- **Module/theme:** user

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

    // Set up two users with different permissions to test access.
    $this->unprivileged_user = $this->drupalCreateUser();
    $this->privileged_user = $this->drupalCreateUser(array('access user profiles'));
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
