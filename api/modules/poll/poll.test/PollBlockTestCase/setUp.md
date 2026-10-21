# PollBlockTestCase::setUp()

- **Type:** Method
- **File:** [`modules/poll/poll.test`](../_file.md), lines 380–386 · [local source](../../../../../source/modules/poll/poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test#L380-L386)
- **Class:** [PollBlockTestCase](../PollBlockTestCase.md)
- **Module/theme:** poll

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('poll');

    // Create and login user
    $admin_user = $this->drupalCreateUser(array('administer blocks'));
    $this->drupalLogin($admin_user);
  }
```

---
_Drupal 7.103 · [modules/poll/poll.test](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._
