# PollTestCase::pollUpdate()

- **Type:** Method
- **File:** [`modules/poll/poll.test`](../_file.md), lines 177–181 · [local source](../../../../../source/modules/poll/poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test#L177-L181)
- **Class:** [PollTestCase](../PollTestCase.md)
- **Module/theme:** poll

## Signature

```php
function pollUpdate($nid, $title, $edit)
```

## Documentation

_No docblock in source._

## Code

```php
  function pollUpdate($nid, $title, $edit) {
    // Edit the poll node.
    $this->drupalPost('node/' . $nid . '/edit', $edit, t('Save'));
    $this->assertText(t('@type @title has been updated.', array('@type' => node_type_get_name('poll'), '@title' => $title)), 'Poll has been updated.');
  }
```

---
_Drupal 7.103 · [modules/poll/poll.test](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._
