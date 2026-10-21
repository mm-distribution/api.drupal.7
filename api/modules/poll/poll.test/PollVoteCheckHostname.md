# PollVoteCheckHostname

- **Type:** Class
- **File:** [`modules/poll/poll.test`](_file.md), lines 479–622 · [local source](../../../../source/modules/poll/poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test#L479-L622)
- **Module/theme:** poll

## Signature

```php
class PollVoteCheckHostname extends PollTestCase
```

## Documentation

_No docblock in source._

## Properties

### $admin_user

```php
protected $admin_user;
```

### $poll_nid

```php
protected $poll_nid;
```

### $web_user1

```php
protected $web_user1;
```

### $web_user2

```php
protected $web_user2;
```

## Methods (derived index)

- [getInfo()](PollVoteCheckHostname/getInfo.md)
- [setUp()](PollVoteCheckHostname/setUp.md)
- [testHostnamePollVote()](PollVoteCheckHostname/testHostnamePollVote.md) — Check that anonymous users with same ip cannot vote on poll more than once unless user is logged in.

---
_Drupal 7.103 · [modules/poll/poll.test](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._
