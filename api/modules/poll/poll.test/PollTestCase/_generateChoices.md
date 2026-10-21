# PollTestCase::_generateChoices()

- **Type:** Method
- **File:** [`modules/poll/poll.test`](../_file.md), lines 108–114 · [local source](../../../../../source/modules/poll/poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test#L108-L114)
- **Class:** [PollTestCase](../PollTestCase.md)
- **Module/theme:** poll

## Signature

```php
function _generateChoices($count = 7)
```

## Documentation

_No docblock in source._

## Code

```php
  function _generateChoices($count = 7) {
    $choices = array();
    for ($i = 1; $i <= $count; $i++) {
      $choices[] = $this->randomName();
    }
    return $choices;
  }
```

---
_Drupal 7.103 · [modules/poll/poll.test](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._
