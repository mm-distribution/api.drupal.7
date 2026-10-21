# PollTokenReplaceTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/poll/poll.test`](../_file.md), lines 628–634 · [local source](../../../../../source/modules/poll/poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test#L628-L634)
- **Class:** [PollTokenReplaceTestCase](../PollTokenReplaceTestCase.md)
- **Module/theme:** poll

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Poll token replacement',
      'description' => 'Generates text using placeholders for dummy content to check poll token replacement.',
      'group' => 'Poll',
    );
  }
```

---
_Drupal 7.103 · [modules/poll/poll.test](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._
