# PollJSAddChoice::getInfo()

- **Type:** Method
- **File:** [`modules/poll/poll.test`](../_file.md), lines 443–449 · [local source](../../../../../source/modules/poll/poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test#L443-L449)
- **Class:** [PollJSAddChoice](../PollJSAddChoice.md)
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
      'name' => 'Poll add choice',
      'description' => 'Submits a POST request for an additional poll choice.',
      'group' => 'Poll'
    );
  }
```

---
_Drupal 7.103 · [modules/poll/poll.test](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._
