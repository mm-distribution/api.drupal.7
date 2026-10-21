# PollVoteCheckHostname::setUp()

- **Type:** Method
- **File:** [`modules/poll/poll.test`](../_file.md), lines 493–521 · [local source](../../../../../source/modules/poll/poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test#L493-L521)
- **Class:** [PollVoteCheckHostname](../PollVoteCheckHostname.md)
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

    // Create and login user.
    $this->admin_user = $this->drupalCreateUser(array('administer permissions', 'create poll content'));
    $this->drupalLogin($this->admin_user);

    // Allow anonymous users to vote on polls.
    user_role_change_permissions(DRUPAL_ANONYMOUS_RID, array(
      'access content' => TRUE,
      'vote on polls' => TRUE,
      'cancel own vote' => TRUE,
    ));

    // Enable page cache to verify that the result page is not saved in the
    // cache when anonymous voting is allowed.
    variable_set('cache', 1);

    // Create poll.
    $title = $this->randomName();
    $choices = $this->_generateChoices(3);
    $this->poll_nid = $this->pollCreate($title, $choices, FALSE);

    $this->drupalLogout();

    // Create web users.
    $this->web_user1 = $this->drupalCreateUser(array('access content', 'vote on polls', 'cancel own vote'));
    $this->web_user2 = $this->drupalCreateUser(array('access content', 'vote on polls'));
  }
```

---
_Drupal 7.103 · [modules/poll/poll.test](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._
